# Generated by Django 5.0.6 on 2024-12-09 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_performancereview_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performancereview',
            name='manager',
        ),
    ]
