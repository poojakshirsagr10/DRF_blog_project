# Generated by Django 5.0.6 on 2024-05-16 11:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('science', 'science'), ('history', 'history'), ('geography', 'geography'), ('other', 'other')], default='other', max_length=10)),
                ('blog_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_blog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]