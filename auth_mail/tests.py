from django.test import TestCase
from django.http import HttpRequest  


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = self.client.get("/")
        html = response.content.decode("utf8")  
        self.assertIn("<title>Home</title>", html)  
        self.assertTemplateUsed(response, "home.html")
