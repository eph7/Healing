from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('mantenedor/',login_required(mantenedor), name= 'mantenedor'),
    path('formulario/', formulario, name='formulario'),
    path('nosotros/', nosotros, name='nosotros'),
    #post
    path('vista_post/', vistaPost, name='vista_post'),
    path('lista_post/', listaPost, name='lista_post'),
    path('editar_post/<int:id>', editarPost, name='editar_post'),
    path('eliminar_post/<int:id>', eliminarPost, name='eliminar_post'),
    #Categoria
    path('vista_categoria/', vistaCategoria, name='vista_categoria'),
    path('lista_categoria/', listaCategoria, name='lista_categoria'),
    path('editar_categoria/<int:id>', editarCategoria, name='editar_categoria'),
    path('eliminar_categoria/<int:id>', eliminarCategoria, name='eliminar_categoria'),
    #Catalogos
    path('catalogo/cuello/', cuello, name='cuello'),
    
    #Detalles
    path('<slug>/',detallePost, name='detalle_post'),
    


]

