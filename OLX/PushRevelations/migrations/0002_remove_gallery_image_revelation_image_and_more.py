# Generated by Django 4.2.5 on 2023-10-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PushRevelations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='image',
        ),
        migrations.AddField(
            model_name='revelation',
            name='image',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='revelation',
            name='image_2',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='revelation',
            name='image_3',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]