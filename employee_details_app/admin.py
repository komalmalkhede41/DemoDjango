from django.contrib import admin
from employee_details_app.models import EmployeeDetails

# EmployeeDetails models.
@admin.register(EmployeeDetails)
class EmployeeDetails(admin.ModelAdmin):
    list_display = ('id','employee_id','first_name','last_name','email_id','mobile_number','country')