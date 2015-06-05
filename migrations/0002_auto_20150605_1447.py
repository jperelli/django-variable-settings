# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def jsonify_strings(apps, schema_editor):
    # Wraps each setting 'value' in "
    Setting = app.get_mode('django_variable_settings', 'Settings')
    print "INFO: adding \" to all django_variable_settings values"
    for setting in Settings.objects.all():
        setting.value = '"' + setting.value + '"'
        setting.save


class Migration(migrations.Migration):

    dependencies = [
        ('django_variable_settings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(jsonify_strings),
    ]
