# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emaillistcreator', '0006_auto_20160430_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='docfile',
            field=models.FileField(upload_to='email_attachments'),
        ),
    ]