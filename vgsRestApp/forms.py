from django.forms import ModelForm
from .models import creditCardInfo


class CreditCardForm(ModelForm):
    class Meta:
        model = creditCardInfo
        fields = '__all__'