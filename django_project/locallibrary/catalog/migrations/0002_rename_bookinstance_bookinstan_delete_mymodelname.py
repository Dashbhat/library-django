# Generated by Django 5.0.1 on 2024-02-08 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookInstance',
            new_name='BookInstan',
        ),
        migrations.DeleteModel(
            name='MyModelName',
        ),
    ]