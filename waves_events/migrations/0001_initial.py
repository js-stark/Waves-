# Generated by Django 4.0.2 on 2022-03-28 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('rounds', models.TextField(blank=True, max_length=500)),
                ('rules', models.TextField(blank=True, max_length=500)),
                ('contact', models.TextField(blank=True, max_length=500)),
                ('date', models.TextField(blank=True, max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='photos/events')),
                ('poster', models.ImageField(upload_to='photos/posters')),
                ('is_updated', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('stock', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
