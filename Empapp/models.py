from django.db import models

# Create your models here.
class Employee(models.Model):
      empid= models.IntegerField(primary_key=True)
      name = models.CharField(max_length=20)
      emp_num= models.IntegerField()
      department = models.CharField(max_length=20)


