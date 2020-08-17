# Generated by Django 3.1 on 2020-08-17 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followuser',
            name='followed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to='social.myprofile'),
        ),
        migrations.AlterField(
            model_name='followuser',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='social.myprofile'),
        ),
        migrations.AlterField(
            model_name='mypost',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.myprofile'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='commented_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.myprofile'),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='liked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.myprofile'),
        ),
    ]
