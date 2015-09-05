from django.db import models


class Setting(models.Model):
    key   = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return '{{"{}": "{}"}}'.format(self.key, self.value)

    class Meta(object):
        app_label = 'django_variable_settings'
        permissions = (
            ("change_system_settings", "Can change system settings"),
        )
