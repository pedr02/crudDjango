# Generated by Django 3.0.6 on 2020-06-05 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0004_auto_20200604_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='image',
            field=models.ImageField(default='static/images/housePics/none1.jpg', upload_to='static/images/housePics/'),
        ),
    ]
