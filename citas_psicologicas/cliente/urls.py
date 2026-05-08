from django.urls import path
from .views import *

app_name = 'cliente'

urlpatterns = [
    # Página principal (mis citas)
    path('', mis_citas_option, name='mis_citas_option'),

    # Perfil
    path('perfil/', perfil_cliente, name='perfil_cliente'),

    # Editar perfil
    path('perfil/editar/', editar_perfil_cliente, name='editar_perfil_cliente'),
]