# Generated by Django 4.0.1 on 2022-02-09 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
    ]
