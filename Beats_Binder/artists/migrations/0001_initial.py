# Generated by Django 5.0.1 on 2024-01-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deezer_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('cover', models.URLField()),
                ('albums', models.ManyToManyField(to='albums.album')),
            ],
        ),
    ]
