# Generated by Django 4.1.3 on 2022-11-16 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autoservice', '0004_car_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='due_back',
            field=models.DateField(blank=True, null=True, verbose_name='due back'),
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
    ]
