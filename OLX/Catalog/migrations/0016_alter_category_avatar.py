# Generated by Django 4.2.5 on 2023-10-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0015_alter_category_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='avatar',
            field=models.ImageField(upload_to='images/'),
        ),
    ]