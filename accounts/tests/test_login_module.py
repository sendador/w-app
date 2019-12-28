from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import indexView, registerView


class TestUrls(SimpleTestCase):

    def test_index_page_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, indexView)

    def test_register_page_url_resolves(self):
        url = reverse('register_url')
        self.assertEqual(resolve(url).func, registerView)


class TestLoginTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login_page_GET(self):

        response = self.client.get(reverse('login_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')














