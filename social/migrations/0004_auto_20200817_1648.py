# Generated by Django 3.1 on 2020-08-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20200817_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='pic',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='pic',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
