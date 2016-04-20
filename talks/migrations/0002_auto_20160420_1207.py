# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('when', models.DateTimeField()),
                ('room', models.CharField(choices=[('517D', '517D'), ('517C', '517C'), ('517AB', '517AB'), ('520', '520'), ('710A', '710A')], max_length=10)),
                ('host', models.CharField(max_length=255)),
                ('talk_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talks', to='talks.TalkList')),
            ],
            options={
                'ordering': ('when', 'room'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='talk',
            unique_together=set([('talk_list', 'name')]),
        ),
    ]