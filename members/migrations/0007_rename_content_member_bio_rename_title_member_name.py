# Generated by Django 4.2.8 on 2023-12-12 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_member_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='content',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='title',
            new_name='name',
        ),
    ]
