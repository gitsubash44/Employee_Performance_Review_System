# Generated by Django 5.1.1 on 2024-12-12 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_performancereview_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performancereview',
            name='manager',
        ),
    ]
