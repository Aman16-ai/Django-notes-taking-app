# Generated by Django 3.1.5 on 2021-04-18 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210418_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notesinfo',
            name='date',
        ),
    ]
