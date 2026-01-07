# analytics/serializers.py
from rest_framework import serializers
from .models import Theater, Movie, TicketSale


class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class TicketSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketSale
        fields = '__all__'