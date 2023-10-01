from django.contrib import admin
from .models import Project, Job, Invoice, Client, Employee


class JobsInline(admin.TabularInline):
    model = Job
    extra = 0

class InvoicesInline(admin.TabularInline):
    model = Invoice
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines =[JobsInline, InvoicesInline]

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Job)
admin.site.register(Invoice)
admin.site.register(Client)
admin.site.register(Employee)
