# Generated by Django 3.0.5 on 2020-05-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links_app', '0002_auto_20200502_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='linksmodel',
            name='search',
            field=models.CharField(default='None', max_length=30),
        ),
    ]
