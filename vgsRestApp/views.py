from django.shortcuts import render

# Create your views here.

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
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

# @api_view(['GET'])
def post(self, request):
        if request.method == "POST":
            a = request.POST.get('tag', 'default')
            print("printing", a)
            print(request.POST)
        return HttpResponse("Hello")

class index(APIView):
    
    def get(self, request):

        return render(request, 'index.html')

    

class creditCardList(APIView):
    def get(self, request):
        creditCard1 = creditCardInfo.objects.all()
        serializer = creditCardInfoSerializer(creditCard1, many=True)
        return Response(serializer.data)

    def post(self, request):
        creditCard1 = creditCardInfo.objects.all()
        serializer = creditCardInfoSerializer(data=creditCard1)
        # response = requests.post("https://tntsfeqzp4a.sandbox.verygoodproxy.com/post/",
        #                   json={'cc_number': 'card_number',
        #                   'cc_exp': 'exp_date',
        #                   'cc_cvv': 'cvv'})
        if serializer.is_valid(raise_exception=True):
            serializer.save(response)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return render(request, 'index.html', {'response': response

                                            #   })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # pass

#   os.environ['HTTPS_PROXY'] = 'https://USi6vXVNrcsBYnpCMB7GciTg:2da52565-6e72-4a46-b419-245764f128ae@tntzrhiqrtg.SANDBOX.verygoodproxy.com:8080'
#     res = requests.post('https://echo.apps.verygood.systems/post',
#                         json={'add_message': message},
#                         verify='/full/path/to/cert.pem')