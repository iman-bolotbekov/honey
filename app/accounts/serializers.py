from rest_framework import serializers
from django.urls import reverse_lazy
from django.db import IntegrityError

from . import models


class ClientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)
    password2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = models.Client
        exclude = ['user', 'code']

    def create(self, validated_data):
        try:
            user = models.User(username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.is_active = False
            user.save()
            client = models.Client.objects.create(
                email=validated_data['email'],
                user=user
            )
            return client
        except IntegrityError:
            raise serializers.ValidationError('Такой пользователь уже существует!')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли должны совпадать!')
        if len(data['password']) < 8 and len(data['password2']) < 8:
            raise serializers.ValidationError('Пароль не может быть меньше 8 символов!')
        return data


class ConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConfirmAccount
        fields = '__all__'

    def create(self, validated_data):
        pin = validated_data['pin']
        username = validated_data['username']
        user_confirm = models.User.objects.filter(username=username)
        user_values = user_confirm.values()
        try:
            for user_value in user_values:
                user_dict = user_value
            clients = models.Client.objects.filter(user_id=user_dict.get('id'))
            for client in clients:
                client_dict = client
            user = models.User.objects.get(id=user_dict.get('id'))
            obj = models.ConfirmAccount.objects.create(**validated_data)
            if username == user_dict.get('username') and pin == client_dict.code:
                user.is_active = True
                user.save()
                obj.save()
                return obj
        except:
            raise serializers.ValidationError('Неверный код или имя пользователя!')
