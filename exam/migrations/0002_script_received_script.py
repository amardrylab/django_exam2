# Generated by Django 2.2.14 on 2020-07-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='received_script',
            field=models.BooleanField(default=False),
        ),
    ]
