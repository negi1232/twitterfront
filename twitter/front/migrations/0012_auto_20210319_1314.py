# Generated by Django 3.1.7 on 2021-03-19 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0011_followlist_screenname'),
    ]

    operations = [
        migrations.AddField(
            model_name='followlist',
            name='follow_date',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='followlist',
            name='guid',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='followlist',
            name='screenname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterModelTable(
            name='followlist',
            table=None,
        ),
    ]
