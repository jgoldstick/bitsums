# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitSum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(db_index=True)),
                ('bitsum', models.PositiveIntegerField()),
                ('A', models.PositiveIntegerField()),
                ('B', models.PositiveIntegerField()),
                ('used', models.PositiveIntegerField(db_index=True)),
            ],
        ),
    ]
