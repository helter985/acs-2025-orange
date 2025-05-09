from app.models import Product
from app.repositories.product_repository import ProductRepository

class ProductService:

    def __init__(self):
        self.__repo = ProductRepository()

    def find_by_id(self, id) -> Product:
        return self.__repo.find_by_id(id)
    
    def find_all(self) -> Product:
        return self.__repo.find_all()

    def find_by_name(self, name) -> list:
        return self.__repo.find_by_name(name)

    def find_by_bar_code(self, bar_code) -> list:
        return self.__repo.find_by_bar_code(bar_code)
    
