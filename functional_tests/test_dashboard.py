from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User


class TestDashboardPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'functional_tests\geckodriver.exe')
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def tearDown(self):
        self.browser.quit()

    def test_redirect_after_login(self):
        self.browser.get(self.live_server_url)
        login_page_url = self.browser.current_url
        self.browser.find_element_by_name('username').send_keys('testuser')
        self.browser.find_element_by_name('password').send_keys('testpassword')
        self.browser.find_element_by_name('submit').click()
        redirect_page_url = self.browser.current_url
        self.assertNotEqual(login_page_url, redirect_page_url)

    def test_user_add_city_and_delete(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('username').send_keys('testuser')
        self.browser.find_element_by_name('password').send_keys('testpassword')
        self.browser.find_element_by_name('submit').click()
        self.browser.find_element_by_name('name').send_keys('Paris')
        self.browser.find_element_by_name('submit-city').click()
        self.assertEqual(self.browser.find_element_by_class_name('city-name').text, 'Paris')
        self.assertEqual(self.browser.find_element_by_class_name('successful-msg').text, 'City added successfully')
        self.browser.find_element_by_name('delete-city').click()
        self.assertEqual(self.browser.find_element_by_tag_name('h6').text, '')

    def test_user_add_city_which_exist(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('username').send_keys('testuser')
        self.browser.find_element_by_name('password').send_keys('testpassword')
        self.browser.find_element_by_name('submit').click()
        self.browser.find_element_by_name('name').send_keys('Paris')
        self.browser.find_element_by_name('submit-city').click()
        self.browser.find_element_by_name('name').send_keys('Paris')
        self.browser.find_element_by_name('submit-city').click()
        self.assertEqual(self.browser.find_element_by_class_name('error-msg').text, 'This city is already added!')

    def test_user_add_city_which_isnt_real(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('username').send_keys('testuser')
        self.browser.find_element_by_name('password').send_keys('testpassword')
        self.browser.find_element_by_name('submit').click()
        self.browser.find_element_by_name('name').send_keys('testwrongcity')
        self.browser.find_element_by_name('submit-city').click()
        self.assertEqual(self.browser.find_element_by_class_name('error-msg').text, 'City doesnt exist')

    def test_user_add_blank_form(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('username').send_keys('testuser')
        self.browser.find_element_by_name('password').send_keys('testpassword')
        self.browser.find_element_by_name('submit').click()
        self.browser.find_element_by_name('name').send_keys('')
        self.browser.find_element_by_name('submit-city').click()
        self.assertEqual(self.browser.find_element_by_class_name('error-msg').text, 'Please write the city name')

    def test_user_logout(self):
        self.browser.get(self.live_server_url)
        login_url = self.browser.current_url
        self.browser.find_element_by_name('username').send_keys('testuser')
        self.browser.find_element_by_name('password').send_keys('testpassword')
        self.browser.find_element_by_name('submit').click()
        self.browser.find_element_by_class_name('logout-footer').click()
        self.assertEqual(login_url, self.browser.current_url)