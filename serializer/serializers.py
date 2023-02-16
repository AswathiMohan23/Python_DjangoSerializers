from rest_framework import serializers
from .models import Employees


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id','first_name','last_name']
        #fields = '__all__' #displays all the feilds in employee model







