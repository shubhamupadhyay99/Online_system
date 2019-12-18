'''Docsstirng'''

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import CustomerProdcutList, CreateProducts
from products.views import UpdateCrudUser, Delete, UsersProductsList

class TestClass(SimpleTestCase):
    '''Docsstirng'''

    def test_list(self):
        '''Docsstirng'''
        url = reverse('detail')
        #print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, UsersProductsList)

    def test_customer_prodcut_list(self):
        '''Docsstirng'''
        url = reverse('customerlist')
        #print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, CustomerProdcutList)

    def test_create_product(self):
        '''Docsstirng'''
        url = reverse('createProducts')
        #print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, CreateProducts)

    def test_update(self):
        '''Docsstirng'''
        url = reverse('crud_ajax_update')
        #print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, UpdateCrudUser)

    def test_delete(self):
        '''Docsstirng'''
        url = reverse('crud_ajax_delete')
        #print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, Delete)
