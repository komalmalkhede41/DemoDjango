from django.db import models
from django_countries.fields import CountryField

# Create employeeDetails models.
class EmployeeDetails(models.Model):
    employee_id = models.CharField(max_length=16, editable=False, unique=True)
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    email_id = models.EmailField(max_length=256, null=True)
    mobile_number = models.CharField(max_length=10, null=True)
    country = CountryField(null=True)

    class Meta:
        db_table = 'employee_details'

    def save(self, **kwargs):
        super(EmployeeDetails, self).save(**kwargs)
        self.employee_id = 'ED%04d' % self.pk
        EmployeeDetails.objects.filter(pk=self.pk).update(employee_id=self.employee_id)
