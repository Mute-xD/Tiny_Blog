# Generated by Django 3.0.3 on 2020-08-01 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_log', '0003_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='isPublic',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='isPublic',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]