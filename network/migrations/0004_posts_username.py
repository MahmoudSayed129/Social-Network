# Generated by Django 3.2.7 on 2021-09-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_rename_c_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='username',
            field=models.CharField(default='', max_length=256),
        ),
    ]