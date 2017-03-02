# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 20:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0003_auto_20170228_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='rescatista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mascotas', to=settings.AUTH_USER_MODEL),
        ),
    ]
