# Generated by Django 2.2.6 on 2020-05-29 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20200530_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='secret_id',
            field=models.CharField(max_length=255),
        ),
    ]
