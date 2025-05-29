import unittest
from flask import current_app
from app.models import Product
from app.services import ProductService

from app import create_app, db

service = ProductService()

class ProductTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        product = self.create_product('Coca Cola', '77912', '4000')

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def create_product(self, name, bar_code, price):
        new_product = Product(name=name, bar_code=bar_code, price=price)
        db.session.add(new_product)
        db.session.commit()
        return new_product


    def test_find_by_barcode(self):
        product = service.find_by_bar_code('77912')
        self.assertEqual(product.name, 'Coca Cola')
        self.assertEqual(product.bar_code, '77912')
        self.assertEqual(product.price, 4000.0)
    

if __name__ == '__main__':
  unittest.main()