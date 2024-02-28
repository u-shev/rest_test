from django.contrib import admin
from django.urls import include, path
from food.views import FoodCategoryListAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/foods/', FoodCategoryListAPIView.as_view()),
    path("__debug__/", include("debug_toolbar.urls")),
]
