# Generated by Django 4.1.7 on 2023-03-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0011_alter_createadmin__10thmark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createadmin',
            name='_10thmark',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='createadmin',
            name='_12thmark',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
