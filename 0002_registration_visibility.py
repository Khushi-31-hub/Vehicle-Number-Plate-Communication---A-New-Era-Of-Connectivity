# Generated by Django 5.0.3 on 2024-05-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_driver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='visibility',
            field=models.BooleanField(default=False),
        ),
    ]
