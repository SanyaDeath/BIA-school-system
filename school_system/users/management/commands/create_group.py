import logging

from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

GROUPS = ['teachers', 'students']
MODELS = ['Выражение', 'Студент']
PERMISSIONS = ['view', 'add', 'change', 'delete']


class Command(BaseCommand):
    help = 'creating group for teachers and students'

    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)

            for model in MODELS:
                for permission in PERMISSIONS:
                    name = 'Can {} {}'.format(permission, model)
                    print("Creating {}".format(name))
                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning("Perm not found '{}'.".format(name))
                        continue
                    new_group.permissions.add(model_add_perm)
        return
