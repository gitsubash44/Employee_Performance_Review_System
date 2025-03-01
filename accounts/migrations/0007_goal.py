# Generated by Django 5.1.1 on 2024-11-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_customuser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('status', models.CharField(choices=[('in_progress', 'In Progress'), ('achieved', 'Achieved')], default='in_progress')),
                ('progress', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
