# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0002_auto_20170227_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='id_usuario',
            new_name='rescatista',
        ),
    ]
