# Generated by Django 4.2.5 on 2023-10-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0015_menu_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='isOpen',
            field=models.BooleanField(default=True),
        ),
    ]
