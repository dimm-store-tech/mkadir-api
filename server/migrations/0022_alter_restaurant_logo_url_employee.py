# Generated by Django 4.2.5 on 2023-10-23 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0021_alter_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='logo_url',
            field=models.URLField(blank=True, default=None, max_length=2000, null=True),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.restaurant')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
