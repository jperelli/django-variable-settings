from django.db import models

class Setting(models.Model):
    key   = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __unicode__(self):
    	return '{{"{}": "{}"}}'.format(self.key, self.value)