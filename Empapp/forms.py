from django import forms

class EmployeeForm(forms.Form):
      empid=forms.IntegerField(label="Enter empid")
      name=forms.CharField(label='Enter name',max_length=20)
      emp_num=forms.IntegerField(label='Enter Employeenum',max_value=10)
      department=forms.CharField(label='Enter Department')