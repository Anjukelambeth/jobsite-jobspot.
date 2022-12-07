from dataclasses import fields
import json
from rest_framework.serializers import ModelSerializer
from .models import Account
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

class JobseekerSerializer(ModelSerializer):
    def validate_phone(self, value):
        lower_phone = value
        if Account.objects.filter(email__iexact=lower_phone).exists():
            raise serializers.ValidationError("Duplicate")
        return lower_phone

    class Meta:
        model = Account
        fields = ['id','phone_number', 'user_name', 'email', 'password', 'is_admin','is_dev' ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # user=self.context['request'].user
        instance = self.Meta.model(**validated_data) 
        if password is not None:
            instance.set_password(password)
        instance.is_dev=True
        instance.save()
        return instance

class RecruiterSerializer(ModelSerializer):
    

    def validate_phone(self, value):
        lower_phone = value
        if Account.objects.filter(email__iexact=lower_phone).exists():
            raise serializers.ValidationError("Duplicate")
        return lower_phone

    class Meta:
        model = Account
        fields = ['id', 'user_name', 'email', 'password', 'phone_number','is_admin','is_rec' ]
        extra_kwargs = {'password': {'write_only': True}}

    

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        phone_number=self.validate_phone('phone_number')
        # user=self.context['request'].user
        instance = self.Meta.model(**validated_data) 
        if password is not None:
            instance.set_password(password)
        instance.is_rec=True
        instance.save()
        return instance

class CompanyOwnerSerializer(ModelSerializer):
    
    def validate_phone(self, value):
        lower_phone = value
        if Account.objects.filter(email__iexact=lower_phone).exists():
            raise serializers.ValidationError("Duplicate")
        return lower_phone

    class Meta:
        model = Account
        fields = ['id', 'user_name', 'email', 'password', 'phone_number','is_admin','is_active' ]
        extra_kwargs = {'password': {'write_only': True}}

    

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        phone_number=self.validate_phone('phone_number')
        # user=self.context['request'].user
        instance = self.Meta.model(**validated_data) 
        if password is not None:
            instance.set_password(password)
        instance.is_active=False
        instance.save()
        return instance

    
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = ('username', 'email',)

