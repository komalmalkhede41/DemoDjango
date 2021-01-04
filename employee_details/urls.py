"""employee_details URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from employee_details_app.views import EmployeeDetailsCreateAPIView, EmployeeDetailsListAPIView, \
    EmployeeDetailsRetrieveAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^post/employee_details/$', EmployeeDetailsCreateAPIView.as_view()), # Create Job Position Master API
    url(r'^get/employee_details_list/$', EmployeeDetailsListAPIView.as_view()), # List Job Position Master API
    url(r'^get/employee_details/(?P<employee_id>[\w\-].+)/$', EmployeeDetailsRetrieveAPIView.as_view()) # Retrieve Job Position Master API

]
