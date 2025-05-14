from app.config.database import db
<<<<<<< HEAD

class Product(db.Model):
    __tablename__ = 'products'
    
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String(256), nullable=False)
    bar_code:str = db.Column(db.String(256), unique=True, nullable=False)
    price:float = db.Column(db.Float, nullable=False)
=======
from dataclasses import dataclass

@dataclass
class Product(db.Model):
    id:int = db.Column('id', db.Integer, primary_key=True,)
    name:str = db.Column('name', db.String(256))
    bar_code: str = db.Column('bar_code', db.String(256))
    price:float = db.Column('price', db.Float(256))
    
>>>>>>> 91fc2916beaff86ea968b9e4c40f74de13d03385
