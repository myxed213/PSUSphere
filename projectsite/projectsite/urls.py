from django.contrib import admin
from django.urls import path
from studentorg.views import (
    HomePageView, OrganizationListView, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    CollegeListView, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
    ProgramListView, ProgramCreateView, ProgramUpdateView, ProgramDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list/', OrganizationListView.as_view(), name='organization-list'),
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/edit/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/delete/<int:pk>/', OrganizationDeleteView.as_view(), name='organization-delete'),
    path('student_list/', StudentListView.as_view(), name='student-list'),
    path('student_list/add/', StudentCreateView.as_view(), name='student-add'),
    path('student_list/edit/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student_list/delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    path('college_list/', CollegeListView.as_view(), name='college-list'),
    path('college_list/add/', CollegeCreateView.as_view(), name='college-add'),
    path('college_list/edit/<int:pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('college_list/delete/<int:pk>/', CollegeDeleteView.as_view(), name='college-delete'),
    path('program_list/', ProgramListView.as_view(), name='program-list'),
    path('program_list/add/', ProgramCreateView.as_view(), name='program-add'),
    path('program_list/edit/<int:pk>/', ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/delete/<int:pk>/', ProgramDeleteView.as_view(), name='program-delete'),
]
