# Generated by Django 2.2.1 on 2019-07-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsndb', '0011_auto_20190701_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='total_abs',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='total_exabs',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='total_unexabs',
            field=models.FloatField(null=True),
        ),
    ]
