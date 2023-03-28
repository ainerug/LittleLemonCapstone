from django.test import TestCase
from restaurant.views import Menu
from rest_framework.test import APIClient
from django.urls import reverse
from restaurant.serializers import MenuSerializer
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(name='GreekSalad', price=12.00)
        self.menu2 = Menu.objects.create(name='Pasta', price=10.00)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)