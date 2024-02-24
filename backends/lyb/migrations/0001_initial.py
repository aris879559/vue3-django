# Generated by Django 4.2.1 on 2024-02-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lyb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('posttime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'd_lyb',
            },
        ),
    ]
