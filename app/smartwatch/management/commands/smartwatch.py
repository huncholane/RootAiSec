from django.core.management.base import BaseCommand
from django.core.management import call_command
from smartwatch.watch import watch_files, start_servers

class Command(BaseCommand):
    help = 'Starts the file watcher'

    def handle(self, *args, **options):
        self.stdout.write('Starting file watcher...')
        call_command('collectstatic', '--noinput')
        call_command('migrate')
        start_servers()
        watch_files()