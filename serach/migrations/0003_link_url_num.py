# Generated by Django 2.0.3 on 2018-05-23 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serach', '0002_remove_link_web_type_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='url_num',
            field=models.IntegerField(default=1, max_length=16, verbose_name='访问数量'),
            preserve_default=False,
        ),
    ]
