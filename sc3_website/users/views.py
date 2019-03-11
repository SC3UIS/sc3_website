from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Project
from .forms import ProjectCreateForm

class ProjectList(ListView):
    model = Project

class ProjectView(DetailView):
    model = Project

class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectCreateForm

    def get_success_url(self):
        return reverse_lazy('project_list')
    

