from app.config.database import db

class Product(db.Model):
    __tablename__ = 'products'
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String(256), nullable=False)
    bar_code:str = db.Column(db.String(256), unique=True, nullable=False)
    price:float = db.Column(db.Float, nullable=False)
    
    def __init__(self, name, bar_code, price):
        self.name = name
        self.bar_code = bar_code
        self.price = price