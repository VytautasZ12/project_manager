from django.shortcuts import reverse
from django.views import generic
from .models import Project, Job, Invoice
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    template_name = 'project_form.html'
    fields = ['title', 'deadline', 'client', 'employees']
    success_url = "/userprojects/"

    def form_valid(self, form):
        form.instance.responsible = self.request.user
        form.save()
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Project
    template_name = "project_delete.html"
    context_object_name = "project"
    success_url = "/userprojects/"

    def test_func(self):
        return self.get_object().responsible == self.request.user


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Project
    template_name = 'project_form.html'
    fields = ['title', 'deadline', 'client', 'employees']
    success_url = "/userprojects/"

    def form_valid(self, form):
        form.instance.responsible = self.request.user
        form.save()
        return super().form_valid(form)

    def test_func(self):
        return self.get_object().responsible == self.request.user


class JobCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Job
    template_name = 'job_form.html'
    fields = ['title', 'info', 'price']

    def test_func(self):
        project = Project.objects.get(pk=self.kwargs['order_id'])
        return project.responsible == self.request.user

    def get_success_url(self):
        return reverse('project', kwargs={"pk": self.kwargs['order_id']})

    def form_valid(self, form):
        form.instance.project = Project.objects.get(pk=self.kwargs['order_id'])
        form.save()
        return super().form_valid(form)


class InvoiceCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Invoice
    template_name = 'invoice_form.html'
    fields = ['date']

    def test_func(self):
        project = Project.objects.get(pk=self.kwargs['order_id'])
        return project.responsible == self.request.user

    def get_success_url(self):
        return reverse('project', kwargs={"pk": self.kwargs['order_id']})

    def form_valid(self, form):
        form.instance.project = Project.objects.get(pk=self.kwargs['order_id'])
        form.save()
        return super().form_valid(form)


class InvoiceDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Invoice
    template_name = 'invoice.html'
    context_object_name = "invoice"

    def test_func(self):
        project = Project.objects.get(pk=self.kwargs['order_id'])
        return project.responsible == self.request.user
