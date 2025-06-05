import unittest
from unittest.mock import patch, MagicMock
from app import create_app, db, Product
from app.repositories.product_repository import ProductRepository

class ProductRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        test_config = {
        "TESTING": True,
        # → misma conexión para todos los hilos y en RAM
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        }
        self.app = create_app(test_config)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.productRepository = ProductRepository()
        db.create_all()
        mock_product = Product(name='Coca Cola',bar_code='77912',price= 4000.0) 
        db.session.add(mock_product)
        self.mock_products = [{'id': 1, 'name': 'Coca Cola','bar_code':'77912', 'price': 4000.0}]
        

    def test_find_all(self):
        result = self.productRepository.find_all()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'Coca Cola')
        self.assertEqual(result[0].bar_code, '77912')
        self.assertEqual(result[0].price, 4000.0)

if __name__ == '__main__':
    unittest.main()
