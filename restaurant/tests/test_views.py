from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework import status
import json

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        self.client = Client()
        self.menu_item1 = Menu.objects.create(title="Spaghetti", price=10.99, inventory=5)
        self.menu_item2 = Menu.objects.create(title="Pizza", price=12.99, inventory=10)
        self.menu_item3 = Menu.objects.create(title="Salad", price=5.99, inventory=20)

    def test_getall(self):
        # Use the API to get all menu items at '/restaurant/menu/'
        response = self.client.get('/restaurant/menu/')

        # Serialize the menu items
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        # Check if the response matches the serialized data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), serializer.data)
