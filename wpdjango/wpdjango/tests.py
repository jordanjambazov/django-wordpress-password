"""
Tests for WordPress authentication.
"""

from django.test import TestCase

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import get_hasher

User = get_user_model()  # get any custom user model

hasher = get_hasher('phpass')


TEST_WORDPRESS_USERS = [
    ('test', 'test123', '$P$BmEhFPRHgMIjN/L.dtlKB2RgJxnegN1'),
    #('jordan', '', '')
]


class TestWordPress(TestCase):

    def test_wordpress_users_hashes(self):
        for username, password, wordpress_hash in TEST_WORDPRESS_USERS:
            user = User()
            user.username = username
            user.password = hasher.from_orig(wordpress_hash)
            user.save()
            password_matches = user.check_password(password)
            self.assertTrue(password_matches,
                            "User {} password does not match".format(username))