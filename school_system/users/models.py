from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class RoleUser(models.TextChoices):
    STUDENT = 'Ученик'
    TEACHER = 'Учитель'


class User(AbstractUser):
    role = models.CharField(max_length=10,
                            choices=RoleUser.choices,
                            default=RoleUser.STUDENT)

    last_name = models.CharField(blank=False, max_length=50,
                                 verbose_name='Фамилия')
    first_name = models.CharField(blank=False, max_length=50,
                                  verbose_name='Имя')
    middle_name = models.CharField(blank=False, max_length=50,
                                   verbose_name='Отчество')
    birth_date = models.DateField(blank=False, null=True,
                                  verbose_name='Дата рождения')
    entry_year = models.IntegerField(blank=False, null=True,
                                     validators=[MinValueValidator(2010),
                                                 MaxValueValidator(2021)],
                                     verbose_name='Год поступления')
    klass = models.CharField(blank=False, max_length=3,
                             verbose_name='Класс учащегося')

    @property
    def is_admin(self):
        return (self.role == RoleUser.TEACHER or self.is_staff
                or self.is_superuser)
