from django.db import models
from rest_framework import serializers
from .models import Employee

# Create your models here.
class EmployeeSerializer(serializers.ModelSerializer):
      class Meta:
           model = Employee
           fields='__all__'
