from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

meses = {
    "january": "janero",
    "february": "feverero"
}

# Create your views here.
def january(request):
    return HttpResponse("that's work")

def february(request, month):
    return HttpResponse("feverero" + month)

def month_number(request, month):
    if(month>len(meses) or month<1):
        return HttpResponseNotFound("Invalid number")
    else:
        mes = list(meses.keys())
        return HttpResponseRedirect(mes[month-1])
    

def month(request, month):
    try:
        text = f"<h1>{meses[month]}</h1>"
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Nao tem esse mes muleque")