from tornado.testing import AsyncHTTPTestCase
from torapp import main


class TestTorapp(AsyncHTTPTestCase):

    def get_app(self):
        return main.make_app()

    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Hello world')
