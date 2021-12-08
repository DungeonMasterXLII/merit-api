# Generated by Django 3.1.13 on 2021-12-08 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('project_type', models.CharField(choices=[('WEBSITE', 'Website'), ('WEBGL_GAME', 'WebGL Game'), ('REPL', 'Console App')], default='R', max_length=20)),
            ],
        ),
    ]
