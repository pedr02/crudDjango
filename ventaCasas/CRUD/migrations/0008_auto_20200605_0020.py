# Generated by Django 3.0.6 on 2020-06-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0007_auto_20200604_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='image',
            field=models.ImageField(default='none1.jpg', upload_to=''),
        ),
    ]
