# Generated by Django 4.1 on 2022-08-16 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_alter_usuario_email_alter_usuario_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
    ]
