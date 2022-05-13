# Generated by Django 4.0.4 on 2022-05-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('header_uz', models.CharField(max_length=200, null=True)),
                ('header_en', models.CharField(max_length=200, null=True)),
                ('text', models.TextField(max_length=300)),
                ('text_uz', models.TextField(max_length=300, null=True)),
                ('text_en', models.TextField(max_length=300, null=True)),
                ('link', models.CharField(max_length=70)),
                ('link_uz', models.CharField(max_length=70, null=True)),
                ('link_en', models.CharField(max_length=70, null=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog Post',
            },
        ),
    ]