from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import View
from .models import Post, Categoria
from .forms import PostForm, CategoriaForm, FormularioForm
from django.contrib.auth.decorators import login_required, permission_required
# from django.contrib.auth.forms import UserCreationForm


# Create your views here.

# Principales
def base(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True)
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'base.html', {'posts': posts})


def mantenedor(request):
    return render(request, 'mantenedor.html')

# DetallePost


def detallePost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/pagina/post.html', {'detalle_post': post})

# def singup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('inicio')
#     else:
#          form = UserCreationForm()
#     return render(request, 'singup.html', {
#         'form':form
#     })


class FormularioContacto(View):
    def get(self, request, *args, **kwargs):
        form = FormularioForm()
        contexto = {
            'form': form,
        }
        return render(request, 'blog/pagina/formulario.html', contexto)

    def post(self, request, *args, **kwargs):
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        else:
            contexto = {
                'form': form,
            }
            return render(request, 'blog/pagina/formulario.html', contexto)


def nosotros(request):
    return render(request, 'blog/pagina/nosotros.html')

# Catalogos


def cuelloColumna(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Cuello y Columna')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Cuello y Columna'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/pagina/cuelloColumna.html', {'posts': posts})


def rodilla(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Rodilla')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Rodilla'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/pagina/rodilla.html', {'posts': posts})


def torax(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Torax')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Torax'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/pagina/torax.html', {'posts': posts})


def columna(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Columna')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Columna'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/pagina/columna.html', {'posts': posts})


def hombroCodo(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Hombro y Codo')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Hombro y Codo'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/pagina/hombroCodo.html', {'posts': posts})


def manoMuñeca(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Mano y Muñeca')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Mano y Muñeca'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/pagina/manoMuñeca.html', {'posts': posts})


def cadera(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Cadera')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Cadera'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/pagina/cadera.html', {'posts': posts})


def tobilloPie(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Tobillo y Pie')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Tobillo y Pie'),
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/pagina/tobilloPie.html', {'posts': posts})

# VistaPost


def vistaPost(request):
    user = request.user
    if user.has_perm('blog.profesor'):

        if request.method == 'POST':
            post_form = PostForm(request.POST, files=request.FILES)
            if post_form.is_valid():
                post_form.save()
                return redirect('inicio')
        else:
            post_form = PostForm()
        return render(request, 'blog/post/vista_post.html', {'post_form': post_form})
    else:
        return render(request, 'mantenedor.html')


def listaPost(request):
    queryset = request.GET.get("buscar")
    post_listar = Post.objects.filter(estado=True)
    if queryset:
        post_listar = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(id__icontains=queryset)
        ).distinct()
    return render(request, 'blog/post/lista_post.html', {'post_listar': post_listar})


def editarPost(request, id):
    user = request.user
    if user.has_perm('blog.profesor'):
        post_form = None
        error = None
        try:
            post_editar = Post.objects.get(id=id)
            if request.method == 'GET':
                post_form = PostForm(instance=post_editar)
            else:
                post_form = PostForm(
                    request.POST, instance=post_editar, files=request.FILES)
                if post_form.is_valid():
                    post_form.save()
                return redirect('inicio')
        except ObjectDoesNotExist as e:
            error = e

        return render(request, 'blog/post/vista_post.html', {'post_form': post_form, 'error': error})
    else:
        return render(request, 'mantenedor.html')


def eliminarPost(request, id):
    user = request.user
    if user.has_perm('blog.profesor'):
        post_eliminar = Post.objects.get(id=id)
        if request.method == 'POST':
            post_eliminar.estado = False
            post_eliminar.save()
            return redirect('blog:lista_post')
        return render(request, 'blog/post/eliminar_post.html', {'post_eliminar': post_eliminar})
    else:
        return render(request, 'mantenedor.html')

# VistaCategoria


def vistaCategoria(request):
    user = request.user
    if user.has_perm('blog.profesor'):
        if request.method == 'POST':
            categoria_form = CategoriaForm(request.POST)
            if categoria_form.is_valid():
                categoria_form.save()
                return redirect('inicio')
        else:
            categoria_form = CategoriaForm()
        return render(request, 'blog/categoria/vista_categoria.html', {'categoria_form': categoria_form})
    else:
        return render(request, 'mantenedor.html')


def listaCategoria(request):
    queryset = request.GET.get("buscar")
    categoria_listar = Categoria.objects.filter(estado=True)
    if queryset:
        categoria_listar = Categoria.objects.filter(
            Q(nombre__icontains=queryset) |
            Q(estado__icontains=queryset)
        ).distinct()
    return render(request, 'blog/categoria/lista_categoria.html', {'categoria_listar': categoria_listar})


def editarCategoria(request, id):
    user = request.user
    if user.has_perm('blog.profesor'):
        categoria_form = None
        error = None
        try:
            categoria_editar = Categoria.objects.get(id=id)
            if request.method == 'GET':
                categoria_form = CategoriaForm(instance=categoria_editar)
            else:
                categoria_form = CategoriaForm(
                    request.POST, instance=categoria_editar)
                if categoria_form.is_valid():
                    categoria_form.save()
                return redirect('inicio')
        except ObjectDoesNotExist as e:
            error = e

        return render(request, 'blog/categoria/vista_categoria.html', {'categoria_form': categoria_form, 'error': error})
    else:
        return render(request, 'mantenedor.html')


def eliminarCategoria(request, id):
    user = request.user
    if user.has_perm('blog.profesor'):
        categoria_eliminar = Categoria.objects.get(id=id)
        if request.method == 'POST':
            categoria_eliminar.estado = False
            categoria_eliminar.save()
            return redirect('blog:lista_categoria')
        return render(request, 'blog/categoria/eliminar_categoria.html', {'categoria_eliminar': categoria_eliminar})
    else:
        return render(request, 'mantenedor.html')
