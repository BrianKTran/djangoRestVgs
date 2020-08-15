import json
import requests
# binToReg = b'a string'.decode('ascii')
# # regToBin = 'a string'.encode('ascii')


# print(binToReg)
# # print(regToBin)
def post (self, request):
    os.environ['HTTPS_PROXY'] = 'https://USi6vXVNrcsBYnpCMB7GciTg:2da52565-6e72-4a46-b419-245764f128ae@tntzrhiqrtg.SANDBOX.verygoodproxy.com:8080'
    response = requests.post('https://echo.apps.verygood.systems/post',
                            json={"card_number": request.data["card_number"],
                    "exp_date": request.data["exp_date"],
                    "cvv": request.data["cvv"]},
                    verify='./cert.pem')

print(str(response.content))