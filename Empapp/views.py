from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
from django.http import HttpResponse,Http404
from rest_framework.views import APIView
from .Serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import views



def insert(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            p1=Employee(empid=form.cleaned_data['empid'],name=form.cleaned_data['name'],emp_num=form.cleaned_data['emp_num'],department=form.cleaned_data['department'])
            p1.save()
            return HttpResponse("data inserted successfully")
    else:
        form = EmployeeForm()
    return render(request,'input.html',{'form': form})




class EmployeeList(APIView):
      def get_object(self, pk):
          try:
             return Employee.objects.get(pk=pk)
          except Employee.DoesNotExist:
               raise Http404

      def get(self, request, pk, format=None):
          Employees = self.get_object(pk)
          Serializers = EmployeeSerializer(Employees)
          return Response(Serializers.data)

      def delete(self,request,pk):
          event1= self.get_object(pk)
          event1.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)


class Employeecreate(APIView):
      def get(self, request, format=None):
          snippets = Employee.objects.all()
          serializer = EmployeeSerializer(snippets, many=True)
          return Response(serializer.data)

      def post(self, request, format=None):
          serializer = EmployeeSerializer(data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
