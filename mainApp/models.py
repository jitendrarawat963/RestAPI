from django.db import models

class employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    dsg = models.CharField(max_length=20)
    salary = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)


    def __str__(self):
        return str(self.id)+"/"+self.name
