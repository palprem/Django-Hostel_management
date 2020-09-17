from django.contrib import admin
from django.urls import path
from . import views
app_name='student'
urlpatterns = [
    path("index", views.index),
    path("besic", views.besic),
    path("add/", views.add),
    path("search/", views.search),
    path("hostel_details/", views.hostel_details),
    path("studentDetaile/", views.studentDetaile),
    path("show_Hdetaile/", views.show_Hdetaile),
    path("show_Sdetaile/", views.show_Sdetaile),
    path("vacant/", views.vacant),
    path("nmhVacant/", views.nmhVacant),
    path("nmhDetaile/", views.nmhDetaile),
    
    path("add_nmh/", views.add_nmh),
    path("NMH/", views.NMH),
    path("KMH/", views.KMH),
    
    path("login/", views.login),
    path("loginW/", views.loginW),
    path("loginA/", views.loginA),
    path("loginS/", views.loginS),
    path("delete/", views.delete),
]
