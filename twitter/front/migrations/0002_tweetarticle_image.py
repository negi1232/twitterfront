# Generated by Django 3.1.7 on 2021-03-10 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetarticle',
            name='image',
            field=models.ImageField(default=999, upload_to='images/', verbose_name='画像'),
            preserve_default=False,
        ),
    ]
