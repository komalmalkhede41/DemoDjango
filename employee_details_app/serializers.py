from rest_framework import serializers
from employee_details_app.models import EmployeeDetails

# EmployeeDetails Serializer
class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'
