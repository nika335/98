# Generated by Django 5.0.1 on 2024-04-04 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shearing_app', '0002_textshearing_urls_alter_textshearing_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='textshearing',
            name='title',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
