# Generated by Django 4.1.7 on 2023-04-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_jobpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='expiry',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
