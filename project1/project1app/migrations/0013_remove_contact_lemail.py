# Generated by Django 3.0.3 on 2020-06-20 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1app', '0012_contact_lemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='Lemail',
        ),
    ]
