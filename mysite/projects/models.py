from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=20)
    last_name = models.CharField(verbose_name="Last Name", max_length=20)
    company_name = models.CharField(verbose_name="Company Name", max_length=50)
    contacts = models.TextField(verbose_name="Contacts", max_length=2000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Employee(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=20)
    last_name = models.CharField(verbose_name="Last Name", max_length=20)
    position = models.TextField(verbose_name='Position', max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"

class Job(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    info = models.TextField(verbose_name="Information", max_length=2000, default="")
    price = models.DecimalField(verbose_name="Price", max_digits=5, decimal_places=2, null=True, blank=True)
    project = models.ForeignKey(to="Project", verbose_name="Project", on_delete=models.CASCADE, related_name="jobs")


class Invoice(models.Model):
    date = models.DateField(verbose_name="Date")
    project = models.ForeignKey(to="Project", verbose_name="Project", on_delete=models.CASCADE, related_name="invoices")

    def total(self):
        total = 0
        for job in self.project.jobs.all():
            total += job.price
        return total

class Project(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    start_date = models.DateTimeField(verbose_name="Start Date", auto_now_add=True)
    deadline = models.DateTimeField(verbose_name="Deadline")
    responsible = models.ForeignKey(to=User, verbose_name="Responsible", on_delete=models.SET_NULL, null=True,
                                    blank=True)
    client = models.ForeignKey(to="Client", verbose_name="Client", on_delete=models.SET_NULL, null=True, blank=True)
    employees = models.ManyToManyField(to="Employee", verbose_name="Employees")