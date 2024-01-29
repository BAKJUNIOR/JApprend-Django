# Generated by Django 4.2.9 on 2024-01-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('published', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('content', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]