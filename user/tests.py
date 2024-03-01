from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

client = Client()
user = get_user_model().objects.create_user(email="john@doe.com", password="johnpassword")

# Log in
client.login(username="john", password="johnpassword")

# Log out
client.logout()
user.delete()

