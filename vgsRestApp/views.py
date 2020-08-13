from django.shortcuts import render, redirect, HttpResponse

from .forms import CreditCardForm
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
from rest_framework import status
from django.shortcuts import render

def index(self, request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
    if form.is_valid():
        form.save()
# return redirect('/ccPost/')
        return HttpResponse("data submitted successfully")


    else:
        form = CreditCardForm()

        return render(request, 'index.html', {'form': form})


def ccPost(request):

    return HttpResponse("data submitted successfully")


class index(APIView):

    def get(self, request):

        return render(request, 'index.html')


class ccGet(APIView):
    def get(self, request):
        creditCard1 = creditCardInfo.objects.all()
        serializer = creditCardInfoSerializer(creditCard1, many=True)
        retData = serializer.data
        return Response(retData)
        # return retData["json"]


class ccPost(APIView):

    def post(self, request): 
        # creditCard1 = creditCardInfo.objects.all()
        serializer = creditCardInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
# return Response(serializer.data, status=status.HTTP_201_CREATED)
# return render(request, 'index.html', {'response': response
            return redirect('/ccGet/')

# })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def insertCC(request):
#     if request.method=="POST":
#         card_number=request.POST.get('card_number')
#         exp_date=request.POST.get('exp_date')
#         cvv=request.POST.get('cvv')
#         data={'card_number': card_number, 'exp_date': exp_date, 'cvv': cvv}
#         headers={'Content-Type': 'application/json'}
#         read=requests.post('http://127.0.0.1:8000/ccPost/', json=data, headers=headers)
#         return render(request, 'index.html')
#     else:
#         return render(request, 'index.html')
# inbound
# response = requests.post("https://tntsfeqzp4a.sandbox.verygoodproxy.com/post/",
#                   json={'cc_number': 'card_number',
#                   'cc_exp': 'exp_date',raise_exception=True
#                   'cc_cvv': 'cvv'})response

# outbound
#   os.environ['HTTPS_PROXY'] = 'https://USi6vXVNrcsBYnpCMB7GciTg:2da52565-6e72-4a46-b419-245764f128ae@tntzrhiqrtg.SANDBOX.verygoodproxy.com:8080'
#     res = requests.post('https://echo.apps.verygood.systems/post',
#                         json={'add_message': message},
#                         verify='/full/path/to/cert.pem')
