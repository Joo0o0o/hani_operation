# Generated by Django 3.2.6 on 2021-10-31 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bedapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actingset',
            name='name',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]