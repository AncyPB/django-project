# Generated by Django 3.0.3 on 2020-06-20 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project1app', '0011_auto_20200620_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Lemail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='project1app.Client'),
        ),
    ]
