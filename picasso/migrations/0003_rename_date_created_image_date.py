# Generated by Django 4.0.4 on 2022-05-31 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picasso', '0002_rename_pin_category_rename_tags_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='date_created',
            new_name='date',
        ),
    ]
