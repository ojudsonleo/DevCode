# Generated by Django 3.2.2 on 2021-05-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database', models.CharField(max_length=50)),
                ('database_upload', models.FileField(upload_to='')),
                ('write_data', models.TextField(blank=True)),
            ],
        ),
    ]
