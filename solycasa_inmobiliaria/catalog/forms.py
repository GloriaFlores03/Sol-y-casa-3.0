from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Foto

class NewRegistroForm(UserCreationForm):
    nombre = forms.CharField(label='nombre',max_length=250,
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'nombre'}))
    apellido =forms.CharField(label='apellido',max_length=250,
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'apellido'}))
    email = forms.CharField(label='email',max_length=250,
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'email'}))
    telefono = forms.IntegerField(label='telefono',
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'telefono'}))
    direccion = forms.CharField(label='direccion',max_length=250,
                                widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'direccion'}))
    password1 = forms.CharField(label='contraseña', 
                                widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':'contraseña'}))
    password2 = forms.CharField(label='repetir contraseña', 
                                widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':'repetir contraseña'}))

class NewInmueble(forms.Form):

    precio = forms.IntegerField(label='precio',
                                widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'precio'}))

    ubicacion = forms.CharField(label='ubicacion',max_length=250,
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'ubicacion'}))
    
    m2 = forms.IntegerField(label='m2',
                                widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'m2'}))
    
    descripcion = forms.CharField(label='descripcion',max_length=500,
                                widget=forms.Textarea(attrs={'class':"form-control",'placeholder':'descripcion'}))
    
    compra = forms.BooleanField(label='compra',required=False,initial=False)

    ubicacion_maps = forms.CharField(label='ubicacion_maps',max_length=5000,
                                    widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':'ubicacion maps'}))



class EditPerfilForm(forms.Form):
    nombre = forms.CharField(label='nombre',max_length=250,
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'nombre'}))
    apellido =forms.CharField(label='apellido',max_length=250,
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'apellido'}))
    email = forms.CharField(label='email',max_length=250,
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'email'}))
    telefono = forms.IntegerField(label='telefono',
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'telefono'}))
    direccion = forms.CharField(label='direccion',max_length=250,
                                widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'direccion'}))
class HipotecaForm(forms.Form):
    saldo = forms.IntegerField(label='Saldo',
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'saldo'}))
    pago_mensual = forms.IntegerField(label='Pago mensual',
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'pago_mensual'}))
    pago_extra = forms.IntegerField(label='Pago extra',
                            widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'pago_extra'}))


class SubirFotoA(forms.ModelForm):
    class Meta:
        model= Foto
        fields=['id_inmueble','subir_foto_a']

class SubirFotoC(forms.ModelForm):
    class Meta:
        model= Foto
        fields=['id_inmueble','subir_foto_c']


