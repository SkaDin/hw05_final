from django.test import TestCase, Client
from http import HTTPStatus


class AboutURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_url_exists_at_desired_location(self):
        """Проверка доступности адресов /about/author/ и /about/tech/"""
        template = ['/about/author/', '/about/tech/']
        for url in template:
            with self.subTest(url=url):
                response = self.guest_client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        """Проверка шаблона для адресов /about/author/ и /about/tech/ ."""
        template_url_names = {
            '/about/author/': 'about/author.html',
            '/about/tech/': 'about/tech.html',
        }
        for address, template in template_url_names.items():
            with self.subTest(template=template):
                response = self.guest_client.get(address)
                self.assertTemplateUsed(response, template)
