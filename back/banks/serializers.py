from rest_framework import serializers
from .models import TimeDepositProduct, TimeDepositOption


class TimeDepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeDepositProduct
        fields = '__all__'


class TimeDepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeDepositOption
        exclude = ('product',)
        read_only_fields = ('product',)