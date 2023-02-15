from django.urls import path
from . import views

urlpatterns = [
   path('demo/',views.employeeList.as_view()),
   path('create/',views.employeeList.as_view())

]