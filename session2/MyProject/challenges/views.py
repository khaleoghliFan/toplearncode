from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#data:
days={"Monday":"today is monday",
      "Tuesday":"today is tuesday",
      "Wednesday":"today is wednesday",
      "Thursday":"today is thursday",
      "Friday":"today is friday",
      "Saturday":"today is saturday",
      "Sunday":"today is sunday",}
def hello_world(request):
    return HttpResponse("Hello World!")
def weekdays(request,day):
    data_days=days.get(day)
    return HttpResponse(f"day is {data_days}")



