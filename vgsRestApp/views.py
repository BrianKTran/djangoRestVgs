from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import creditCardInfo
from . serializers import creditCardInfoSerializer
import requests
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def indexGet(request):
#         creditCard1=creditCardInfo.objects.all()
#         serializer=creditCardInfoSerializer(creditCard1, many=True)
#         return render(request,  'index.html')

# def indexPost(request):
        
#         creditCard2=creditCardInfo.objects.all() 
#         serializer1 = creditCardInfoSerializer(creditCard2, many=True)
#         response = requests.post("https://tntsfeqzp4a.sandbox.verygoodproxy.com/post/",
#                           json={'cc_number': 'card_number',
#                           'cc_exp': 'exp_date',
#                           'cc_cvv': 'cvv'})
        
#         serializer1.save()
#         return Response(serializer1.data, status=status.HTTP_201_CREATED)                  
#         # return render(request, 'index.html')

class index(APIView):
    def get(self, request):
        creditCard1=creditCardInfo.objects.all()
        serializer=creditCardInfoSerializer(creditCard1, many=True)
        return Response(serializer.data)
        # return render(request,  'index.html')
    def post():
        pass
class creditCardList(APIView):
    def get(self, request):
        creditCard1=creditCardInfo.objects.all()
        serializer=creditCardInfoSerializer(creditCard1, many=True)
        return Response(serializer.data)

    def post():
        response = requests.post("https://tntsfeqzp4a.sandbox.verygoodproxy.com/post/",
                          json={'cc_number': 'card_number',
                          'cc_exp': 'exp_date',
                          'cc_cvv': 'cvv'})
        pass


    
