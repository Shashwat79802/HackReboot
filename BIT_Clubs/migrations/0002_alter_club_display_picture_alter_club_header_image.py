# Generated by Django 4.1.6 on 2023-02-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BIT_Clubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='display_picture',
            field=models.ImageField(upload_to='BIT_Clubs/static/media'),
        ),
        migrations.AlterField(
            model_name='club',
            name='header_image',
            field=models.ImageField(upload_to='BIT_Clubs/static/media'),
        ),
    ]
