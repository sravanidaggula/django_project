# Generated by Django 4.1.2 on 2023-01-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_gateway_city_alter_gateway_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gateway',
            name='city',
            field=models.TextField(max_length=199),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='name',
            field=models.TextField(max_length=199),
        ),
    ]
