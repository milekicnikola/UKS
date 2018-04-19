# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('message', models.TextField()),
                ('dateTime', models.DateTimeField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('hashcode', models.CharField(primary_key=True, max_length=64, serialize=False)),
                ('message', models.TextField()),
                ('dateTime', models.DateTimeField()),
                ('user', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('finishDate', models.DateField(null=True)),
                ('description', models.TextField()),
                ('timeSpent', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('donePercentage', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('assignedTo', models.ForeignKey(blank=True, related_name='assignedTo', to=settings.AUTH_USER_MODEL, null=True)),
                ('createdBy', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='createdBy')),
            ],
        ),
        migrations.CreateModel(
            name='IssueType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('key', models.CharField(unique=True, max_length=10)),
                ('marker', models.CharField(choices=[('default', 'silver'), ('primary', 'blue'), ('success', 'green'), ('info', 'light blue'), ('warning', 'yellow'), ('danger', 'red')], max_length=15, default='default')),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('key', models.CharField(unique=True, max_length=10)),
                ('marker', models.CharField(choices=[('default', 'silver'), ('primary', 'blue'), ('success', 'green'), ('info', 'light blue'), ('warning', 'yellow'), ('danger', 'red')], max_length=15, default='default')),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('key', models.CharField(unique=True, max_length=10)),
                ('marker', models.CharField(choices=[('default', 'silver'), ('primary', 'blue'), ('success', 'green'), ('info', 'light blue'), ('warning', 'yellow'), ('danger', 'red')], max_length=15, default='default')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(unique=True, max_length=10)),
                ('description', models.TextField()),
                ('contributors', models.ManyToManyField(blank=True, related_name='contributors', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='owner')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('key', models.CharField(unique=True, max_length=10)),
                ('marker', models.CharField(choices=[('default', 'silver'), ('primary', 'blue'), ('success', 'green'), ('info', 'light blue'), ('warning', 'yellow'), ('danger', 'red')], max_length=15, default='default')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='label',
            field=models.ForeignKey(verbose_name='Issue type', to='uksApp.IssueType'),
        ),
        migrations.AddField(
            model_name='issue',
            name='milestone',
            field=models.ForeignKey(blank=True, to='uksApp.Milestone', null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='priority',
            field=models.ForeignKey(blank=True, to='uksApp.Priority', null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(to='uksApp.Project'),
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(to='uksApp.Status'),
        ),
        migrations.AddField(
            model_name='commit',
            name='issue',
            field=models.ManyToManyField(blank=True, related_name='commits', to='uksApp.Issue'),
        ),
        migrations.AddField(
            model_name='commit',
            name='project',
            field=models.ForeignKey(to='uksApp.Project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(to='uksApp.Issue'),
        ),
    ]
