# Generated by Django 2.2.6 on 2019-11-10 22:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191110_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Publicacion'),
        ),
    ]
