git clone https://github.com/BrianKTran/djangoRestVgs.git

python --version # make sure you are using python 3

pip install django djangorestframework requests

python manage.py runserver

Go to http://127.0.0.1:8000/index/

Enter Sentitive CC Data:
        Credit Card Number 
        CC Expiration 
        CC CVV
    Hit submit to Redact data

Hit refresh and hit ok to clear alert boxes 

Copy tokens from The Data Table below and 
paste to redact data form below

Enter Redacted Data:
        Credit Card Number Token
        CC Expiration Token
        CC CVV Token
   Hit submit to Reveal data

Hit refresh and hit ok to clear alert boxes 

See decrypted information in the Data Table below which has been sent to echo server