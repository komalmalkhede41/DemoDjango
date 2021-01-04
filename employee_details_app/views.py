from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from employee_details_app.models import EmployeeDetails
from employee_details_app.serializers import EmployeeDetailsSerializer

# Create EmployeeDetails views.
class EmployeeDetailsCreateAPIView(CreateAPIView):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer
    authentication_classes = (TokenAuthentication,)

# List EmployeeDetails views.
class EmployeeDetailsListAPIView(ListAPIView):
    serializer_class = EmployeeDetailsSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = EmployeeDetails.objects.all()
            return queryset

# RetrieveUpdateDestroy EmployeeDetails views.
class EmployeeDetailsRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'employee_id'

    def perform_update(self, serializer):
        return super(EmployeeDetailsRetrieveAPIView, self).perform_update(serializer)

    def destroy(self, request, employee_id):
        EmployeeDetails.objects.filter(employee_id=employee_id).delete()
        return Response(EmployeeDetails.objects.filter(employee_id=employee_id).values())