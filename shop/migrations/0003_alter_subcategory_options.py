# Generated by Django 5.1.4 on 2025-01-12 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_subcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['name'], 'verbose_name': 'subcategory', 'verbose_name_plural': 'subcategories'},
        ),
    ]
