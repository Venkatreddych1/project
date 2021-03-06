"""projectemp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url

from Empapp import views

urlpatterns = [
    url(r'^$', views.insert, name='insert'),
    url('api/employee/',views.EmployeeList.as_view(),name="list"),
    url('api/(?P<pk>\d+)/', views.EmployeeDetail.as_view(), name="detail"),

    ]
