# Generated by Django 3.2.8 on 2021-12-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='general', max_length=100),
            preserve_default=False,
        ),
    ]
