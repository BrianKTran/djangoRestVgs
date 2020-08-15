from django.shortcuts import render, redirect, HttpResponse
from .forms import CreditCardForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from . models import creditCardInfo
from . serializers import creditCardInfoSerializer
import requests
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from rest_framework import status
from django.shortcuts import render


class index(APIView):
    def get(self, request):
        return render(request, 'index.html')


class ccGet(APIView):
    def get(self, request):
        creditCard1 = creditCardInfo.objects.all()
        serializer = creditCardInfoSerializer(creditCard1, many=True)
        retData = serializer.data
        return Response(retData)


class ccPost(APIView):
    def post(self, request):
        creditCard1 = creditCardInfo.objects.all()
        response = requests.post("https://tntzrhiqrtg.sandbox.verygoodproxy.com/post",
                                 json={"card_number": request.data["card_number"],
                                       "exp_date": request.data["exp_date"],
                                       "cvv": request.data["cvv"]})
        # decode from binary string to regular string
        decode = response.content.decode('ascii')
        # parse json now that it is a regular string
        parsed = json.loads(decode)
        # parse the data for each field
        parseStr = json.loads(parsed['data'])
        # pass to serializer
        serializer = creditCardInfoSerializer(data=parseStr)
        # save to post method
        if serializer.is_valid():
            # if True:
            serializer.save()
        # print(parsed)
            return Response(parsed, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class postReveal(APIView):
    def post(self, request):
        creditCard1 = creditCardInfo.objects.all()
        os.environ['HTTPS_PROXY'] = 'https://USi6vXVNrcsBYnpCMB7GciTg:2da52565-6e72-4a46-b419-245764f128ae@tntzrhiqrtg.SANDBOX.verygoodproxy.com:8080'
        response = requests.post('https://echo.apps.verygood.systems/post',
                                 json={"card_number": request.data["card_number"],
                                       "exp_date": request.data["exp_date"],
                                       "cvv": request.data["cvv"]},
                                 verify='vgsRestApp/cert.pem')
        # decode from binary string to regular string
        decode = response.content.decode('ascii')
        # parse json now that it is a regular string
        parsed = json.loads(decode)
        # parse the data for each field
        parseStr = json.loads(parsed['data'])
        # pass to serializer
        serializer = creditCardInfoSerializer(data=parseStr)
        # save to post method
        if serializer.is_valid():
            # if True:
            serializer.save()
        # print(parsed)
            return Response(parsed, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

