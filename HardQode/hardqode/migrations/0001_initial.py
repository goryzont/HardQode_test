# Generated by Django 4.2.1 on 2024-03-03 06:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video_link', models.URLField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discipline', to='hardqode.product')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('min_users', models.IntegerField(validators=[django.core.validators.MinValueValidator(3, message='Минимум 3 участника может быть в группе')])),
                ('num_users', models.IntegerField(validators=[django.core.validators.MaxValueValidator(20, message='Максимум 20 участников может быть')])),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='hardqode.product')),
                ('users', models.ManyToManyField(related_name='groupps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
