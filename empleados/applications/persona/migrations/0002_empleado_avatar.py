# Generated by Django 3.2.9 on 2021-12-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
