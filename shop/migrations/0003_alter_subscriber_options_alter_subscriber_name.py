# Generated by Django 4.0.5 on 2022-06-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_subscribe_subscriber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'MySubscriber', 'verbose_name_plural': 'A lot of Subscribers'},
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]