# Generated by Django 3.0.2 on 2020-02-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_board_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='author',
            field=models.CharField(default='aaa', max_length=40, verbose_name='작성자'),
            preserve_default=False,
        ),
    ]