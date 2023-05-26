#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import User


"""Create Superuser Instance"""
superuser=os.environ.get("SUPERUSER"),
superuser_email=os.environ.get("SUPERUSER_EMAIL"),
superuser_password=os.environ.get("SUPERUSER_PASSWORD"),

User.objects.create_superuser('superuser', 'superuser_email', 'superuser_password')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trevorkeoghphotography.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
