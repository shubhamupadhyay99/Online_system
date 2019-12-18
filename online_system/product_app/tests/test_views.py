'''Docsstirng'''


from django.test import TestCase, Client
from django.urls import reverse

class TestView(TestCase):
    '''Docsstirng'''
    def test_product(self):
        '''Docsstirng'''
        client = Client()

        response = client.get(reverse('createProducts'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products_form.html')
