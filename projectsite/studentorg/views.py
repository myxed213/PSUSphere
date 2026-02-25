from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from studentorg.models import Organization, Student, College, Program
from .forms import OrganizationForm, StudentForm, CollegeForm, ProgramForm

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

class OrganizationListView(ListView):
    model = Organization
    template_name = 'org_list.html'
    context_object_name = 'organization'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Organization.objects.filter(Q(name__icontains=query) | Q(college__college_name__icontains=query) | Q(description__icontains=query))
        return Organization.objects.all()

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'record_delete.html'
    success_url = reverse_lazy('organization-list')

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'student'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(Q(lastname__icontains=query) | Q(firstname__icontains=query) | Q(student_id__icontains=query))
        return Student.objects.all()

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'record_delete.html'
    success_url = reverse_lazy('student-list')

class CollegeListView(ListView):
    model = College
    template_name = 'college_list.html'
    context_object_name = 'college'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return College.objects.filter(Q(college_name__icontains=query))
        return College.objects.all()

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'record_delete.html'
    success_url = reverse_lazy('college-list')

class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'program'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Program.objects.filter(Q(prog_name__icontains=query) | Q(college__college_name__icontains=query))
        return Program.objects.all()

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'record_delete.html'
    success_url = reverse_lazy('program-list')
