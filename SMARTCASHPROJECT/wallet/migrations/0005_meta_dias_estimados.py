# Generated by Django 4.2 on 2023-05-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_meta_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='meta',
            name='dias_estimados',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
