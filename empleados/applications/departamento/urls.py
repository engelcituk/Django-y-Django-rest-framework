from django.contrib import admin
from django.urls import path

def desdeApps(self):
    print('==================desde la app departamento')


urlpatterns = [
    path('departamento/', desdeApps ),
]