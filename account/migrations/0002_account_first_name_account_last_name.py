# Generated by Django 4.2.8 on 2023-12-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(default=1, max_length=30, verbose_name='first name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(default=1, max_length=30, verbose_name='last name'),
            preserve_default=False,
        ),
    ]
