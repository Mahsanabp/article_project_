# Generated by Django 5.2.1 on 2025-07-16 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
