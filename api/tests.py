from django.urls import reverse
from django.forms.models import model_to_dict
from rest_framework.test import APITestCase, APIClient

from api.models import Dish, Menu


class PublicTestCase(APITestCase):
    fixtures = ["data.json"]

    def setUp(self):
        self.client = APIClient()

    def test_get_menu_list(self):
        url = reverse("list-list")
        r = self.client.get(url)

        non_empty_menus = Menu.objects.exclude(dishes=None).count()

        self.assertEqual(len(r.json()), non_empty_menus)

    def test_get_menu_details(self):
        menu = Menu.objects.exclude(dishes=None).first()

        url = reverse("list-detail", args=[menu.pk])
        r = self.client.get(url)

        self.assertEqual(menu.name, r.json().get("name"))
        self.assertEqual(menu.dishes.count(), len(r.json().get("dishes")))


class MenuTestCase(APITestCase):
    fixtures = ["data.json"]

    def setUp(self):
        self.client = APIClient()
        self.client.login(username="admin", password="admin")

    def test_get_menus(self):
        url = reverse("menu-list")
        r = self.client.get(url)

        menus = Menu.objects.count()

        self.assertEqual(len(r.json()), menus)

    def test_get_menu_details(self):
        menu = Menu.objects.first()

        url = reverse("menu-detail", args=[menu.pk])
        r = self.client.get(url)

        self.assertEqual(menu.name, r.json().get("name"))
        self.assertEqual(menu.dishes.count(), len(r.json().get("dishes")))

    def test_create_menu(self):
        url = reverse("menu-list")
        data = {
            "name": "Test menu",
            "description": "Random description",
        }

        r = self.client.post(url, data)
        self.assertEqual("Test menu", r.json().get("name"))
        self.assertEqual("Random description", r.json().get("description"))

    def test_update_menu(self):
        menu = Menu.objects.first()
        url = reverse("menu-detail", args=[menu.pk])
        data = {
            "name": "Updated test menu",
        }

        r = self.client.put(url, data)
        self.assertEqual("Updated test menu", r.json().get("name"))
        self.assertEqual(menu.description, r.json().get("description"))

    def test_delete_menu(self):
        menu = Menu.objects.first()
        url = reverse("menu-detail", args=[menu.pk])

        r = self.client.delete(url)
        self.assertFalse(Menu.objects.filter(pk=menu.pk))


class DishTestCase(APITestCase):
    fixtures = ["data.json"]

    def setUp(self):
        self.client = APIClient()
        self.client.login(username="admin", password="admin")

    def test_get_dishes(self):
        url = reverse("dish-list")
        r = self.client.get(url)

        dishes = Dish.objects.count()

        self.assertEqual(len(r.json()), dishes)

    def test_get_dish_details(self):
        dish = Dish.objects.first()

        url = reverse("dish-detail", args=[dish.pk])
        r = self.client.get(url)

        self.assertEqual(dish.name, r.json().get("name"))

    def test_create_dish(self):
        url = reverse("dish-list")
        data = {
            "name": "Test dish",
            "description": "Random description",
            "preparation_time": 30,
            "price": 19.99,
        }

        r = self.client.post(url, data)
        self.assertEqual("Test dish", r.json().get("name"))
        self.assertEqual("Random description", r.json().get("description"))
        self.assertEqual(30, r.json().get("preparation_time"))

    def test_update_dish(self):
        dish = Dish.objects.first()
        url = reverse("dish-detail", args=[dish.pk])
        data = {"name": "Updated test dish", "price": 29.99, "preparation_time": 40}

        r = self.client.put(url, data)
        self.assertEqual("Updated test dish", r.json().get("name"))
        self.assertEqual(dish.description, r.json().get("description"))

    def test_delete_dish(self):
        dish = Dish.objects.first()
        url = reverse("dish-detail", args=[dish.pk])

        r = self.client.delete(url)
        self.assertFalse(Dish.objects.filter(pk=dish.pk))
