# Generated by Django 3.2.8 on 2021-12-13 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0048_comentario_aprobado'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='nombre_comentador',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
