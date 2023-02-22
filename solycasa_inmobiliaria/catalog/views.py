from multiprocessing import context
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from catalog.forms import NewInmueble, NewRegistroForm, EditPerfilForm, SubirFotoA,SubirFotoC,HipotecaForm
from .models import Cliente,Inmueble, Foto, Inmueble, Empleado
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render (request,"index.html")

def alquilar(request):
    alquilar_list = Inmueble.objects.all().filter(compra=0)
    context={
        'alquilar_list':alquilar_list,     
    }
    return render (request, "alquilar.html", context=context)
    
def alquilar_details(request,pk):
    alquilar_details = Inmueble.objects.get(pk=pk)
    foto_list = Foto.objects.filter(id_inmueble=pk)
    if request.method == 'POST':
            request.session['inmueble_alquilado'] = alquilar_details.id

    context={
        'alquilar_details':alquilar_details,
        'foto_list':foto_list,
    }
    return render (request, "alquilar_details.html", context=context)

def comprar(request):
    comprar_list = Inmueble.objects.all().filter(compra=1)
    context={
        'comprar_list':comprar_list,    
    }
    return render (request, "comprar.html", context=context)

def comprar_details(request,pk):
    comprar_details = Inmueble.objects.get(pk=pk)
    foto_list = Foto.objects.filter(id_inmueble=pk)
    if request.method == 'POST':
            request.session['inmueble_comprado'] = comprar_details.id

    context={
        'comprar_details':comprar_details,
        'foto_list':foto_list,
    }
    return render (request, "comprar_details.html", context=context)

