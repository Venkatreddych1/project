from django.test import TestCase
from Empapp.models import Employee


class EmployeeModelsTestCase(TestCase):
    def setUp(self):
        '''Notice this is a method which wont reflect the changes in actual DB
           setUp method will be executed always before executing a test method..
        '''
        e1 = Employee(empid=2, name='Venkatesh', emp_num=100, department="ECE")
        e1.save()

    def test_employee_info(self):
        qs = Employee.objects.all()
        self.assertEquals(qs.count(),1)

    def test_employee_name(self):
        emp_name = Employee.objects.get(name='Venkatesh')
        self.assertEquals('Venkatesh',emp_name.name)

    def test_employee_department(self):
        emp_department = Employee.objects.get(department="ECE")
        self.assertEquals('ECE',emp_department.department)

    def test_employee_number(self):
        emp_number = Employee.objects.get(emp_num=100)
        self.assertEquals(100,emp_number.emp_num)
