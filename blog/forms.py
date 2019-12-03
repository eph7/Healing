from django import forms
from .models import Post, Categoria, Formulario


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['categoria', 'estado', 'title', 'slug',
                  'descripcion', 'text', 'imagen', 'published_date']

        # widgets = {
        #     'published_date':forms.SelectDateWidget(years=range(2019-2030)),
        # }


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nombre', 'estado']


class FormularioForm(forms.ModelForm):

    class Meta:
        model = Formulario
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo electrónico',
                }
            ),
            'asunto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el asunto',
                }
            ),
            'mensaje': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su mensaje',
                    'style': 'height: 7em;',
                }
            ),
        }
