# Generated by Django 3.0.3 on 2020-06-18 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project1app', '0003_auto_20200618_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='email',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='project1app.Client'),
        ),
    ]