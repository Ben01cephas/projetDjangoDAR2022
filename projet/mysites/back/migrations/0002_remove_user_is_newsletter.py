# Generated by Django 4.0.3 on 2022-03-02 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_newsletter',
        ),
    ]