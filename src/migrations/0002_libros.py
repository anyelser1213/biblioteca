# Generated by Django 4.0.6 on 2022-07-12 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60, unique=True, verbose_name='Nombre')),
                ('autor', models.CharField(max_length=50, verbose_name='Autor')),
            ],
        ),
    ]