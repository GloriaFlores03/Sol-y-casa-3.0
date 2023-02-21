from django.contrib import admin
from django.shortcuts import render
from .models import Inmueble,Empleado,Cliente,Foto
from django.contrib.auth.models import Permission


admin.site.register(Permission)
admin.site.register(Inmueble)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Foto)

# Register your models here.
