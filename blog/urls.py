from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [

    path('formulario/', FormularioContacto.as_view(), name='formulario'),
    path('nosotros/', nosotros, name='nosotros'),
    # post
    path('vista_post/', login_required(vistaPost), name='vista_post'),
    path('lista_post/', login_required(listaPost), name='lista_post'),
    path('editar_post/<int:id>', login_required(editarPost), name='editar_post'),
    path('eliminar_post/<int:id>',
         login_required(eliminarPost), name='eliminar_post'),
    # Categoria
    path('vista_categoria/', login_required(vistaCategoria), name='vista_categoria'),
    path('lista_categoria/', login_required(listaCategoria), name='lista_categoria'),
    path('editar_categoria/<int:id>',
         login_required(editarCategoria), name='editar_categoria'),
    path('eliminar_categoria/<int:id>',
         login_required(eliminarCategoria), name='eliminar_categoria'),
    # Catalogos
    path('catalogo/cuelloColumna/', cuelloColumna, name='cuelloColumna'),
    path('catalogo/rodilla/', rodilla, name='rodilla'),
    path('catalogo/torax/', torax, name='torax'),
    path('catalogo/columna/', columna, name='columna'),
    path('catalogo/hombroCodo/', hombroCodo, name='hombroCodo'),
    path('catalogo/manoMuñeca/', manoMuñeca, name='manoMuñeca'),
    path('catalogo/cadera/', cadera, name='cadera'),
    path('catalogo/tobilloPie/', tobilloPie, name='tobilloPie'),
    # Detalles
    path('<slug>/', detallePost, name='detalle_post'),



]
