from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TimeDepositProduct, SavingsProduct
from .serializers import TimeDepositProductSerializer, TimeDepositOptionSerializer, SavingsProductSerializer, SavingsOptionSerializer
import requests


@api_view(['GET'])
def save_time_deposits(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()

    for product in response.get('result').get('baseList'):
        save_data = {
            'dcls_month' : product.get('dcls_month'),
            'fin_co_no' : product.get('fin_co_no'),
            'fin_prdt_cd' : product.get('fin_prdt_cd'),
            'kor_co_nm' : product.get('kor_co_nm'),
            'fin_prdt_nm' : product.get('fin_prdt_nm'),
            'join_way' : product.get('join_way'),
            'mtrt_int' : product.get('mtrt_int'),
            'spcl_cnd' : product.get('spcl_cnd'),
            'join_deny' : product.get('join_deny'),
            'etc_note' : product.get('etc_note'),
            'max_limit' : product.get('max_limit'),
            'dcls_strt_day' : product.get('dcls_strt_day'),
            'dcls_end_day' : product.get('dcls_end_day'),
            'fin_co_subm_day' : product.get('fin_co_subm_day'),
        }
        serializer = TimeDepositProductSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for option in response.get('result').get('optionList'):
        save_data = {
            'dcls_month' : option.get('dcls_month'),
            'fin_co_no' : option.get('fin_co_no'),
            'fin_prdt_cd' : option.get('fin_prdt_cd'),
            'intr_rate_type' : option.get('intr_rate_type'),
            'intr_rate_type_nm' : option.get('intr_rate_type_nm'),
            'save_trm' : option.get('save_trm'),
            'intr_rate' : option.get('intr_rate'),
            'intr_rate2' : option.get('intr_rate2'),
        }
        serializer = TimeDepositOptionSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            product = TimeDepositProduct.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
            serializer.save(product=product)

    return JsonResponse({ 'message': 'Saved!' })


@api_view(['GET'])
def save_savings(request):
    api_key = settings.API_KEY
    url = f'https://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()

    for product in response.get('result').get('baseList'):
        save_data = {
            'dcls_month' : product.get('dcls_month'),
            'fin_co_no' : product.get('fin_co_no'),
            'fin_prdt_cd' : product.get('fin_prdt_cd'),
            'kor_co_nm' : product.get('kor_co_nm'),
            'fin_prdt_nm' : product.get('fin_prdt_nm'),
            'join_way' : product.get('join_way'),
            'mtrt_int' : product.get('mtrt_int'),
            'spcl_cnd' : product.get('spcl_cnd'),
            'join_deny' : product.get('join_deny'),
            'join_member' : product.get('join_member'),
            'etc_note' : product.get('etc_note'),
            'max_limit' : product.get('max_limit'),
            'dcls_strt_day' : product.get('dcls_strt_day'),
            'dcls_end_day' : product.get('dcls_end_day'),
            'fin_co_subm_day' : product.get('fin_co_subm_day'),
        }
        serializer = SavingsProductSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for option in response.get('result').get('optionList'):
        save_data = {
            'dcls_month' : option.get('dcls_month'),
            'fin_co_no' : option.get('fin_co_no'),
            'fin_prdt_cd' : option.get('fin_prdt_cd'),
            'intr_rate_type' : option.get('intr_rate_type'),
            'intr_rate_type_nm' : option.get('intr_rate_type_nm'),

            'rsrv_type' : option.get('rsrv_type'),
            'rsrv_type_nm' : option.get('rsrv_type_nm'),

            'save_trm' : option.get('save_trm'),
            'intr_rate' : option.get('intr_rate'),
            'intr_rate2' : option.get('intr_rate2'),
        }
        serializer = SavingsOptionSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            product = SavingsProduct.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
            serializer.save(product=product)
    
    return JsonResponse({ 'message': 'Saved!' })
