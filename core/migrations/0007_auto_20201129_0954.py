# Generated by Django 3.1.3 on 2020-11-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201129_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actelegislatif',
            name='libelleActe_libelleCourt',
            field=models.TextField(null=True),
        ),
    ]
