# Generated by Django 4.1.7 on 2023-02-24 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='article',
            table='article',
        ),
        migrations.AlterModelTable(
            name='categoryarticle',
            table='category_article',
        ),
    ]
