from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count
from django.db.models.functions import Abs
from django.db import transaction

from hardqode.models import Product, Lesson
from hardqode.serializer import ProductSerializer, LessonSerializer


def distribute_users_to_groups(product):
    groups = product.group_set.all().order_by('min_users')
    users = product.creator.groups.filter(product=product).annotate(num_users=Count('users')).order_by('num_users')

    with transaction.atomic():
        for user in users:
            min_group = groups.first()
            for group in groups[1:]:
                if group.users.count() < min_group.users.count():
                    min_group = group
            min_group.users.add(user)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(product_id=product_id, product__group__users=user)