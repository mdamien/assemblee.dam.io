# Generated by Django 3.1.3 on 2020-11-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201129_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actelegislatif',
            name='id',
        ),
        migrations.AlterField(
            model_name='actelegislatif',
            name='uid',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
