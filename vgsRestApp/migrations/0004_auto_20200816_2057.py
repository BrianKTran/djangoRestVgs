# Generated by Django 3.1 on 2020-08-17 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vgsRestApp', '0003_auto_20200813_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcardinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='creditcardinfo',
            name='cc_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
