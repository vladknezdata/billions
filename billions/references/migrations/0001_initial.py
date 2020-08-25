# Generated by Django 3.1 on 2020-08-25 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('aka', models.CharField(max_length=25)),
                ('img_small', models.ImageField(blank=True, upload_to='')),
                ('img_large', models.ImageField(blank=True, upload_to='')),
                ('actor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('aired', models.DateField()),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='ReferenceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('year', models.IntegerField()),
                ('poster', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('time', models.TimeField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('dialog', models.TextField(max_length=500)),
                ('explanation', models.TextField(max_length=1500)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='references.referencecategory')),
                ('characters', models.ManyToManyField(to='references.Character')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='references.episode')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='references.season')),
            ],
            options={
                'ordering': ['season', 'episode', 'time'],
            },
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='references.season'),
        ),
    ]
