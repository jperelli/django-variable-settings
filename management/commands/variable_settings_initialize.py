from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import Setting

class Command(BaseCommand):
    help = 'Initializes variable settings with values found in settings'

    def add_arguments(self, parser):

        parser.add_argument('-r', '--reset',
            help='Delete all settings before initializing',
            dest='reset',
            action='store_true',
            default=False)
    
    def handle(self, *args, **options):

        self.stdout.write('Start initializing variable settings')

        if ( options['reset'] ):
            Setting.objects.all().delete()
            self.stdout.write('All variable settings deleted')

        for s in settings.VARIABLE_SETTINGS:
            try:
                setting = Setting.objects.get(key = s[0])
                if len(s) >= 3 and s[2] == True:
                    setting.value = s[1]
                    setting.save()
                    self.stdout.write('set {} [forced]'.format(s[0]))
                else:
                    self.stdout.write('skip {}'.format(s[0]))
            except Setting.DoesNotExist:
                setting = Setting(key = s[0])
                setting.value = s[1]
                setting.save()
                self.stdout.write('set {}'.format(s[0]))

        self.stdout.write('Finish initializing variable settings')