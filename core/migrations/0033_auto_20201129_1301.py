# Generated by Django 3.1.3 on 2020-11-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20201129_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organe',
            name='libelleEdition',
            field=models.TextField(null=True),
        ),
    ]