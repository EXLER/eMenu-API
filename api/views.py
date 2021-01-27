from django.shortcuts import render
from rest_framework import viewsets, permissions

from api.models import Menu, Dish
from api.serializers import MenuSerializer, DishSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage menu cards.
    """

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class DishViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage dishes.
    """

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticated]


class PublicMenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menus to be viewed.
    """

    pass
