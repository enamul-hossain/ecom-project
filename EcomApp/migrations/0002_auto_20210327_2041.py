# Generated by Django 3.1.5 on 2021-03-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='twitter',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='setting',
            name='youtube',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
