# Generated by Django 2.0 on 2020-04-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mpesacallbacks_mpesacalls_mpesapayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.IntegerField(null=True)),
                ('amount', models.IntegerField(null=True)),
                ('phonenumber', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='session_levels',
            fields=[
                ('session_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('phonenumber', models.CharField(max_length=25, null=True)),
                ('level', models.IntegerField(null=True)),
            ],
        ),
    ]