# Generated by Django 4.2.7 on 2023-12-09 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='contact_notes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
