from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

from random import randint

# Создать сущность продукта. У продукта должен быть создатель этого продукта(автор/преподаватель).
# Название продукта, дата и время старта, стоимость (1 балл)


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subject')
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=5, decimal_places=2)


class Lesson(models.Model):
    subject = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discipline')
    title = models.CharField(max_length=100)
    video_link = models.URLField()


class Group(models.Model):
    subject = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subject')
    name = models.CharField(max_length=100)
    min_users = models.IntegerField(validators=[
        MinValueValidator(3, message='Минимум 3 участника может быть в группе')])
    num_users = models.IntegerField(validators=[
        MaxValueValidator(20, message='Максимум 20 участников может быть')
    ])
    users = models.ManyToManyField(User, related_name='groupps')


