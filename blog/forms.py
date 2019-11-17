from django import forms
from .models import Post,Categoria

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['categoria', 'estado','title','slug','descripcion','text','published_date']

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nombre', 'estado']
