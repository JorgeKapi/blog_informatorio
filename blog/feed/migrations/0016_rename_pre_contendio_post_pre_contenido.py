# Generated by Django 3.2.8 on 2021-11-30 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0015_post_pre_contendio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pre_contendio',
            new_name='pre_contenido',
        ),
    ]
