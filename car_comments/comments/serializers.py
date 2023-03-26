from rest_framework import serializers

from .models import Country, Producer


class CountrySerializator(serializers.ModelSerializer):

    name = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = Country
        fields = ('name',)


class ProducerSerializtor(serializers.ModelSerializer):

    class Meta:
        model = Producer
        fields = ('name', 'country')

    name = serializers.CharField(max_length=255, required=True)
    country = CountrySerializator()

    def create(self, validated_data):
        country = Country.objects.get(name=validated_data.pop('country').pop('name'))
        producer_name = validated_data.pop('name')

        producer = Producer.objects.create(name=producer_name, country=country)

        return producer

# class CountryUpdateSerializator(serializers.ModelSerializer):

#     class Meta:
#         model = Country
#         fields = "__all__"


# class CountryCreateSerializator(serializers.ModelSerializer):

#     class Meta:
#         model = Country
#         fields = "__all__"


# class CountryDeleteSerializator(serializers.ModelSerializer):

#     class Meta:
#         model = Country
#         fields = "__all__"
