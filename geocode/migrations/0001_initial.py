# Generated by Django 3.1.2 on 2020-10-25 05:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtRisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=20)),
                ('risk_level', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='GPS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(19)])),
                ('close_contact', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.IntegerField(unique=True)),
            ],
        ),
    ]
