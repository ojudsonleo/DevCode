# Generated by Django 3.2.2 on 2021-05-13 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='command',
            field=models.CharField(default=1233, max_length=60),
            preserve_default=False,
        ),
    ]
