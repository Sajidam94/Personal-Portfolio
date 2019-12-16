# Generated by Django 3.0 on 2019-12-10 07:55

import core.models
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=196)),
                ('comments', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(blank=True, max_length=40, null=True)),
                ('duration', models.CharField(blank=True, max_length=9, null=True)),
                ('academy', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('profession', models.CharField(max_length=30)),
                ('contact_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField(verbose_name='Date of birth')),
                ('location', models.CharField(max_length=30)),
                ('summary', models.TextField()),
                ('facebook', models.CharField(max_length=50)),
                ('linkedin', models.CharField(max_length=50)),
                ('github', models.CharField(max_length=50)),
                ('banner_image', models.CharField(max_length=100)),
                ('profile_image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('source_code_link', models.CharField(blank=True, max_length=200, null=True)),
                ('live_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('progress', core.models.IntegerRangeField()),
            ],
        ),
    ]