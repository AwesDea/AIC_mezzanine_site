# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import base.models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_auto_20160214_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='code',
            field=models.FileField(upload_to=base.models.team_code_directory_path, storage=django.core.files.storage.FileSystemStorage(), verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='compiled_code',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to=base.models.team_compiled_code_directory_path, null=True, verbose_name='compiled code', blank=True),
        ),
    ]
