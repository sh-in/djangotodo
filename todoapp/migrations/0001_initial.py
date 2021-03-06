# Generated by Django 4.0.2 on 2022-03-01 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todoapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タスク名')),
                ('description', models.TextField(blank=True, verbose_name='詳細')),
                ('deadline', models.DateField(verbose_name='締め切り')),
            ],
        ),
    ]
