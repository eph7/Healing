# Generated by Django 2.2.6 on 2019-11-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(upload_to='imagenes/', verbose_name='Imagen'),
        ),
    ]