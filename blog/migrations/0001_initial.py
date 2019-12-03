# Generated by Django 2.2.6 on 2019-11-10 18:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria Activada/Categoria no Activada')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre ')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Nombre ')),
                ('correo', models.EmailField(max_length=200, verbose_name='Correo Electronico')),
                ('asunto', models.CharField(max_length=100, verbose_name='Asunto')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creacion')),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Fecha de Publicacion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
