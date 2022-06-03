from django.urls import path
from . import views

urlpatterns = [
    path('new/',views.Add_Record),
    path('all/',views.Record_Details),
]