# Generated by Django 3.1.5 on 2021-01-26 10:29

import api.functions
from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.functions.get_image_path)),
                ('preparation_time', models.PositiveIntegerField()),
                ('is_vegetarian', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('dishes', models.ManyToManyField(blank=True, related_name='menus', to='api.Dish')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
