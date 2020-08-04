import json
from django.test import TestCase, Client
from django.urls import reverse, resolve
from Empapp.models import Employee
from Empapp.views import EmployeeList, EmployeeDetail


class EmployeeViewsTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=[3]) #checking for /api/3->Works..
        e1=Employee(empid=3, name="Venkat", emp_num=200, department='CSE')
        e1.save()

    def test_view_insert(self):
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'insert')

    def test_view_employee_list(self):
        resolver = resolve('/api/employee/')
        self.assertEquals(resolver.func.cls, EmployeeList)

    def test_view_employee_detail(self):
        resolver = resolve('/api/2/')
        self.assertEquals(resolver.func.cls, EmployeeDetail)

    def test_employees_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_employee_list_POST(self):
        '''
        This method make sures that an employee is created with test data,
        And returns 201 status_code, after the creation is successfull.
        '''
        response = self.client.post(self.list_url, {
            'empid':4,
            'name':"Erana Gouda",
            'emp_num':400,
            'department':"MBA",
        })
        self.assertEquals(response.status_code, 201)

    def test_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)

    def test_detail_DELETE(self):
        response = self.client.delete(self.detail_url, json.dumps({'pk':3}))
        self.assertEquals(response.status_code, 204)
