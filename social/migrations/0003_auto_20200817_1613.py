# Generated by Django 3.1 on 2020-08-17 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20200817_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.myprofile'),
        ),
    ]
