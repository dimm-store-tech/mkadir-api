# Generated by Django 4.2.6 on 2023-10-17 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0020_alter_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.URLField(blank=True, default=None, max_length=2000, null=True),
        ),
    ]
