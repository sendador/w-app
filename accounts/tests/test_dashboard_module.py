from django.test import TestCase, Client
from accounts.models import City
from django.contrib.auth.models import User
from django.urls import reverse


class TestDashboard(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.city = City.objects.create(
            name='Paris'
        )

    def tearDown(self):
        self.city.delete()

    def test_dashboard_view_if_logged(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_if_logout(self):
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_delete_city(self):
        before_delete = City.objects.filter(name='Paris').count()
        response = self.client.get('/delete/Paris', follow=True)
        after_delete = City.objects.filter(name='Paris').count()
        self.assertTrue(before_delete>after_delete)
        self.assertEqual(response.redirect_chain[0][1], 301)
        self.assertEqual(response.redirect_chain[1][1], 302)

    def test_add_new_city_success(self):
        before_add = City.objects.all().count()
        response = self.client.post('/', {'name': 'London'}, format='text/html')
        after_add = City.objects.all().count()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(before_add < after_add)

    def test_add_new_city_failed(self):
        before_add = City.objects.all().count()
        response = self.client.post('/', {'name': 'Test_Wrong_City'}, format='text/html')
        after_add = City.objects.all().count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(before_add, after_add)

    def test_add_city_already_exist(self):
        first_city = self.client.post('/', {'name': 'Tokyo'}, format='text/html')
        before_add = City.objects.all().count()
        second_city = self.client.post('/', {'name': 'Tokyo'}, format='text/html')
        after_add = City.objects.all().count()
        self.assertEqual(first_city.status_code, 200)
        self.assertEqual(second_city.status_code, 200)
        self.assertEqual(before_add, after_add)






