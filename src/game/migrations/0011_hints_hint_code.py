# Generated by Django 4.0.1 on 2022-03-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_remove_hints_hint_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='hints',
            name='hint_code',
            field=models.IntegerField(default=None),
        ),
    ]