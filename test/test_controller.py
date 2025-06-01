import unittest
from unittest.mock import patch
from app import create_app

class ProductControllerTestCase(unittest.TestCase):

    # Set Up de la aplicacion y el cliente de prueba, creando un producto Mock para utilizar en las pruebas
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.mock_product = {'id': 1, 'name': 'Coca Cola','bar_code':'77912', 'price': 4000.0}
        

    @patch('app.controllers.product_controller.service.find_by_id')
    def test_get_by_id_success(self, mock_find_by_id):
        mock_find_by_id.return_value = self.mock_product
        
        response = self.client.get('/api/v1/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), self.mock_product)

    @patch('app.controllers.product_controller.service.find_by_id')
    def test_get_by_id_not_found(self, mock_find_by_id):
        mock_find_by_id.return_value = None

        response = self.client.get('/api/v1/products/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Producto no encontrado'})

    
    @patch('app.controllers.product_controller.service.find_by_bar_code')
    def test_get_by_bar_code_success(self, mock_find_by_barcode):
        mock_find_by_barcode.return_value = self.mock_product
        

        response = self.client.get('/api/v1/products/bar-code/77912')
        print(response.get_json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), self.mock_product)

    @patch('app.controllers.product_controller.service.find_by_bar_code')
    def test_get_by_bar_code_not_found(self, mock_find_by_name):
        mock_find_by_name.return_value = None

        response = self.client.get('/api/v1/products/bar-code/99999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Producto no encontrado'})

if __name__ == '__main__':
    unittest.main()
