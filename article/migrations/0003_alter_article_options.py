# Generated by Django 5.2.1 on 2025-07-16 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'article', 'verbose_name_plural': 'article List'},
        ),
    ]
