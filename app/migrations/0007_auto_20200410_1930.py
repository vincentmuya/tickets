# Generated by Django 2.0 on 2020-04-10 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200410_1923'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Transaction',
        ),
    ]
