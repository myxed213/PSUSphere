"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from studentorg.views import (
    HomePageView, OrganizationListView, StudentListView, 
    CollegeListView, ProgramListView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list/', OrganizationListView.as_view(), name='organization-list'),
    path('student_list/', StudentListView.as_view(), name='student-list'),
    path('college_list/', CollegeListView.as_view(), name='college-list'),
    path('program_list/', ProgramListView.as_view(), name='program-list'),
]
