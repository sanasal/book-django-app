# Generated by Django 4.0.10 on 2023-02-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mystry_and_Police',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('img', models.ImageField(blank=True, default='', upload_to='')),
                ('auther', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
