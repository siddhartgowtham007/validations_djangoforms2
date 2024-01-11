from django.db import models

# Create your models here.


class Employee(models.Model):
    Eid=models.IntegerField()
    Ename=models.CharField(max_length=20)
    Erole=models.CharField(max_length=15)
    def __str__(self):
        return self.Ename