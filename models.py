from flask_pymongo import PyMongo
from marshmallow import Schema, fields

mongo = PyMongo()

class WebtoonSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    characters = fields.List(fields.Str(), required=True)
