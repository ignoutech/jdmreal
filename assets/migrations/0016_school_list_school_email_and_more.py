# Generated by Django 4.1.7 on 2023-03-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0015_school_list_admin_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_list',
            name='school_email',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school_list',
            name='school_mobile_no',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
    ]