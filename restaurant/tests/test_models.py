from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_create_menu_item(self):
        # Create a new instance of the Menu model
        item = Menu.objects.create(title="Spaghetti", price=10.99, inventory=5)
        
        # Test the string representation of the Menu instance
        self.assertEqual(str(item), "Spaghetti : 10.99")
