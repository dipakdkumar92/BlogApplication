from django.contrib.auth.models import User
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('createsuperuser', interactive=False, username='admin', email='test@example.com')
        user = User.objects.get(username='admin')
        user.set_password('password')
        user.save()