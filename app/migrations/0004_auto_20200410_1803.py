# Generated by Django 2.0 on 2020-04-10 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_payment_session_levels'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('type_of_user', models.CharField(max_length=30, null=True)),
                ('national_id', models.IntegerField(null=True)),
                ('phonenumber', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60, null=True)),
                ('nearest_town', models.CharField(max_length=50)),
                ('level', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='phonenumber',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='session_levels',
            old_name='phonenumber',
            new_name='phone_number',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
