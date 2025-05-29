import unittest
from unittest.mock import Mock, patch
from flask import current_app
from app.models import Product
from app.services import ProductService

from app import create_app, db

class ProductTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @patch('app.services.ProductService')
    def test_find_by_barcode(self, mock_service):
        mock_product = Mock()
        mock_product.name = 'Coca Cola'
        mock_product.bar_code = '77912'
        mock_product.price = 4000.0
        mock_service.find_by_bar_code.return_value = mock_product

        product = mock_service.find_by_bar_code('77912')
        self.assertEqual(product.name, 'Coca Cola')
        self.assertEqual(product.bar_code, '77912')
        self.assertEqual(product.price, 4000.0)


    @patch('app.services.ProductService')
    def test_find_by_name(self, mock_service):
        mock_product = Mock()
        mock_product.name = 'Coca Cola'
        mock_product.bar_code = '77912'
        mock_product.price = 4000.0
        mock_service.find_by_name.return_value = [mock_product]

        product = mock_service.find_by_name('Coca Cola')
        self.assertEqual(product[0].name, 'Coca Cola')
        self.assertEqual(product[0].bar_code, '77912')
        self.assertEqual(product[0].price, 4000.0)


if __name__ == '__main__':
  unittest.main()
