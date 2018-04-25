from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import Setting
import json

class Command(BaseCommand):
    help = 'Initializes variable settings with values found in settings'

    def add_arguments(self, parser):

        parser.add_argument('-r', '--reset',
            help='Delete all settings before initializing',
            dest='reset',
            action='store_true',
            default=False)

    def save_object(self, setting, value):
        setting.value = json.dumps(value)
        setting.save()

    def handle(self, *args, **options):

        self.stdout.write('Start initializing variable settings')

        if ( options['reset'] ):
            Setting.objects.all().delete()
            self.stdout.write('All variable settings deleted')

        for s in settings.VARIABLE_SETTINGS:
            if len (s) == 2: # If overwrite not set explicetely
                key, value, overwrite = s + [False]
            elif len (s) == 3:
                key, value, overwrite = s
            else:
                self.stdout.write('  ERROR: invalid format for {}'.format(s[0]))

            try:
                setting = Setting.objects.get(key = key)
                if overwrite:
                    try:
                        self.save_object(setting, value)
                        self.stdout.write("  SET  {} to '{}' [forced]".format(key, value))
                    except:
                        self.stdout.write("!ERROR {} to '{}' [forced]".format(key, value))
                        raise
                else:
                    self.stdout.write('  SKIP {}'.format(key))

            except Setting.DoesNotExist:
                setting = Setting(key = key)
                try:
                    self.save_object(setting, value)
                    self.stdout.write('  SET  {}'.format(key))
                except:
                    self.stdout.write("!ERROR {} to '{}'".format(key, value))
                    raise

        self.stdout.write('Finish initializing variable settings')
