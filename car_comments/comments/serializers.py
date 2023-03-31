from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Country,
    Producer,
    Car,
    Comment
)


class CountrySerializator(serializers.ModelSerializer):

    name = serializers.CharField(max_length=255, required=True)
    producers = serializers.SerializerMethodField('_get_producers')

    class Meta:
        model = Country
        fields = ['name', 'producers']


    # def _is_producer(self) -> bool:
    #     if self.context.get('producer', False):
    #         self.Meta.fields.remove('producers')

    def _get_producers(self, country):
        country_name = getattr(country, 'name')
        producers = Producer.objects.filter(country__name=country_name).only('id', 'name').values('id', 'name')

        return  producers


class CountryProducerSerializator(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)

    name = serializers.CharField(max_length=255, required=True)


class ProducerSerializtor(serializers.ModelSerializer):

    class Meta:
        model = Producer
        fields = ('name', 'country', 'cars', 'comments')

    name = serializers.CharField(max_length=255, required=True)
    country = CountryProducerSerializator()
    cars = serializers.SerializerMethodField('_get_cars', read_only=True)
    comments = serializers.SerializerMethodField('_get_comments_count', read_only=True)

    def _get_comments_count(self, producer):
        cars = Car.objects.filter(producer=producer)
        comments_count = Comment.objects.filter(car__in=cars).count()

        return comments_count

    # country = CountryProducerSerializator()
    country = serializers.CharField(max_length=255, source='country.name')
    cars = serializers.SerializerMethodField('_get_cars')

    def _get_cars(self, producer):
        cars = Car.objects.filter(producer__name=producer).values()

        return cars

    def create(self, validated_data):

        try:
            country = Country.objects.get(name=validated_data.pop('country').pop('name'))
        except Exception:
            raise serializers.ValidationError({'error': 'country`s name does not exist'})
        
        producer_name = validated_data.pop('name')
        producer = Producer.objects.create(name=producer_name, country=country)

        return producer
    
    def update(self, instance, validated_data):

        try:
            country = Country.objects.get(name=validated_data.pop('country').pop('name'))
        except Exception:
            raise serializers.ValidationError({'error': 'country`s name does not exist'})        

        country = Country.objects.get(name=validated_data.pop('country').pop('name'))
        instance.name = validated_data.pop('name', False)
        instance.country = country
        instance.save()

        return instance
    

class CarDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ('name',)

    name = serializers.CharField(max_length=255, required=True)


class CarSerializator(serializers.ModelSerializer):
    class Meta:
        model = Car
        # fields = ('name', 'producer', 'year_start', 'year_end')
        fields = ('name', 'producer', 'year_start', 'year_end', 'comments', 'comments_count')

    producer = CarDefaultSerializer()
    name = serializers.CharField(max_length=128)
    comments = serializers.SerializerMethodField('_get_comments', read_only=True)
    comments_count = serializers.SerializerMethodField('_get_comments_count', read_only=True)

    def _get_comments_count(self, car):
        comments_count = Comment.objects.filter(car__name=car).count()

        return comments_count

    def _get_comments(self, car):
        comments = Comment.objects.filter(car__name=car).values()

        return comments

    def create(self, validated_data):
        name = validated_data.pop('name')
        year_start = validated_data.pop('year_start')
        year_end = validated_data.pop('year_end')
        
        try:
            producer = Car.objects.get(producer__name=validated_data.pop('producer').pop('name'))
        except Exception:
            raise serializers.ValidationError({'error': 'producer`s name does not exist'})

        car = Car.objects.create(
            name=name,
            producer=producer,
            year_start=year_start,
            year_end=year_end
        )

        return car
    
    def update(self, instance, validated_data):
        
        try:
            producer = Car.objects.get(producer__name=validated_data.pop('producer').pop('name'))
        except Exception:
            raise serializers.ValidationError({'error': 'produceres`s name does not exist'})
        
        name = validated_data.pop('name')
        year_start = validated_data.pop('year_start')
        year_end = validated_data.pop('year_end')

        instance.name = name
        instance.producer = producer
        instance.year_start = year_start
        instance.year_end = year_end
        instance.save()

        return instance

class CommentSerializator(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'email', 'car', 'comment_text', 'create_date')

    car = CarDefaultSerializer()

    def create(self, validated_data):
        email = validated_data.pop('email')
        car_name = validated_data.pop('car').pop('name')
        comment_text = validated_data.pop('comment_text')

        try:
            car = Car.objects.get(name=car_name)
        except Exception:
            raise serializers.ValidationError({'error': 'car`s name does not exist'})
        
        comment = Comment.objects.create(
            email=email,
            car=car,
            comment_text=comment_text
        )

        return comment
