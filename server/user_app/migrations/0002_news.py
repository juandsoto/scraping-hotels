# Generated by Django 4.1.7 on 2023-05-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('news_date', models.DateField(auto_now_add=True)),
                ('news_title', models.CharField(max_length=50)),
                ('news_description', models.CharField(max_length=300)),
                ('news_image', models.URLField()),
            ],
        ),
    ]
