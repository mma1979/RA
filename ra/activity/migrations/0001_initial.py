# Generated by Django 2.2.7 on 2019-11-17 16:33

import django.contrib.admin.models
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyActivity',
            fields=[
            ],
            options={
                'verbose_name': 'My Activity',
                'verbose_name_plural': 'My Activities',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('admin.logentry',),
            managers=[
                ('objects', django.contrib.admin.models.LogEntryManager()),
            ],
        ),
    ]
