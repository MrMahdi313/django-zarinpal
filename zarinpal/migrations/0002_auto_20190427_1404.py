# Generated by Django 2.2 on 2019-04-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('zarinpal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='callback_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
