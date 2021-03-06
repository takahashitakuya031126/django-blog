# Generated by Django 2.0.2 on 2020-06-16 02:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('image', models.ImageField(blank=True, upload_to='images', verbose_name='画像')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, verbose_name='タグ名')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog_app.Tag', verbose_name='タグ'),
        ),
    ]
