# Generated by Django 3.1.3 on 2020-11-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20201129_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mandat',
            name='dateFin',
            field=models.TextField(null=True),
        ),
    ]
