from django.contrib import admin
from .models import Post, Categoria, Formulario
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria


class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado',)
    resource_class = CategoriaResource


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'title']
    list_display = ('id', 'title', 'estado', 'created_date',)
    resource_class = PostResource


class FormularioResource(resources.ModelResource):
    class Meta:
        model = Formulario


class FormularioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'correo']
    list_display = ('asunto',)
    resource_class = FormularioResource


admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Formulario, FormularioAdmin)
