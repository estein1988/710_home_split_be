# Generated by Django 3.1.2 on 2020-11-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_auto_20201106_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
