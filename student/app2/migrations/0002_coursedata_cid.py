# Generated by Django 5.1 on 2024-08-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedata',
            name='cid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
