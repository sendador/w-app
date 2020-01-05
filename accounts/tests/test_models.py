from django.test import TestCase, Client
from accounts.models import City
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.city = City.objects.create(
            name='Paris'
        )

    def test__str__(self):
        self.assertEqual(str(self.city), self.city.name)

    def test_clean(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.city = self.client.post('/', {'name': 'london'}, format='text/html')
        city_name = City.objects.get(name='London')
        self.assertEqual(city_name.name, 'London')

