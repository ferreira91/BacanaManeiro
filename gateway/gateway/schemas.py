from marshmallow import Schema, fields, validate


class AddressSchema(Schema):
    street = fields.Str(required=True)
    number = fields.Str(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)
    country_code = fields.Str(required=True)
    postal_code = fields.Str(required=True)


class ContactSchema(Schema):
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True)


class EstablishmentSchema(Schema):
    document = fields.Str(required=True, validate=validate.Length(min=11, max=14))
    name = fields.Str(required=True)
    address = fields.Nested(AddressSchema, many=False)
    contact = fields.Nested(ContactSchema, many=False)
    photo_urls = fields.List(fields.URL(required=True), required=True)


class CreateEstablishmentSchema(EstablishmentSchema):
    password = fields.Str(required=True, load_only=True)


class UpdateEstablishmentPassword(Schema):
    current_password = fields.Str(required=True)
    new_password = fields.Str(required=True)
