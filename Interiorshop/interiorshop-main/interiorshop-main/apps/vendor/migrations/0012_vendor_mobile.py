# Generated by Django 3.0.14 on 2021-07-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0011_auto_20210719_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
    ]
