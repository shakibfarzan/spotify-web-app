# Generated by Django 4.1.3 on 2022-11-29 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_delete_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normaluser',
            name='id',
        ),
        migrations.RemoveField(
            model_name='superadmin',
            name='id',
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='auth_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='normal_user', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='superadmin',
            name='auth_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='super_admin', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
