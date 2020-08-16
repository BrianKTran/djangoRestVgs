from django.db import models

# Create your models here.

class creditCardInfo(models.Model):
    cc_id=models.AutoField(primary_key=True)
    card_number=models.CharField(max_length=100)
    exp_date=models.CharField(max_length=100)
    cvv=models.CharField(max_length=100)

    def __str__(self):
        return self.cc_id+ ' ' + self.card_number + ' ' + self.exp_date + ' ' + self.cvv
    
