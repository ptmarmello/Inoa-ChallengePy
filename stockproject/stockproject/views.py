from urllib import response
from xmlrpc.client import boolean
from mailsender import views
from django.http import HttpResponse
import requests

def Test():
    apiKey = "asdjhaksdjha"
    stockSymbolTest = input("Qual ação você deseja?")
    try:
        response = requests.get('https://api.twelvedata.com/time_series?apikey={}&interval=1min&symbol={}&format=JSON&outputsize=1', apiKey, stockSymbolTest.upper() )
    except ImportError as exc:
        raise ImportError(
            "Couldn't request the api. Are you sure it's the right apiKey? "
            "Perhaps you should check your Stock name as well "
            "does it appear on our Stock whitelist?"
            "If the error persists, get in touch with your administrator"
        ) from exc
    if response:
        print(response)
        HttpResponse(response)




class ApiRequest():
    def Start(firstValue, secondValue, stockSymbol, apiKey):
        try:
            response = requests.get('https://api.twelvedata.com/time_series?apikey={}&interval=1min&symbol={}&format=JSON&outputsize=1', apiKey, stockSymbol.upper() )
        except ImportError as exc:
            raise ImportError(
                "Couldn't request the api. Are you sure it's the right apiKey? "
                "Perhaps you should check your Stock name as well "
                "does it appear on our Stock whitelist?"
                "If the error persists, get in touch with your administrator"
            ) from exc
        if response:
            print(response)
            HttpResponse(response)
            emailtype = ApiRequest.ValueComp(firstValue=firstValue, secondValue=secondValue, respValue=response.json())
            views.MailSender.mailsend(emailtype=emailtype)
        return

    def ValueComp(firstValue, secondValue,respValue):
        if respValue >= firstValue:
            return "Venda"
        elif respValue <= secondValue:
            return "Compre"
        else:
            return "Continua"
    