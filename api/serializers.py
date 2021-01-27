from rest_framework import serializers

from api.models import Menu, Dish


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("id", "name", "description", "created_at", "updated_at", "dishes")


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            "id",
            "name",
            "description",
            "price",
            "image",
            "preparation_time",
            "is_vegetarian",
        )
