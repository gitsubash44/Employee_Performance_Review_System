# Generated by Django 5.0.6 on 2024-11-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_performancereview'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='position',
            field=models.CharField(default='', max_length=50),
        ),
    ]
