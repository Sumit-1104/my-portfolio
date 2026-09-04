from unittest.mock import patch

from django.test import TestCase


class PortfolioTests(TestCase):
	def test_homepage_renders_contact_form(self):
		response = self.client.get('/', HTTP_HOST='localhost')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'action="/contact/"')
		self.assertContains(response, 'csrfmiddlewaretoken')

	@patch('account.views.EmailMessage.send')
	def test_contact_sends_message(self, send):
		response = self.client.post('/contact/', {
			'name': 'Test User',
			'email': 'test@example.com',
			'subject': 'Hello',
			'message': 'Test message',
		}, HTTP_HOST='localhost')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b'OK')
		send.assert_called_once()
