# Generated by Django 3.2.5 on 2022-09-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220914_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
