"""Create the site's admin login on deploy, if it doesn't exist yet.

Set these in Railway > service > Variables (never commit the password):
    DJANGO_SUPERUSER_PASSWORD   required; without it this command does nothing
    DJANGO_SUPERUSER_USERNAME   optional, default "admin"
    DJANGO_SUPERUSER_EMAIL      optional, default ceo@rpconsultant.online

Safe to run on every deploy: an existing user is left unchanged.
"""
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create the admin superuser from environment variables (skips if it already exists).'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'ceo@rpconsultant.online')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not password:
            self.stdout.write('create_superadmin: DJANGO_SUPERUSER_PASSWORD not set, skipping.')
            return

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            self.stdout.write(f'create_superadmin: user "{username}" already exists, skipping.')
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'create_superadmin: created superuser "{username}".'))
