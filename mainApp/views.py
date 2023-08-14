from django.shortcuts import render,HttpResponse
from .models import employee
from rest_framework.renderers import JSONRenderer
from .serializers import employeeserializer
from django.db.models import Q
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

def homePage(Request):
    return render(Request,"index.html")

def getRecord(Request):
    data = employee.objects.all()
    dataserializer = employeeserializer(data,many=True)
    return HttpResponse(JSONRenderer().render(dataserializer.data),content_type="application/json")


def getSingleRecord(Request,id):
    data = employee.objects.get(id=id)
    dataserializer = employeeserializer(data)
    return HttpResponse(JSONRenderer().render(dataserializer.data),content_type="application/json")


def searchRecord(Request,search):
    data = employee.objects.filter(Q(name__contains=search)|Q(dsg__contains=search)|Q(salary__contains=search)|Q(city__contains=search)|Q(state__contains=search))
    dataserializer = employeeserializer(data,many=True)
    return HttpResponse(JSONRenderer().render(dataserializer.data),content_type="application/json")



@csrf_exempt
def createRecord(Request):
    jsonData  = Request.body
    stream = io.BytesIO(jsonData)
    pythonData = JSONParser().parse(stream)
    empserializer = employeeserializer(data=pythonData)
    if (empserializer.is_valid()):
        empserializer.save()
        msg = {"result":"Done","message":"Record Is Created !!!"}
    else:
        msg = {"result":"Failed","message":"Invalid Record !!!"}
    return HttpResponse(JSONRenderer().render(msg),content_type="application/json")


@csrf_exempt
def updateRecord(Request,id):
    jsonData  = Request.body
    stream = io.BytesIO(jsonData)
    pythonData = JSONParser().parse(stream)
    empserializer = employeeserializer(data=pythonData)
    try:
        emp = employee.objects.get(id=id)
        empserializer = employeeserializer(emp,data=pythonData,partial=True)
        if (empserializer.is_valid()):
            empserializer.save()
            msg = {"result":"Done","message":"Record Is Updated !!!"}
        else:
            msg = {"result":"Failed","message":"Invalid Record !!!"}
    except:
        msg = {"result":"Failed","message":"Invalid Record !!!"}
    return HttpResponse(JSONRenderer().render(msg),content_type="application/json")


@csrf_exempt
def deleteRecord(Request,id):
    try:
        data = employee.objects.get(id=id)
        data.delete()
        msg = {"result":"Done","message":"Record Is Delete !!!"}
    except:
        msg = {"result":"Failed","message":"Invalid Record !!!"}
    return HttpResponse(JSONRenderer().render(msg),content_type="application/json")



