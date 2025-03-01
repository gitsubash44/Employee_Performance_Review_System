# Generated by Django 5.0.6 on 2024-12-09 07:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_performancereview_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancereview',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_given', to=settings.AUTH_USER_MODEL),
        ),
    ]
