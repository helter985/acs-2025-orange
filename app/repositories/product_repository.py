from app.models import Product
from app.config.database import db

class ProductRepository():
    def __init__(self):
        self.__model = Product

    '''
    Devuelve todos los objetos de la Base de Datos
    '''
    def find_all(self) -> Product:
        return db.session.query(self.__model).all()

    '''
    Devuelve el objeto con el id específico
    '''
    def find_by_id(self, id: str) -> Product:
        return db.session.query(self.__model).filter(self.__model.id == id).first()
    
    '''
    Devuelve los objetos con el nombre solictado
    '''
    def find_by_name(self, name: str) -> list:
        return db.session.query(self.__model).filter(self.__model.name.ilike(f'%{name}%')).all()
    

    def find_by_bar_code(self, bar_code: str) -> list:
        return db.session.query(self.__model).filter(self.__model.bar_code == bar_code).first()