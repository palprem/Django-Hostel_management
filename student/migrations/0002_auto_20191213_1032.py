# Generated by Django 2.2.7 on 2019-12-13 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hosteldetail',
            old_name='hostel_name',
            new_name='name',
        ),
    ]
