from django.test import TestCase
from django.urls import reverse

class PageTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_men_page(self):
        response = self.client.get(reverse('men'))
        self.assertEqual(response.status_code, 200)

    def test_women_page(self):
        response = self.client.get(reverse('women'))
        self.assertEqual(response.status_code, 200)

    def test_kids_page(self):
        response = self.client.get(reverse('kids'))
        self.assertEqual(response.status_code, 200)

    def test_accessories_page(self):
        response = self.client.get(reverse('accessories'))
        self.assertEqual(response.status_code, 200)

    def test_cart_page(self):
        response = self.client.get(reverse('view_cart'))
        self.assertIn(response.status_code, [200, 302])

    def test_search_page(self):
        response = self.client.get(reverse('search'))
        self.assertIn(response.status_code, [200, 302])

    def test_checkout_page(self):
        response = self.client.get(reverse('checkout'))
        self.assertIn(response.status_code, [200, 302])

    def test_admin_dashboard_page(self):
        response = self.client.get(reverse('admin_dashboard'))
        self.assertIn(response.status_code, [200, 302])

    def test_customer_reviews_page(self):
        response = self.client.get(reverse('customer_reviews'))
        self.assertEqual(response.status_code, 200)

    def test_customer_support_page(self):
        response = self.client.get(reverse('customer_support'))
        self.assertEqual(response.status_code, 200)

    def test_track_order_page(self):
        response = self.client.get(reverse('track_order', args=[1]))  # dummy order_id
        self.assertIn(response.status_code, [200, 302, 404])

    def test_cancel_order_page(self):
        response = self.client.get(reverse('cancel_order', args=[1]))  # dummy order_id
        self.assertIn(response.status_code, [200, 302, 404])

    def test_user_profile_page(self):
        response = self.client.get(reverse('user_profile', args=[1]))  # dummy user_id
        self.assertIn(response.status_code, [200, 302, 404])
