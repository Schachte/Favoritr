# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_newlistitem_slugitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newlist',
            name='list_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='newlist',
            unique_together=set([('user', 'list_name')]),
        ),
    ]
