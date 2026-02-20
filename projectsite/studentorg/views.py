from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Organization, Student, College, Program

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

class OrganizationListView(ListView):
    model = Organization
    template_name = 'org_list.html'
    context_object_name = 'organization'
    paginate_by = 5

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'student'
    paginate_by = 5

class CollegeListView(ListView):
    model = College
    template_name = 'college_list.html'
    context_object_name = 'college'
    paginate_by = 5

class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'program'
    paginate_by = 5
