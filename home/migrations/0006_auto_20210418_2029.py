# Generated by Django 3.1.5 on 2021-04-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210418_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesinfo',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
