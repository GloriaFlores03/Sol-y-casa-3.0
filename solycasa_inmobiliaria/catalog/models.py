from django.db import models

import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

# Create your models here.

class Inmueble(models.Model):
    precio = models.CharField(max_length=200)
    ubicacion  = models.CharField(max_length=200)
    m2 = models.IntegerField()
    hipoteca = models.CharField(max_length=200,null=True, blank=True)
    descripcion = models.TextField(max_length=500)
    compra = models.BooleanField(default=True)
    ubicacion_maps = models.CharField(max_length=5000,null=True)

    class Meta:
        ordering = ['ubicacion','precio', 'm2', 'hipoteca']  

    def get_google_maps_url(self):
        if self.ubicacion_maps:
            return self.ubicacion_maps
        else:
            if self.ubicacion:
                direccion = self.ubicacion.replace(' ', '+')
                return f'https://www.google.com/maps/embed/v1/place?q={direccion}'
            else:
                return None
            
    def get_absolute_url(self):
        return reverse('alquilar_details', args=[str(self.id)])

    def __str__(self):
        return f"{self.ubicacion}"
    
    
class Empleado(models.Model):
    id_user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True)
    telefono = models.IntegerField()
    direccion= models.CharField(max_length=250)

    class Meta:
        ordering = ['id_user']


    def get_absolute_url_a(self):
        return reverse('alquilar_inmueble', args=[str(self.id)])

    def get_absolute_url_c(self):
        return reverse('comprar_inmueble', args=[str(self.id)])    


    def __str__(self):
        return f"{self.id_user}"


class Cliente(models.Model):
    id_user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True)
    telefono = models.IntegerField()
    direccion= models.CharField(max_length=250)

    class Meta:
        ordering = ['id_user']

    
    def get_absolute_url_r(self):
        return reverse('registro', args=[str(self.id)])    
    
    def __str__(self):
        return f"{self.id_user}"
    

class Foto(models.Model):
    id_inmueble = models.ForeignKey('Inmueble', on_delete=models.SET_NULL,null=True)
    #id_inmueble = models.IntegerField(null=True)
    subir_foto_a= models.ImageField(upload_to="fotos_alquilar", null=True)
    subir_foto_c= models.ImageField(upload_to="fotos_compra", null=True)

    class Meta:
        ordering = ['id_inmueble']  

    def get_absolute_url(self):
        return reverse('foto', args=[str(self.id)])

    def __str__(self):
        return f"{self.id_inmueble}"


# Create your models here.
