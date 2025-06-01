import unittest
from unittest.mock import patch, MagicMock
from app import create_app
from app.repositories.product_repository import ProductRepository

class ProductRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.productRepository = ProductRepository()
        self.mock_products = [{'id': 1, 'name': 'Cereales','bar_code':'12345', 'price': 2500.0}]

    @patch('app.repositories.product_repository.db')
    def test_find_all(self, mock_db):
        mock_query = MagicMock()
        mock_query.all.return_value = self.mock_products
        mock_db.session.query.return_value = mock_query

        result = self.productRepository.find_all()
        self.assertEqual(result, self.mock_products)

if __name__ == '__main__':
    unittest.main()
