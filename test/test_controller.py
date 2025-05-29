import unittest
from unittest.mock import patch
from flask import Flask, jsonify, Blueprint

class ProductControllerTestCase(unittest.TestCase):

    # MOCKEO DE LA APP COMPLETA---------------------------------------------------------------------
    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True

        product = Blueprint('product', __name__)

        @product.route('/products/<int:id>', methods=['GET'])
        def get_by_id(id):
            from app.controllers import product_controller
            product = product_controller.service.find_by_id(id)
            if not product:
                return jsonify({'message': 'Producto no encontrado'}), 404
            return jsonify(product_controller.product_schema.dump(product))

        @product.route('/products/bar_code/<bar_code>', methods=['GET'])
        def get_by_bar_code(bar_code):
            from app.controllers import product_controller
            product = product_controller.service.find_by_bar_code(bar_code)
            if not product:
                return jsonify({'message': 'Producto no encontrado'}), 404
            return jsonify(product_controller.product_schema.dump(product))
        
        self.app.register_blueprint(product)
        self.client = self.app.test_client()
    # MOCKEO DE LA APP COMPLETA---------------------------------------------------------------------

    @patch('app.controllers.product_controller.service.find_by_id')
    @patch('app.controllers.product_controller.product_schema.dump')
    def test_get_by_id_success(self, mock_find_by_id, mock_dump):
        mock_product = {'id': 1, 'name': 'Coca Cola','bar_code':'77912', 'price': 4000.0}
        mock_find_by_id.return_value = mock_product
        mock_dump.return_value = mock_product

        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), mock_product)

    @patch('app.controllers.product_controller.service.find_by_id')
    def test_get_by_id_not_found(self, mock_find_by_id):
        mock_find_by_id.return_value = None

        response = self.client.get('/products/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Producto no encontrado'})

    
    @patch('app.controllers.product_controller.service.find_by_bar_code')
    @patch('app.controllers.product_controller.product_schema.dump')
    def test_get_by_bar_code_success(self, mock_find_by_barcode, mock_dump):
        mock_product = {'id': 1, 'name': 'Coca Cola','bar_code':'77912', 'price': 4000.0}
        mock_find_by_barcode.return_value = mock_product
        mock_dump.return_value = mock_product

        response = self.client.get('/products/bar_code/77912')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), mock_product)

    @patch('app.controllers.product_controller.service.find_by_bar_code')
    def test_get_by_bar_code_not_found(self, mock_find_by_name):
        mock_find_by_name.return_value = None

        response = self.client.get('/products/bar_code/99999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Producto no encontrado'})

if __name__ == '__main__':
    unittest.main()
