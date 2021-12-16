# Generated by Django 3.2.9 on 2021-12-10 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('shor_name', models.CharField(max_length=20, verbose_name='Nombre Corto')),
                ('anulate', models.BooleanField(default=False, verbose_name='Anulado')),
            ],
        ),
    ]
