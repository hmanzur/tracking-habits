# Generated by Django 3.0.4 on 2020-03-29 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='start_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