def registro(request):
    message = 0
    if request.method == 'POST':
        form = NewRegistroForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()

                cliente = Cliente.objects.create(
                    id_user=user,
                    telefono=form.cleaned_data['telefono'],
                    direccion=form.cleaned_data['direccion']
                    )
                cliente.id_user.first_name=form.cleaned_data['nombre']
                cliente.id_user.last_name=form.cleaned_data['apellido']
                cliente.id_user.email=form.cleaned_data['email']
                cliente.id_user.save()

                message = 1
                form = NewRegistroForm()
                return redirect('index')
            except:
                    message = 3
        else:
            message = 2
    else:
        form = NewRegistroForm()

    context = {
        'form':form,
        'message':message,}

    return render(request, "registro.html", context=context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    context={
        'form':form,
    }
    return render(request, 'login.html',context=context)


@login_required
#@permission_required("Can add inmueble")
def new_inmueble(request):
    message=0
    if request.method=='POST':
        form = NewInmueble(request.POST)
        if form.is_valid():
            try:
                inmueble= Inmueble()
                inmueble.precio = form.cleaned_data["precio"]
                inmueble.ubicacion = form.cleaned_data["ubicacion"]
                inmueble.m2 = form.cleaned_data["m2"]
                inmueble.descripcion = form.cleaned_data["descripcion"]
                inmueble.compra = form.cleaned_data["compra"]
                inmueble. ubicacion_maps = form.cleaned_data["ubicacion_maps"]
                inmueble.save()
                message = 1
                form=NewInmueble()
            except:
                message=3
        else:
            message=2
    else:
        form= NewInmueble()

    context = {
        'form':form,
        'message':message,
    }

    return render(request,"new_inmueble.html",context=context)

@login_required
#@permission_required("Permisos_Empleados",'permiso 3')
def delete_inmueble(request,pk):
    delete_inmueble=Inmueble.objects.get(pk=pk)
    delete_inmueble.delete()
    return redirect('/catalog/alquilar/')

@login_required
#@permission_required("Permisos_Empleados",'permiso 1')
def edit_inmueble(request,pk):
    edit_inmueble = Inmueble.objects.get(pk=pk)
    sent=False
    if request.method =='POST':
        form = NewInmueble(request.POST)
        if form.is_valid():
            sent = True
            edit_inmueble.precio = form.cleaned_data["precio"]
            edit_inmueble.ubicacion = form.cleaned_data["ubicacion"]
            edit_inmueble.m2 = form.cleaned_data["m2"]
            edit_inmueble.descripcion = form.cleaned_data["descripcion"]
            edit_inmueble.compra = form.cleaned_data["compra"]
            edit_inmueble. ubicacion_maps = form.cleaned_data["ubicacion_maps"]
            edit_inmueble.save()
            form = NewInmueble()
    else:
        form = NewInmueble(initial={
            'precio': edit_inmueble.precio,
            'ubicacion': edit_inmueble.ubicacion,
            'm2': edit_inmueble.m2,
            'descripcion': edit_inmueble.descripcion,
            'compra': edit_inmueble.compra,
            'ubicacion_maps': edit_inmueble.ubicacion_maps,
        })


    context ={
        'sent':sent,
        'form':form,
        'edit_inmueble':edit_inmueble,
    }

    return render(request,'edit_inmueble.html',context=context)



@login_required
def perfil_cliente(request):
    if request.user.is_authenticated:
        user = request.user
        cliente = Cliente.objects.get(id_user=user)
        inmueble_alquilado = request.session.get('inmueble_alquilado', None)
        if inmueble_alquilado:
            inmueble_a = Inmueble.objects.get(pk=inmueble_alquilado)
            alquilado = True
        else:
            alquilado = False
            inmueble_a = None

        inmueble_comprado = request.session.get('inmueble_comprado', None)
        if inmueble_comprado:
            inmueble_c = Inmueble.objects.get(pk=inmueble_comprado)
            comprado = True
        else:
            comprado = False
            inmueble_c = None


    context={
        'cliente':cliente,
        'alquilado':alquilado,
        'inmueble':inmueble_a,
        'comprado':comprado,
        'inmueble_comprado':inmueble_c,
    }

    return render(request,"perfil_cliente.html",context=context)

@login_required
def edit_perfil_cliente(request):
    message = 0
    user = request.user
    if request.method == 'POST':
        form = EditPerfilForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['nombre']
            user.last_name = form.cleaned_data['apellido']
            user.email = form.cleaned_data['email']
            user.save()

            cliente.created = Cliente.objects.get_or_create(id_user=user)
            cliente.telefono = form.cleaned_data['telefono']
            cliente.direccion = form.cleaned_data['direccion']
            cliente.save()

            message = 1
    else:
        initial_data = {
            'nombre': user.first_name,
            'apellido': user.last_name,
            'email': user.email,
        }
        cliente = Cliente.objects.filter(id_user=user).first()
        if cliente:
            initial_data['telefono'] = cliente.telefono
            initial_data['direccion'] = cliente.direccion
        form = EditPerfilForm(initial=initial_data)
        
        
    context = {
        'form': form,
        'message': message,
    }
    
    return render(request, "edit_perfil_cliente.html", context=context)


@login_required
def perfil_empleado(request):
    if request.user.is_authenticated:
        user = request.user
        empleado = Empleado.objects.get(id_user=user)

    context={
        'empleado':empleado,
    }
    return render(request,"perfil_empleado.html",context=context)

@login_required
def edit_perfil_empleado(request):
    message = 0
    user = request.user
    if request.method == 'POST':
        form = EditPerfilForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['nombre']
            user.last_name = form.cleaned_data['apellido']
            user.email = form.cleaned_data['email']
            user.save()

            empleado.created = Empleado.objects.get_or_create(id_user=user)
            empleado.telefono = form.cleaned_data['telefono']
            empleado.direccion = form.cleaned_data['direccion']
            empleado.save()

            message = 1
    else:
        initial_data = {
            'nombre': user.first_name,
            'apellido': user.last_name,
            'email': user.email,
        }
        empleado = Empleado.objects.filter(id_user=user).first()
        if empleado:
            initial_data['telefono'] = empleado.telefono
            initial_data['direccion'] = empleado.direccion
        form = EditPerfilForm(initial=initial_data)
        
        
    context = {
        'form': form,
        'message': message,
    }
    
    return render(request, "edit_perfil_empleado.html", context=context)


@login_required
def delete_perfil_cliente(request):
    user = request.user
    delete_cliente = Cliente.objects.get(id_user=user)
    delete_cliente.delete()
    user.delete()
    return redirect('index')

@login_required
def delete_perfil_empleado(request):
    user = request.user
    delete_empleado = Empleado.objects.get(id_user=user)
    delete_empleado.delete()
    user.delete()
    return redirect('index')


@login_required
#@permission_required("catalog.can_create")    ESSS ASIII
#@permission_required("Permisos_Empleados",'permiso 2')
def subir_fotos_a(request,pk):
    message = ""
    if request.method=='POST':
        form  = SubirFotoA(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            message=1
    else:
        form = SubirFotoA()
    
    context = {
        'message':message,
        'form':form,
    }
    return render(request, 'subir_fotos_a.html',context)


@login_required
#@permission_required("Permisos_Empleados",'permiso 2')
def subir_fotos_c(request,pk):
    message = ""
    if request.method=='POST':
        form  = SubirFotoC(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            message=1
    else:
        form = SubirFotoC()
    
    context = {
        'message':message,
        'form':form,
    }
    return render(request, 'subir_fotos_c.html',context)
                    
def alquilar_inmueble(request, pk):
    if request.method == 'POST':
        inmueble = Inmueble.objects.get(pk=pk)
        request.session['inmueble_alquilado'] = inmueble.id
        return redirect('perfil_cliente')
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])

def comprar_inmueble(request, pk):
    if request.method == 'POST':
        inmueble = Inmueble.objects.get(pk=pk)
        request.session['inmueble_comprado'] = inmueble.id
        return redirect('perfil_cliente')
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])



def hipoteca(request):
    message=0
    if request.method=='POST':
        form = HipotecaForm(request.POST)
        if form.is_valid():
  
            form.saldo = form.cleaned_data['saldo']
            form.pago_mensual = form.cleaned_data['pago_mensual']
            form.pago_extra = form.cleaned_data['pago_extra']
            form.save()
            message = 1
            form=HipotecaForm()

        else:
            message=2
    else:
        form= HipotecaForm()

    context = {
        'form':form,
        'message':message,
    }

    return render(request,"comprar_details.html",context=context)
