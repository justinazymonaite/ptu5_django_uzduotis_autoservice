# Generated by Django 4.1.3 on 2022-11-18 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autoservice', '0009_alter_car_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ceated at')),
                ('content', models.TextField(max_length=2000, verbose_name='content')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='autoservice.order', verbose_name='order')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_reviews', to=settings.AUTH_USER_MODEL, verbose_name='reviewer')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]