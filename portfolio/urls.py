from django.urls import path
from .views import index, aboutMe, projects


urlpatterns = [
    path('', index, name = "home"),
    path('aboutMe', aboutMe, name = "aboutMe"),
    path('projects', projects, name = "projects"),
]