# Generated by Django 2.0 on 2021-01-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='desc',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]
