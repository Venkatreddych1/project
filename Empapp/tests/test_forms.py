from django.test import TestCase
from Empapp.forms import EmployeeForm
from Empapp.models import Employee


class FormTestCase(TestCase):
    def test_valid_form(self):
        w = Employee.objects.create(empid=500, emp_num=1020, name='Ajayy', department='MPCC')
        data = {
                'empid': w.empid,
                'name': w.name,
                'department': w.department,
                'emp_num': w.emp_num,
                }
        form = EmployeeForm(data=data)
        self.assertTrue(form.is_valid)

    def test_invalid_form(self):
        w = Employee.objects.create(empid=20, emp_num=103,department='SPACE')
        data = {
                'empid': w.empid,
                'emp_num': w.emp_num,
                'department': w.department,
                }
        form = EmployeeForm(data=data)
        self.assertFalse(form.is_valid())
