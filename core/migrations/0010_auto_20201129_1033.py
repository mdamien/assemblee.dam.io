# Generated by Django 3.1.3 on 2020-11-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='classification_famille_espece_code',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='classification_famille_espece_libelle',
            field=models.TextField(null=True),
        ),
    ]
