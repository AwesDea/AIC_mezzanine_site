# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0037_auto_20160317_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dockercontainer',
            name='dockerfile_src',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to=b'docker/dockerfiles', null=True, verbose_name='dockerfile source', blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='log_file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to=b'games/logs/', null=True, verbose_name='game log file', blank=True),
        ),
        migrations.AlterField(
            model_name='gameconfiguration',
            name='config',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to=game.models.game_config_directory_path, null=True, verbose_name='configuration file', blank=True),
        ),
    ]
