# add_product.py
from app import create_app
from app.models.product import Product
from app.config.database import db

app = create_app()

def crear_producto(name, bar_code, price):
    with app.app_context():
        new_product = Product(name=name, bar_code=bar_code, price=price)
        db.session.add(new_product)
        db.session.commit()

def main():
    # Ejemplo de uso
    crear_producto('Producto 3', '1267890', 1099)
    crear_producto('Producto 4', '2678901', 599)

if __name__ == '__main__':
    main()
