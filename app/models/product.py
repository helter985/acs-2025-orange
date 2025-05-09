from app.config.database import db
from dataclasses import dataclass

@dataclass
class Product(db.Model):
    id:int = db.Column('id', db.Integer, primary_key=True,)
    name:str = db.Column('name', db.String(256))
    bar_code: str = db.Column('bar_code', db.String(256))
    price:float = db.Column('price', db.Float(256))
    
