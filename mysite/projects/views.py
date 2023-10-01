from django.shortcuts import render
from django.views import generic
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ProjectListView(generic.ListView):
    model = Project
    template_name = "projects.html"
    context_object_name = 'projects'


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = "project.html"
    context_object_name = "project"


class UserProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "userprojects.html"
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(responsible=self.request.user)
