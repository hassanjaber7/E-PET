from django.test import TestCase
from selenium import webdriver


class GenericWebAppTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.live_server_url = "http://127.0.0.1:8000"  # Update with your app's URL

    def test_homepage_loads(self):
        self.browser.get(self.live_server_url)
        # Replace 'Your Web App' with the text that should be on your homepage
        self.assertIn("EPET", self.browser.title)

    def tearDown(self):
        self.browser.quit()
