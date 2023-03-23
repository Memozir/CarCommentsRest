from rest_framework import serializers

from .models import Country


class CountrySerializator(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = "__all__"


class CountryCreateSerializator(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = "__all__"