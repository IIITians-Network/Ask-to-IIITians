# Generated by Django 3.0.3 on 2020-09-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20200907_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='secret_code_value',
            field=models.CharField(max_length=10),
        ),
    ]
