from django.test import TestCase
from rest_framework import serializers
from Empapp.models import Employee
from Empapp.Serializers import EmployeeSerializer

class SerializerTestCase(TestCase):
    def test_valid_serializer(self):
        w = Employee.objects.create(empid=200, emp_num=1030,name='john',department='SPACE')
        data = {
                'empid': w.empid,
                'emp_num': w.emp_num,
                'name': w.name,
                'department': w.department,
                }
        serializer = EmployeeSerializer(w, data=data)
        #print(serializer.is_valid())
        #print(serializer.data)
        #print(serializer.validated_data)
        self.assertTrue(serializer.is_valid())

    def test_in_valid_serializer(self):
        w = Employee.objects.create(empid=200, emp_num=1030,name='',department='SPACE')
        data = {
                'empid': w.empid,
                'emp_num': w.emp_num,
                'name': w.name,
                'department': w.department,
                }
        serializer = EmployeeSerializer(w, data=data)
        self.assertFalse(serializer.is_valid())
