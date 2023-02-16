# Create your views here.
from rest_framework import status
from rest_framework.views import APIView # normal views can return api data
from rest_framework.response import Response # if code is fine it gives 200 response
from .models import Employees
from .serializers import EmployeeSerializer


class EmployeeList(APIView):
    serializer_class=EmployeeSerializer

    def get(self,request):
        employee1=Employees.objects.all() # emoloyee1 stores all the objects
        serializer = EmployeeSerializer(employee1,many= True) #take all objects and converts to json, many =true means there are many of them so here no need to return just one json object
        return Response(serializer.data) # every view function returns an http response and in this case its json

    def post(self,request):
        print(request.data)
        serializer = EmployeeSerializer(data = request.data)  # take all objects and converts to json, many =true means there are many of them so here no need to return just one json object
        '''if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  # every view function returns an http response and in this case its json
        '''
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "employee added", "status": 200, "data": serializer.data},
                        status=status.HTTP_200_OK)


    def put(self,request, emp_id=None):
        emp = Employees.objects.get(id=emp_id)
        serializer =EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "data edited", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        return Response({"message": "errors", "status": 400, "data": serializer.data},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, emp_id):
        try:
            emp = Employees.objects.get(id=emp_id)
            emp.delete()
            return Response({"message": "employee deleted", "status": 204, "data": {}},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": "error", "status": 204, "data": {}},status=status.HTTP_400_BAD_REQUEST)

