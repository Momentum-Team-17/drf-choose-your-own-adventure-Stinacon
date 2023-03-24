# Generated by Django 4.1.7 on 2023-03-23 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_tracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trackings_of_book', to='library.book'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trackings_of_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='tracker',
            constraint=models.UniqueConstraint(fields=('user', 'book'), name='tracker_constraints'),
        ),
    ]