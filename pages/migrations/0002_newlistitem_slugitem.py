# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newlistitem',
            name='slugitem',
            field=autoslug.fields.AutoSlugField(default=b'', populate_from=b'list_item', editable=False),
        ),
    ]
