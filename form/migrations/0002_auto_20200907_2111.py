# Generated by Django 3.0.3 on 2020-09-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='replied_by',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='reply',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='secret_code',
            field=models.CharField(default='13c4989897', max_length=10),
        ),
    ]
