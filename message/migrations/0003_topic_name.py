# Generated by Django 2.2 on 2019-04-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]