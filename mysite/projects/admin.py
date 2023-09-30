from django.contrib import admin
from .models import Project, Job, Invoice, Client, Employee
# Register your models here.
admin.site.register(Project)
admin.site.register(Job)
admin.site.register(Invoice)
admin.site.register(Client)
admin.site.register(Employee)