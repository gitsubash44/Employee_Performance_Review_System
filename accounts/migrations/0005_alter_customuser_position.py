# Generated by Django 5.0.6 on 2024-11-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='position',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
