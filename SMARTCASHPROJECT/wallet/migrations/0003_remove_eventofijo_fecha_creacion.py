# Generated by Django 4.2 on 2023-05-17 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_eventofijo_fecha_creacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventofijo',
            name='fecha_creacion',
        ),
    ]
