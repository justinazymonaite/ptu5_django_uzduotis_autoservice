# Generated by Django 4.1.3 on 2022-11-16 12:57

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0006_carmodel_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='summary',
            field=tinymce.models.HTMLField(default='-', max_length=1000, verbose_name='summary'),
        ),
    ]
