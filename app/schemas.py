from flask_restful import fields

product_fields = {
    "nome": fields.String,
    "descricao": fields.String,
    "peso": fields.String,
    "garantia": fields.String,
    "link_descricao": fields.String,
    "fotos": fields.List(fields.String),
    "preco": fields.Float
}