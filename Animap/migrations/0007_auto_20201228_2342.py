# Generated by Django 3.1.1 on 2020-12-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Animap', '0006_auto_20201228_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(to='Animap.Genre'),
        ),
    ]
