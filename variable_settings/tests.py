from django.test import TestCase
from django.core.management import call_command
import variable_settings

class ManagementTest(TestCase):

    def test_variable_settings_initialize(self):
        with open('/dev/null', 'w') as f:  # avoids annoying output
            call_command('variable_settings_initialize', stdout=f)
        self.assertTrue(True)

    def test_set_and_get(self):
        variable_settings.set('evergreenstreet', 123)
        variable_settings.set('address.evergreenstreet', 123)
        variable_settings.set('address.evergreenavenue', 'first')

        self.assertEqual(variable_settings.get('evergreenstreet'), 123)
        self.assertEqual(variable_settings.get('address.evergreenavenue'), 'first')
        self.assertDictEqual(variable_settings.get('address.*'), {u'address.evergreenavenue': u'first', u'address.evergreenstreet': 123})
        self.assertDictEqual(variable_settings.all(), {u'address.evergreenavenue': u'first', u'evergreenstreet': 123, u'address.evergreenstreet': 123})
