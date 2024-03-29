# Generated by Django 4.0 on 2024-03-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('is_done', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('completed', models.DateField(auto_now=True)),
            ],
        ),
    ]
