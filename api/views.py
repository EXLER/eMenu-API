from django.db.models import Count
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Menu, Dish
from api.serializers import MenuSerializer, DishSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage or view menu cards.
    """

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DishViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage or view dishes.
    """

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PublicMenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menus to be viewed.
    """

    queryset = Menu.objects.exclude(dishes=None).annotate(dishes_count=Count("dishes"))
    serializer_class = MenuSerializer
    http_method_names = ["get"]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["name", "created_at", "updated_at"]
    ordering_fields = ["name", "dishes_count"]