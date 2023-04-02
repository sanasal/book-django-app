# Generated by Django 4.0.10 on 2023-03-07 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_shell', '0006_islam_pdf_file_languages_pdf_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloadlanguagesitem',
            name='languages_item',
        ),
        migrations.RemoveField(
            model_name='downloadlanguagesitem',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='downloadmystry_and_policeitem',
            name='mystry_item',
        ),
        migrations.RemoveField(
            model_name='downloadmystry_and_policeitem',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='downloadprogrammingitem',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='downloadprogrammingitem',
            name='programming_item',
        ),
        migrations.RemoveField(
            model_name='downloadpsychologyitem',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='downloadpsychologyitem',
            name='psychology_item',
        ),
        migrations.RemoveField(
            model_name='downloadsciencesitem',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='downloadsciencesitem',
            name='sciences_item',
        ),
        migrations.DeleteModel(
            name='DownloadIslamItem',
        ),
        migrations.DeleteModel(
            name='DownloadLanguagesItem',
        ),
        migrations.DeleteModel(
            name='DownloadMystry_and_PoliceItem',
        ),
        migrations.DeleteModel(
            name='DownloadProgrammingItem',
        ),
        migrations.DeleteModel(
            name='DownloadPsychologyItem',
        ),
        migrations.DeleteModel(
            name='DownloadSciencesItem',
        ),
    ]
