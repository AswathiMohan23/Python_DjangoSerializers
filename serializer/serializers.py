from rest_framework import serializers
from .models import employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
    #    fields = ('first_name','last_name')
        fields = '__all__' #displays all the feilds in employee model



