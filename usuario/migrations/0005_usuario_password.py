# Generated by Django 4.1 on 2022-08-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_remove_usuario_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
