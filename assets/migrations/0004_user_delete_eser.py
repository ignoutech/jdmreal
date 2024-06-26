# Generated by Django 4.1.7 on 2023-03-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_rename_user_eser'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('_type', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Eser',
        ),
    ]
