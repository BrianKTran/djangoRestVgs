from django.db import models

# Create your models here.

class creditCardInfo(models.Model):
    card_number=models.CharField(max_length=16)
    exp_date=models.CharField(max_length=5)
    cvv=models.CharField(max_length=3)

    def __str__(self):
        return self.card_number + ' ' + self.exp_date + ' ' + self.cvv
    