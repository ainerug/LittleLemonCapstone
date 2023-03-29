from django.test import TestCase
from restaurant.models import Menu

#TestCase class
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="GreekSalad", price=12.00, inventory=100)
        self.assertEqual(item, "GreekSalad : 12.00")
