# Generated by Django 3.1.7 on 2021-03-07 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
    ]
