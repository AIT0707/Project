# Generated by Django 5.0 on 2024-01-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='added_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='friends',
            name='added_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='added_date',
            field=models.DateField(null=True),
        ),
    ]
