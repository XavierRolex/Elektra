from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Product, Wishlist
from django.core.files.uploadedfile import SimpleUploadedFile

class WishlistTests(TestCase):
    """
    Unit testing for Wishlist.
    - Adding products to the wishlist.
    - Removing products from the wishlist.
    - Checking wishlist products.
    """
    def setUp(self):
        """
        Setting up the test environment.
        - Creating a test user , product (with an image), and client session.
        - Creating a dummy image file to fix ImageField error.
        """
        # test (user, product, and client)
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Creating a dummy image file to fix ImageField error
        image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')

        # Creating a product with an image
        self.product = Product.objects.create(
            name='Test Product',
            price=10.0,
            description='A cool product',
            image=image
        )

        # User log in
        self.client.force_login(self.user)

    def test_add_to_wishlist(self):
        """
        Test of adding a product to the wishlist.
        - Check if the product is added to the wishlist.
        - Check if the response is a redirect.
        """
        response = self.client.get(reverse('add_to_wishlist', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  # Expect redirect
        self.assertTrue(Wishlist.objects.filter(user=self.user, product=self.product).exists())

    def test_remove_from_wishlist(self):
        """
        Test of removing a product from the wishlist.
        - Check if the product is removed from the wishlist.
        - Check if the response is a redirect.
        """
        Wishlist.objects.create(user=self.user, product=self.product)
        response = self.client.get(reverse('remove_from_wishlist', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Wishlist.objects.filter(user=self.user, product=self.product).exists())

    def test_view_wishlist(self):
        """
        Test of viewing the wishlist.
        - Check if the response is 200, if yes then OK.
        - Check if the product is displayed in the wishlist.
        """
        Wishlist.objects.create(user=self.user, product=self.product)
        response = self.client.get(reverse('view_wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
