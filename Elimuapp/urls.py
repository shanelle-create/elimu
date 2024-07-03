
from django.contrib import admin
from django.urls import path
from Elimuapp import views

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('home', views.index,name="home"),
    path('gallery/', views.gallery,name="gallery"),
    path('table/', views.table,name="table"),
    path('form/', views.form,name="form"),
    path('login/', views.login,name="login"),
    path('registration/', views.registration,name="registration"),


]
