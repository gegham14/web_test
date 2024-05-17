# Generated by Django 5.0.6 on 2024-05-15 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=35)),
                ('review', models.TextField(max_length=350)),
                ('model_text', models.CharField(blank=True, max_length=40)),
            ],
        ),
    ]
