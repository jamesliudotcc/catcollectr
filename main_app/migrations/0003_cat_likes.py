# Generated by Django 2.1.7 on 2019-02-18 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cat_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
