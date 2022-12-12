from django.urls import path
from . import views

urlpatterns = [
     path("create/", views.LoginCreate.as_view(), name="create"), #vista basada en clases
     path("datos/", views.DatosAlmacenar.as_view(), name="datos"), 
     path('', views.index, name='index'),
]