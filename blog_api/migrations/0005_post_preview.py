# Generated by Django 3.2.3 on 2021-05-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0004_auto_20210531_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
