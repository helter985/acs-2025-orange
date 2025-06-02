import unittest
from unittest.mock import patch, Mock
from app import create_app
from app.services import ProductService

class ProductServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.mock_product = Mock()
        self.mock_product.name = 'Coca Cola'
        self.mock_product.bar_code = '77912'
        self.mock_product.price = 4000.0


    @patch('app.repositories.product_repository.ProductRepository.find_by_bar_code')
    def test_find_by_barcode(self, mock_find_by_bar_code):
        mock_find_by_bar_code.return_value = self.mock_product
        service = ProductService()
        product = service.find_by_bar_code('77912')
        self.assertEqual(product.name, 'Coca Cola')
        self.assertEqual(product.bar_code, '77912')
        self.assertEqual(product.price, 4000.0)

    @patch('app.repositories.product_repository.ProductRepository.find_by_name')
    def test_find_by_name(self, mock_find_by_name):
        mock_find_by_name.return_value = [self.mock_product]
        service = ProductService()
        result = service.find_by_name('Coca')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'Coca Cola')
        self.assertEqual(result[0].bar_code, '77912')
        self.assertEqual(result[0].price, 4000.0)

    @patch('app.repositories.product_repository.ProductRepository.find_by_id')
    def test_find_by_id(self, mock_find_by_id):
        mock_find_by_id.return_value = self.mock_product
        service = ProductService()
        product = service.find_by_id('0')
        self.assertEqual(product.name, 'Coca Cola')
        self.assertEqual(product.bar_code, '77912')
        self.assertEqual(product.price, 4000.0)

    @patch('app.repositories.product_repository.ProductRepository.find_all')
    def test_find_all(self, mock_find_all):
        mock_find_all.return_value = [self.mock_product]
        service = ProductService()
        result = service.find_all()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'Coca Cola')
        self.assertEqual(result[0].bar_code, '77912')
        self.assertEqual(result[0].price, 4000.0)

if __name__ == '__main__':
    unittest.main()

