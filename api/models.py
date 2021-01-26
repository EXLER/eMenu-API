from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator

from api.functions import get_image_path


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class Dish(BaseModel):
    name = models.CharField(max_length=200)
    price = models.DecimalField(
        decimal_places=2, max_digits=5, validators=[MinValueValidator(Decimal("0.00"))]
    )
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    preparation_time = models.PositiveIntegerField()
    is_vegetarian = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return f"{self.name}{' (vegetarian)' if self.is_vegetarian else ''}"


class Menu(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    dishes = models.ManyToManyField(Dish, related_name="menus", blank=True)

    def __str__(self):
        return self.name