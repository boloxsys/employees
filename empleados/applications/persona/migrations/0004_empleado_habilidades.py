# Generated by Django 3.2.9 on 2021-12-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]