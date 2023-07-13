from django.test import TestCase
from restaurant.models import Menu
from decimal import Decimal

class MenuTest(TestCase):
    def setUp(self) -> None:
        self.item1 = Menu.objects.create(
            title = 'Coffee',
            price = 1.25,
            inventory = 15
        )

    def test_create_menu_item(self) -> None:
        item2 = Menu.objects.create(
            title = 'Cookie',
            price = 2.00,
            inventory = 7
        )
        self.assertEqual(Menu.objects.count(), 5)
        self.assertEqual(item2.title, 'Cookie')
        self.assertEqual(item2.price, Decimal(2.00))
        self.assertEqual(item2.inventory, 7)

    def test_get_menu_item(self) -> None:
        item = Menu.objects.get(id = self.item1.id)
        self.assertEqual(item.title, 'Coffee')
        self.assertEqual(item.price, Decimal(1.25).quantize(Decimal("0.00")))
        self.assertEqual(item.inventory, 15)

    def test_delete_menu_item(self) -> None:
        item = Menu.objects.get(id = self.item1.id)
        item.delete()
        self.assertEqual(Menu.objects.count(), 0)