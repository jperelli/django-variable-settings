#from django.test import TestCase
from unittest import TestCase  # use this to keep data in db

from django.core.management import call_command

class ManagementTest(TestCase):

    def test_variable_settings_initialize(self):
        with open('/dev/null', 'w') as f:  # avoids annoying output
            call_command('variable_settings_initialize', stdout=f)
