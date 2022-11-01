from urllib import response
from mailsender import views
from django.http import HttpResponse
from decouple import config
import requests
import json

# from stockproject import mailsender
from mailsender import views

apiKey = config('STOCK_API_KEY')

def Test(stockSymbol, firstValue, secondValue ):
    stockSymbol = stockSymbol.upper()
    print( stockSymbol, firstValue, secondValue )
    firstValue = float(firstValue)
    secondValue = float(secondValue)

    try:
        response = requests.get('https://api.twelvedata.com/time_series?apikey=03f25006a3764aaa84bd1d1843a7c915&interval=1min&symbol=petr4&format=JSON&outputsize=1')
    except ImportError as exc:
        raise ImportError(
            "Couldn't request the api. Are you sure it's the right apiKey? "
            "Perhaps you should check your Stock name as well "
            "does it appear on our Stock whitelist?"
            "If the error persists, get in touch with your administrator"
        ) from exc
    
    if response:
        data = response.json()
        value = float(data['values'][0]['close'])
        print("Live Stock Value: " + value )
    else:
        return
        
    """
        Precisa ter um loop aqui em algum lugar pra ficar infinitamente
        caso o
        emailtype retorne um Continue
    """
    emailType = ApiRequest.ValueComp(firstValue=firstValue, secondValue=secondValue, respValue=value)
    
    if emailType == "Continua":
        return 
    else:
        views.mailtester(emailtype=emailType)
    
    return



class ApiRequest():
    def Start(firstValue, secondValue, stockSymbol, apiKey):
        try:
            response = requests.get('https://api.twelvedata.com/time_series?apikey={}&interval=1min&symbol={}&format=JSON&outputsize=1', apiKey, stockSymbol.upper() )
        except ImportError as exc:
            raise ImportError(
                "Couldn't request the api. Are you sure it's the right apiKey? "
                "Perhaps you should check your Stock name as well "
                "Does it appear on our Stock whitelist?"
                "If the error persists, get in touch with your administrator"
            ) from exc
        if response:
            emailtype = ApiRequest.ValueComp(firstValue=firstValue, secondValue=secondValue, respValue=response.json())
            views.MailSender.mailsend(emailtype=emailtype)
        return

    def ValueComp(firstValue, secondValue, respValue):
        if firstValue >= secondValue:
            maxValue = firstValue
            minValue = secondValue
        else:
            maxValue = secondValue
            minValue = firstValue

        if (respValue >= maxValue):
            return "Venda"
        elif respValue >= minValue:
            return "Continua"
        else:
            return "Venda"
    