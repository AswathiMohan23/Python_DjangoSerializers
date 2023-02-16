from django.urls import path
from . import views

urlpatterns = [
   #path('demo/',views.EmployeeList.as_view()),
   path('employee/',views.EmployeeList.as_view(),name = 'employee'),
   path('employee/<int:emp_id>',views.EmployeeList.as_view(),name = 'employee')
]