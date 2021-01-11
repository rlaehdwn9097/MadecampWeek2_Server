from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from restfulapi import views

urlpatterns = [
    path('contacts/', views.contacts),
    path('contacts/<int:pk>/', views.contact),
    path('admin/', admin.site.urls),
    path('contacts/get/', views.get),
    path('photos/', views.photos),
    path('photos/<int:id>/', views.deletephoto)
]
