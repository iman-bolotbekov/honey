from rest_framework import serializers

from .models import Tare, Honey, Basket, Feedback
from django.db.models import Q


class TareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tare
        fields = '__all__'


class HoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Honey
        fields = '__all__'
        read_only_fields = ['client', 'quantity']


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'
        read_only_fields = ['client', 'honey', 'quantity']
    #
    # def create(self, validated_data):
    #     validated_data['quantity'] += 1
    #     obj = Basket.objects.create(**validated_data)
    #     obj.quantity += 1
    #     obj.save()
    #     return obj


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        read_only_fields = ['client', ]