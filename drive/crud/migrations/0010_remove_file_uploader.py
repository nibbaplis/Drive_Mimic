# Generated by Django 2.2.2 on 2019-06-17 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_auto_20190617_0707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='uploader',
        ),
    ]