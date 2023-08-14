from rest_framework import serializers
from .models import employee


class employeeserializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    dsg = serializers.CharField(max_length=20)
    salary = serializers.IntegerField()
    city = serializers.CharField(max_length=20)
    state = serializers.CharField(max_length=20)


    def create(self,validatedData):
        return employee.objects.create(**validatedData) 
    

    def update(self,instance,validatedData,):
        if("name" in validatedData and validatedData["name"]!=""):
            instance.name = validatedData["name"]
        if("dsg" in validatedData and validatedData["dsg"]!=""):
            instance.dsg = validatedData["dsg"]
        if("salary" in validatedData and validatedData["salary"]!=""):
            instance.salary = validatedData["salary"]
        if("city" in validatedData and validatedData["city"]!=""):
            instance.city = validatedData["city"]
        if("state" in validatedData and validatedData["state"]!=""):
            instance.state = validatedData["state"]
        instance.save()
        return instance
