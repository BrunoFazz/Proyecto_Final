from django.contrib import admin
from django.urls import path , include
from django.contrib.auth.views import LogoutView
from core.views import inicio,agregar,editar,mostrar ,eliminar,acerca_de_mi

urlpatterns = [
    path('', inicio, name="index"),
    path('agregar/', agregar, name="agregar"),
    path('editar/<int:id_filial>/', editar, name="editar"),
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/<int:id_filial>/', eliminar, name="eliminar"),
    path('AboutMe', acerca_de_mi, name="AboutMe"),
]


#Basadas en Clase
