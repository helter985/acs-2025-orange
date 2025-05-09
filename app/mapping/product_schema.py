from app.models.product import Product
from marshmallow import validate, fields, Schema, post_load

class ProductSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=105))
    bar_code =fields.String(required=True, validate=validate.Length(min=1, max=105))
    price = fields.Float(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return Product(**data)