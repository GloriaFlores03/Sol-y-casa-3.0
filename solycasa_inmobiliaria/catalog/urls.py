from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('alquilar/',views.alquilar,name='alquilar'),
    path('comprar/',views.comprar,name='comprar'),
    path('registro/',views.registro,name='registro'),
    path('alquilar_details/<int:pk>',views.alquilar_details,name='alquilar_details'),
    path('login/',views.login,name="login"),
    path('new_inmueble/',views.new_inmueble,name="new_inmueble"),
    path('edit_inmueble/<int:pk>',views.edit_inmueble,name="edit_inmueble"),
    path('delete_inmueble/<int:pk>',views.delete_inmueble,name="delete_inmueble"),
    path('perfil_cliente',views.perfil_cliente,name='perfil_cliente'),
    path('edit_perfil_cliente/',views.edit_perfil_cliente,name='edit_perfil_cliente'),
    path('perfil_empleado',views.perfil_empleado,name='perfil_empleado'),
    path('edit_perfil_empleado/',views.edit_perfil_empleado,name='edit_perfil_empleado'),
    path('delete_perfil_cliente/',views.delete_perfil_cliente,name="delete_perfil_cliente"),
    path('delete_perfil_empleado/',views.delete_perfil_empleado,name="delete_perfil_empleado"),
    path('logout/',views.logout_view,name="logout"),
    path('comprar_details/<int:pk>',views.comprar_details,name='comprar_details'),
    path('subir_fotos_a/<int:pk>',views.subir_fotos_a,name='subir_fotos_a'),
    path('subir_fotos_c/<int:pk>',views.subir_fotos_c,name='subir_fotos_c'),
    path('alquilar_inmueble/<int:pk>/', views.alquilar_inmueble, name='alquilar_inmueble'),
    path('comprar_inmueble<int:pk>/',views.comprar_inmueble,name="comprar_inmueble"),


]

