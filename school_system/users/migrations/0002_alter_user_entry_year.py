# Generated by Django 4.0 on 2021-12-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='entry_year',
            field=models.PositiveIntegerField(null=True, verbose_name='Год поступления'),
        ),
    ]
