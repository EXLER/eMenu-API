from django.contrib import admin

from api.models import Menu, Dish


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ()

    def get_readonly_fields(self, request, obj=None):
        base_fields = ["created_at", "updated_at"]
        return set(list(self.readonly_fields) + base_fields)


class MenuAdmin(BaseAdmin):
    model = Menu
    fields = (
        "name",
        "description",
        "dishes",
    )


class DishAdmin(BaseAdmin):
    model = Dish
    fields = (
        "name",
        "description",
        "price",
        "image",
        "preparation_time",
        "is_vegetarian",
    )
    list_display = (
        "name",
        "price",
        "preparation_time",
        "is_vegetarian",
    )


admin.site.register(Menu, MenuAdmin)
admin.site.register(Dish, DishAdmin)