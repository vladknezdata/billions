# Generated by Django 3.1 on 2020-08-25 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0003_auto_20200825_2127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='season',
            options={'ordering': ['-number']},
        ),
        migrations.AddField(
            model_name='character',
            name='imdb_link',
            field=models.URLField(blank=True),
        ),
    ]
