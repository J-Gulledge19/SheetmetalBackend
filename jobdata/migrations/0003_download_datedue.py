# Generated by Django 4.2.1 on 2023-06-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobdata', '0002_alter_weight_dl'),
    ]

    operations = [
        migrations.AddField(
            model_name='download',
            name='dateDue',
            field=models.CharField(default=0.008695652173913044, max_length=10),
            preserve_default=False,
        ),
    ]
