# Generated by Django 3.2.3 on 2021-05-13 15:04

from django.db import migrations, models
import otherapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('otherapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Json',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.JSONField(default=otherapp.models.Default, verbose_name='Json')),
            ],
        ),
    ]
