from django.test import TestCase, Client
from django.urls import reverse


class TestRegister(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }

    def test_register_page_GET(self):
        response = self.client.get(reverse('register_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_register_success(self):
        response = self.client.post('/register/', self.user, format='text/html')
        self.assertEqual(response.status_code, 302)
