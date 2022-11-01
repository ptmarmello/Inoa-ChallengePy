import email
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from decouple import config

DEFAULT_FOM_EMAIL = config('EMAIL_HOST_USER')
EMAIL_SEND_TO = config('EMAIL_SEND_TO')

def mailtester(emailtype="Venda", message="Sorry, but something went wrong. Please contact your administrator."):
    if emailtype == "Venda":
        assunto = "Pode Vender"
        message = "Olá, Olá! Vende ai, amigo."
    elif emailtype == "Compre":
        assunto = "Pode Comprar"
        message = "Olá, Olá! Compra ai, amigo."
    else:
        assunto = "Something went wrong, budy"
        

    send_mail(assunto, message , DEFAULT_FOM_EMAIL, [ 'ptmarmello', 'ptmarmello' ])
    # print(message)
    return HttpResponse('Oh Hello, Peter. ' + message)

# Create your views here.
class MailSender():
    def mailsend(emailtype, message="Sorry, but something went wrong. Please contact your administrator."):
        if emailtype == "Venda":
            assunto = "Pode Vender"
            message = "Olá, Olá! Vende ai, amigo."
        elif emailtype == "Compre":
            assunto = "Pode Comprar"
            message = "Olá, Olá! Compra ai, amigo."
        else:
            return

        send_mail(assunto, message ,'towho', ['towho1','towho2'])

        return HttpResponse('Oh Hello, Peter')