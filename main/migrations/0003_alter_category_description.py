# Generated by Django 4.1.7 on 2023-02-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_author_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(default=models.TextField(default='description')),
        ),
    ]
