from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import status
from . models import creditCardInfo
from . serializers import creditCardInfoSerializer
import requests
from django.views.decorators.csrf import csrf_exempt
from django.template import loader



class index_view(APIView):

    def get(self, request):

        # index_temp = loader.get_template('index.html')index_temp.render,
        creditCard1 = creditCardInfo.objects.all()
        serializer = creditCardInfoSerializer(creditCard1, many=True)
        ser_data = serializer.data
        return Response(ser_data)

        # return render(request, template_name)

    def post(self, request):
        creditCard1 = creditCardInfo.objects.all()
        serializer = creditCardInfoSerializer(data=creditCard1)
        response = requests.post("https://tntsfeqzp4a.sandbox.verygoodproxy.com/post/",
                          json={'cc_number': 'card_number',
                          'cc_exp': 'exp_date',
                          'cc_cvv': 'cvv'})
        if serializer.is_valid(raise_exception=True):
            serializer.save(response)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # pass


# class creditCardList(APIView):
#     def get(self, request):
#         creditCard1 = creditCardInfo.objects.all()
#         serializer = creditCardInfoSerializer(creditCard1, many=True)
#         return Response(serializer.data)

    # def post():
    #     # response = requests.post("https://tntsfeqzp4a.sandbox.verygoodproxy.com/post/",
    #     #                   json={'cc_number': 'card_number',
    #     #                   'cc_exp': 'exp_date',
    #     #                   'cc_cvv': 'cvv'})
    #     pass
