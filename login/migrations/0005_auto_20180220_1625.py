# Generated by Django 2.0.1 on 2018-02-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20180220_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploaded_at',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
