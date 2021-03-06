# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-15 08:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=25)),
                ('pic_cover', models.ImageField(null=True, upload_to='media/')),
                ('content', models.FileField(upload_to='pdfs/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=10000, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='store.Books')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(null=True, upload_to='media/')),
                ('bio', models.CharField(default='Hi!', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('teach_pic', models.ImageField(upload_to='media/')),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHERS', 'Others')], max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('available', models.CharField(default='Yes/No', max_length=5, null=True)),
                ('number', models.IntegerField()),
                ('subject', models.TextField(max_length=10000)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='teacher_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='store.Teacher'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='books',
            name='book_name',
            field=models.ForeignKey(max_length=25, on_delete=django.db.models.deletion.CASCADE, to='store.Profile'),
        ),
    ]
