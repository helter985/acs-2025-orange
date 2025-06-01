from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.mapping.product_schema import product_schema, products_schema

product = Blueprint('product', __name__)
service = ProductService()

@product.route('/products', methods=['GET'])
def get_all():
    products = service.find_all()
    return jsonify(products_schema.dump(products))

@product.route('/products/<int:id>', methods=['GET'])
def get_by_id(id):
    product = service.find_by_id(id)
    if not product:
        response = jsonify({'message': 'Producto no encontrado'})
        response.status_code = 404
        return response
    response = product_schema.dump(product)
    response = jsonify(response)
    response.status_code = 200
    return response

@product.route('/products/name/<string:name>', methods=['GET'])
def get_by_name(name):
    products = service.find_by_name(name)
    if not products:
        return jsonify({'message': 'No se encontraron productos con ese nombre'}), 404
    return jsonify(products_schema.dump(products), 200)

@product.route('/products/barcode/<string:bar_code>', methods=['GET'])
def get_by_bar_code(bar_code):
    product = service.find_by_bar_code(bar_code)
    if not product:
        return jsonify({'message': 'No se encontró producto con ese código de barras'}), 404
    return jsonify(product_schema.dump(product))

