# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_variable_settings', '0002_auto_20150605_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setting',
            options={'permissions': (('change_system_settings', 'Can change system settings'),)},
        ),
    ]
