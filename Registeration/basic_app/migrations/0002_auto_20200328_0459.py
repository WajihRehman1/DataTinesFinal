# Generated by Django 3.0.4 on 2020-03-27 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='contact',
            field=models.BigIntegerField(default=1234, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='email',
            field=models.EmailField(default=234234123, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]