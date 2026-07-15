import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a superuser from ADMIN_USERNAME / ADMIN_PASSWORD / ADMIN_EMAIL env vars"

    def handle(self, *args, **options):
        username = os.getenv("ADMIN_USERNAME", "admin")
        password = os.getenv("ADMIN_PASSWORD", "")
        email = os.getenv("ADMIN_EMAIL", "admin@edway.io")

        if not password:
            self.stdout.write(self.style.WARNING("ADMIN_PASSWORD not set — skipping admin creation"))
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email, "is_staff": True, "is_superuser": True},
        )
        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created"))
        else:
            user.email = email
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' password updated"))
