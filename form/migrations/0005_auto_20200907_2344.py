# Generated by Django 3.0.3 on 2020-09-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20200907_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='secret_code_value',
            field=models.CharField(default='6416422474', max_length=10),
        ),
    ]