from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
# from django.views.generic import View
from .models import Post,Categoria
from .forms import PostForm,CategoriaForm


# Create your views here.

#Principales
def base(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'base.html',{'posts': posts})

def mantenedor(request):
     return render(request,'mantenedor.html')

#DetallePost
def detallePost(request,slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'blog/pagina/post.html', {'detalle_post':post})

def formulario(request):
    return render(request,'blog/pagina/formulario.html')

def nosotros(request):
    return render(request,'blog/pagina/nosotros.html')

#Catalogos
def cuello(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Cuello')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Cuello'),       
        ).distinct()

    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'blog/pagina/cuello.html',{'posts': posts})


#VistaPost
def vistaPost(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request, 'blog/post/vista_post.html',{'post_form':post_form})

def listaPost(request):
    queryset = request.GET.get("buscar")
    post_listar = Post.objects.filter(estado = True)
    if queryset:
        post_listar = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(id__icontains = queryset)
        ).distinct()
    return render(request, 'blog/post/lista_post.html',{'post_listar':post_listar})

def editarPost(request,id):
    post_form = None
    error = None
    try:
        post_editar = Post.objects.get(id = id)
        if request.method == 'GET':
            post_form = PostForm(instance= post_editar)
        else:
            post_form = PostForm(request.POST, instance= post_editar)
            if post_form.is_valid():
                post_form.save()
            return redirect('inicio')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'blog/post/vista_post.html',{'post_form':post_form,'error':error})

def eliminarPost(request,id):
    post_eliminar = Post.objects.get(id = id)
    if request.method == 'POST':
        post_eliminar.estado=False
        post_eliminar.save()
        return redirect('blog:lista_post')
    return render(request, 'blog/post/eliminar_post.html',{'post_eliminar':post_eliminar})

#VistaCategoria
def vistaCategoria(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        if categoria_form.is_valid():
            categoria_form.save()
            return redirect('inicio')
    else:
        categoria_form = CategoriaForm()
    return render(request, 'blog/categoria/vista_categoria.html',{'categoria_form':categoria_form})

def listaCategoria(request):
    queryset = request.GET.get("buscar")
    categoria_listar = Categoria.objects.filter(estado = True)
    if queryset:
        categoria_listar = Categoria.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(estado__icontains = queryset)
        ).distinct()
    return render(request, 'blog/categoria/lista_categoria.html',{'categoria_listar':categoria_listar})

def editarCategoria(request,id):
    categoria_form = None
    error = None
    try:
        categoria_editar = Categoria.objects.get(id = id)
        if request.method == 'GET':
            categoria_form = CategoriaForm(instance= categoria_editar)
        else:
            categoria_form = CategoriaForm(request.POST, instance= categoria_editar)
            if categoria_form.is_valid():
                categoria_form.save()
            return redirect('inicio')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'blog/categoria/vista_categoria.html',{'categoria_form':categoria_form,'error':error})

def eliminarCategoria(request,id):
    categoria_eliminar = Categoria.objects.get(id = id)
    if request.method == 'POST':
        categoria_eliminar.estado=False
        categoria_eliminar.save()
        return redirect('blog:lista_categoria')
    return render(request, 'blog/categoria/eliminar_categoria.html',{'categoria_eliminar':categoria_eliminar})