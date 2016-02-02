# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20160201_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='team', blank=True, to='base.Team', null=True),
        ),
    ]
