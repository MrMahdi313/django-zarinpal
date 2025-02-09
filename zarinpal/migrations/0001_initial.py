# Generated by Django 2.1.7 on 2019-04-12 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hashid_field.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('authority', models.CharField(blank=True, max_length=100, null=True)),
                ('ref_id', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('callback_url', models.CharField(max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=225, null=True)),
                ('last_name', models.CharField(blank=True, max_length=225, null=True)),
                ('email', models.CharField(blank=True, max_length=225, null=True)),
                ('mobile', models.CharField(blank=True, max_length=225, null=True)),
                ('order_number', hashid_field.field.HashidField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', blank=True, min_length=7, null=True)),
                ('address', models.CharField(blank=True, max_length=225, null=True)),
                ('country', models.CharField(blank=True, max_length=225, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=225, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('successful_payment_date_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=100)),
                ('failure_reason', models.CharField(blank=True, max_length=100, null=True)),
                ('simulation', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
