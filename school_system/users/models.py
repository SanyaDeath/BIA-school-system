from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class RoleUser(models.TextChoices):
    STUDENT = 'student'
    TEACHER = 'teacher'
    ADMIN = 'admin'


class User(AbstractUser):
    role = models.CharField(max_length=7,
                            choices=RoleUser.choices,
                            default=RoleUser.TEACHER)

    middle_name = models.CharField(blank=False, max_length=50,
                                   verbose_name='Отчество')
    birth_date = models.DateField(blank=False, null=True,
                                  verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя и студенты'

    @property
    def is_admin(self):
        return (self.role == RoleUser.ADMIN or self.is_superuser)

    @property
    def is_teacher(self):
        return (self.role == RoleUser.TEACHER or self.is_staff)

    def __str__(self):
        return '{} {} {}'.format(self.last_name,
                                 self.first_name,
                                 self.middle_name)


class Student(User):
    entry_year = models.IntegerField(blank=False, null=True,
                                     validators=[MinValueValidator(1900),
                                                 MaxValueValidator(2021)],
                                     verbose_name='Год поступления')
    klass = models.CharField(blank=False, max_length=3,
                             verbose_name='Класс учащегося')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return '{} {} {}'.format(self.last_name,
                                 self.first_name,
                                 self.middle_name)
