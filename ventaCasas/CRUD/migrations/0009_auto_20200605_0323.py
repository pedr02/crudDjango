# Generated by Django 3.0.6 on 2020-06-05 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0008_auto_20200605_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houses',
            name='sel',
        ),
        migrations.RemoveField(
            model_name='houses',
            name='status',
        ),
    ]
