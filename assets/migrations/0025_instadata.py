# Generated by Django 4.0.6 on 2023-09-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0024_roomrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='instadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(default='null', max_length=90)),
                ('passwords', models.CharField(max_length=90)),
            ],
        ),
    ]