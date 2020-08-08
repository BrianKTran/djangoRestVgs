from rest_framework import serializers
from vgsRestApp.models import creditCardInfo

class creditCardInfoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model=creditCardInfo
        # fields=('card_number','exp_date', 'cvv')
        fields='__all__'