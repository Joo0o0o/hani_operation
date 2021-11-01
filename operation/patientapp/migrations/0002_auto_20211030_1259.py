# Generated by Django 3.2.6 on 2021-10-30 03:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['-updated_at', '-created_at']},
        ),
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='birthday',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_num',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='reg_num',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='slug',
            field=models.SlugField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterIndexTogether(
            name='patient',
            index_together={('id', 'slug')},
        ),
    ]
