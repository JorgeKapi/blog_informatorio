# Generated by Django 3.2.8 on 2021-11-29 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_auto_20211129_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='actualizado_en',
            field=models.DateTimeField(auto_now=True),
        ),
    ]