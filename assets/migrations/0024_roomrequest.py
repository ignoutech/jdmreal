# Generated by Django 4.0.6 on 2023-05-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0023_show_places_product_id_alter_rooms_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='roomrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_uuid', models.CharField(default='null', max_length=90)),
                ('room_uuid', models.CharField(max_length=90)),
                ('note', models.CharField(max_length=300)),
                ('conversation_time', models.CharField(max_length=300)),
                ('client_name', models.CharField(max_length=30)),
                ('client_mobile_no', models.CharField(max_length=30)),
            ],
        ),
    ]