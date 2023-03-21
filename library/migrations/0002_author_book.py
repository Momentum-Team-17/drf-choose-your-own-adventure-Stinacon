# Generated by Django 4.1.7 on 2023-03-21 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_published', models.DateField(blank=True, null=True)),
                ('genre', models.CharField(choices=[('self-help', 'Self-Help'), ('graphic', 'Graphic Novel'), ('horror', 'Horror'), ('romance', 'Romance'), ('comedy', 'Comedy'), ('spy', 'Spy')], max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_by_author', to='library.author')),
            ],
        ),
    ]
