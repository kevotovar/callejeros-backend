# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 06:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='especie',
            old_name='id_expecie',
            new_name='id_especie',
        ),
    ]
