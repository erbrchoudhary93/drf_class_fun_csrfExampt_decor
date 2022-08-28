from django.urls import path,include
from .import views

urlpatterns = [
   
    path('studentapiclass/', views.StudentAPI.as_view()),
    path('studentapifun/', views.student_api),
]
