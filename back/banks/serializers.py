from rest_framework import serializers
from .models import TimeDepositProduct, TimeDepositOption, SavingsProduct, SavingsOption


class TimeDepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeDepositProduct
        fields = '__all__'


class TimeDepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeDepositOption
        exclude = ('product',)
        read_only_fields = ('product',)


class SavingsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsProduct
        fields = '__all__'


class SavingsOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsOption
        exclude = ('product',)
        read_only_fields = ('product',)