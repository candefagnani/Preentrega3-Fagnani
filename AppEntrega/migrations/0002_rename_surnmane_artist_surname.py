# Generated by Django 4.1.7 on 2023-04-01 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='surnmane',
            new_name='surname',
        ),
    ]