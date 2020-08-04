from django.test import TestCase
from django.urls import reverse, resolve


class EmployeeUrlsTestCase(TestCase):
    
    def test_api_urls(self):
        url = reverse('list')
        self.assertEquals(url, '/api/employee/')

    def test_insert_urls(self):
        url = reverse('insert')
        self.assertEquals(url, '/')

    def test_detail_urls(self):
        url = reverse('detail', args=[2])
        self.assertEquals(url, '/api/2/')
