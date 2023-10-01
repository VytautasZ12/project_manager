from django.urls import path
from .views import (ProjectListView,
                    ProjectDetailView,
                    UserProjectListView,
                    ProjectCreateView)

urlpatterns = [
    path('', ProjectListView.as_view(), name="projects"),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name="project"),
    path('userprojects/', UserProjectListView.as_view(), name= "userprojects"),
    path('projects/create/', ProjectCreateView.as_view(), name="project_create"),
]