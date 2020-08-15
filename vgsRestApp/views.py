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
        # print('------------------------------------------------')
        # print(response)
        # print('------------------------------------------------')
        # decode from binary string to regular string
        decode = response.content.decode('ascii')
        # parse json now that it is a regular string
        parsed = json.loads(decode)
        # parse the data for each field
        parseStr = json.loads(parsed['data'])
        # print('------------------------------------------------')
        # print(parseStr)
        # print('------------------------------------------------')
        # pass to serializer
        serializer = creditCardInfoSerializer(data=parseStr)
        # save to post method
        if serializer.is_valid():
            # if True:
            serializer.save()
        # print(parsed)
            return Response(parsed, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# inbound
# response = requests.post("https://tntzrhiqrtg.sandbox.verygoodproxy.com/post/",
#                   json={"card_number": "card_number",
#                   "exp_date": "exp_date",raise_exception=True
#                   "cvv": "cvv"})response ....request.data

# outbound
#   os.environ['HTTPS_PROXY'] = 'https://USi6vXVNrcsBYnpCMB7GciTg:2da52565-6e72-4a46-b419-245764f128ae@tntzrhiqrtg.SANDBOX.verygoodproxy.com:8080'
#     res = requests.post('https://echo.apps.verygood.systems/post',
#                         json={"card_number": request.data["card_number"],
        #   "exp_date": request.data["exp_date"],
        #   "cvv": request.data["cvv"]})

# Print
        # 1 print({"card_number": "card_number",
        #           "exp_date": "exp_date",
        #           "cvv": "cvv"})
        # print('----------------------------')
        # 2 print({"card_number": request.data['card_number'],
        #           "exp_date": request.data['exp_date'],
        #           "cvv": request.data['cvv']})
        # 3 print(type(parsed))
        # 4 print(type(request.data))
        # 5 print(type(request))
        # 6 rint(request.data, type(request.data))

        # 7 print(parsed['data'], type(parsed['data']))

# Output
# 1 {'card_number': 'card_number', 'exp_date': 'exp_date', 'cvv': 'cvv'}
# ----------------------------
# 2 {'card_number': '4555555555555555', 'exp_date': '55555', 'cvv': '555'}
# 3 <class 'dict'>
# 4 <class 'dict'>
# 5 <class 'rest_framework.request.Request'>
# 6 {'card_number': '4555555555555555', 'exp_date': '55555', 'cvv': '555'} <class 'dict'>
# 7 {"card_number":"tok_sandbox_oKmqD4SVbYdfRwihjorTia","exp_date":"tok_sandbox_cQcSMSn3BpEGZaLJCjhJpz","cvv":"tok_sandbox_8c9bAL9xuP8duX8iY5Zy4s"} <class 'str'>
# {'args': {}, 'data': '{"card_number":"tok_sandbox_oKmqD4SVbYdfRwihjorTia","exp_date":"tok_sandbox_cQcSMSn3BpEGZaLJCjhJpz","cvv":"tok_sandbox_8c9bAL9xuP8duX8iY5Zy4s"}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip,
# deflate', 'Connection': 'close', 'Content-Length': '143', 'Content-Type': 'application/json', 'Host': 'echo.apps.verygood.systems', 'User-Agent': 'python-requests/2.24.0', 'Vgs-Request-Id': '79767bcacdb9f6793de7fdb7c0b118a6', 'Vgs-Tenant': 'tntzrhiqrtg', 'X-Forwarded-Host': 'tntzrhiqrtg.sandbox.verygoodproxy.com'}, 'json': {'card_number': 'tok_sandbox_oKmqD4SVbYdfRwihjorTia', 'cvv': 'tok_sandbox_8c9bAL9xuP8duX8iY5Zy4s', 'exp_date': 'tok_sandbox_cQcSMSn3BpEGZaLJCjhJpz'}, 'origin': '71.58.79.53, 52.7.148.215, 34.194.18.145, 10.22.91.166', 'url': 'https://echo.apps.verygood.systems/post'}
