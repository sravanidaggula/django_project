# Generated by Django 4.1.2 on 2023-01-23 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_gateway_city_alter_gateway_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gateway',
            old_name='city',
            new_name='gateway_name',
        ),
        migrations.RenameField(
            model_name='gateway',
            old_name='name',
            new_name='servername',
        ),
    ]