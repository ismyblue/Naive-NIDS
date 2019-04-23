# Generated by Django 2.0 on 2019-04-23 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=20)),
                ('role_desc', models.CharField(max_length=75)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('usr_id', models.AutoField(primary_key=True, serialize=False)),
                ('usr_login', models.CharField(max_length=25)),
                ('usr_pwd', models.CharField(max_length=32)),
                ('usr_name', models.CharField(max_length=75)),
                ('usr_enabled', models.IntegerField()),
                ('role_id', models.ForeignKey(db_column='role_id', on_delete=django.db.models.deletion.CASCADE, to='nids.Role')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
