from rest_framework import serializers

from api.models import Menu, Dish


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ("id", "name", "description", "created_at", "updated_at", "dishes")


class DishSerializer(serializers.HyperlinkedModelSerializer):
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
