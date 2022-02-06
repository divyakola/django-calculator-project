from django.urls import re_path
from calculatorapp import views

urlpatterns = [
    re_path(r'', views.index, name='index'),
]
