# Generated by Django 4.1 on 2022-08-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.SlugField(error_messages={'unique': 'O usuario cadastrado já existe.'}, max_length=40, unique=True),
        ),
    ]
