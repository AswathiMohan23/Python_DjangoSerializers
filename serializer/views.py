from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView # normal views can return api data
from rest_framework.response import Response # if code is fine it gives 200 response
from .models import employees
from .serializers import EmployeeSerializer

class employeeList(APIView):
    serializer_class=EmployeeSerializer
    def get(self,request):
        employee1=employees.objects.all() # emoloyee1 stores all the objects
        serializer = EmployeeSerializer(employee1,many= True) #take all objects and converts to json, many =true means there are many of them so here no need to return just one json object
        return Response(serializer.data) # every view function returns an http response and in this case its json



