from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Country,
    Producer,
    Car
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
        producers = Producer.objects.filter(country__name=country_name).values('id', 'name')

        return  producers


class CountryProducerSerializator(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)

    name = serializers.CharField(max_length=255, required=True)


class ProducerSerializtor(serializers.ModelSerializer):

    class Meta:
        model = Producer
        fields = ('name', 'country', 'cars',)

    name = serializers.CharField(max_length=255, required=True)
    country = CountryProducerSerializator()
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
    

class ProducerCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ('name',)

    name = serializers.CharField(max_length=255, required=True)


class CarSerializator(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name', 'producer', 'year_start', 'year_end')
        # fields = ('name', 'producer', 'year_start', 'year_end', 'comments')

    producer = ProducerCarSerializer()
    name = serializers.CharField(max_length=128)
    # comments = serializers.SerializerMethodField('_get_comments')

    def _get_comments(self, car):
        pass

    def create(self, validated_data):
        name = validated_data.pop('name')
        year_start = validated_data.pop('year_start')
        year_end = validated_data.pop('year_end')
        
        try:
            producer = Producer.objects.get(name=validated_data.pop('producer').pop('name'))
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
        pass
