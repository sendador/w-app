from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import indexView, registerView
from django.contrib.auth.models import User


class TestUrls(SimpleTestCase):

    def test_index_page_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, indexView)

    def test_register_page_url_resolves(self):
        url = reverse('register_url')
        self.assertEqual(resolve(url).func, registerView)


class TestLogin(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def tearDown(self):
        self.user.delete()

    def test_login_page_GET(self):

        response = self.client.get(reverse('login_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_success(self):
        response = self.client.login(username='testuser', password='testpassword')
        self.assertEqual(response, True)

    def test_login_failed_wrong_password(self):
        response = self.client.login(username='testuser', password='wrong_password')
        self.assertEqual(response, False)

    def test_login_failed_wrong_login(self):
        response = self.client.login(username='wrong_user', password='testpassword')
        self.assertEqual(response, False)

    def test_redirect_if_login(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/login/', follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.redirect_chain[0][0], '/')

    def test_not_redirect_if_not_login(self):
        response = self.client.get('/login/', follow=True)
        self.assertEqual(response.redirect_chain, [])
















