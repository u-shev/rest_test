from django.db.models import Prefetch
from rest_framework import generics
from .models import Food, FoodCategory
from .serializers import FoodListSerializer


class FoodCategoryListAPIView(generics.ListAPIView):

    serializer_class = FoodListSerializer

    queryset = FoodCategory.objects.filter(
        food__is_publish=True
        ).prefetch_related(
            Prefetch('food',
                     queryset=Food.objects.filter(
                         is_publish=True).only(
                             'id', 'category', 'internal_code', 'code',
                             'name_ru', 'description_ru', 'description_en',
                             'description_ch', 'is_vegan', 'is_special',
                             'cost', 'additional').prefetch_related
                     (Prefetch('additional',
                               queryset=Food.objects.all().only(
                                            'internal_code'))))).distinct().only(
                                                'id', 'name_ru', 'name_en',
                                                'name_ch', 'order_id')
