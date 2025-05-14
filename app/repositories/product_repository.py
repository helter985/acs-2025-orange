from app.models import Product
from app.config.database import db
<<<<<<< HEAD
=======
from .CRUD import Create, Read, Update, Delete
>>>>>>> 91fc2916beaff86ea968b9e4c40f74de13d03385

class ProductRepository():
    def __init__(self):
        self.__model = Product

<<<<<<< HEAD
=======



>>>>>>> 91fc2916beaff86ea968b9e4c40f74de13d03385
    '''
    Devuelve todos los objetos de la Base de Datos
    '''
    def find_all(self) -> Product:
        return db.session.query(self.__model).all()

    '''
    Devuelve el objeto con el id específico
    '''
    def find_by_id(self, id: str) -> Product:
<<<<<<< HEAD
        return db.session.query(self.__model).filter(self.__model.id == id).first()
=======
        return db.session.query(self.__model).filter(self.__model.id == id).one()
>>>>>>> 91fc2916beaff86ea968b9e4c40f74de13d03385
    
    '''
    Devuelve los objetos con el nombre solictado
    '''
    def find_by_name(self, name: str) -> list:
<<<<<<< HEAD
        return db.session.query(self.__model).filter(self.__model.name.ilike(f'%{name}%')).all()
    

    def find_by_bar_code(self, bar_code: str) -> list:
        return db.session.query(self.__model).filter(self.__model.bar_code == bar_code).first()
=======
        return db.session.query(self.__model).filter(self.__model.name.like(name)).all()
    

    def find_by_bar_code(self, bar_code: str) -> list:
        return db.session.query(self.__model).filter(self.__model.bar_code == bar_code).one()
>>>>>>> 91fc2916beaff86ea968b9e4c40f74de13d03385
