from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
      class Meta:
          model = Employee
          fields = ['empid','emp_num','name', 'department']
          
