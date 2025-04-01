from marshmallow import fields, Schema # type: ignore


class UserSchema(Schema):
    id = fields.String()
    username = fields.String()
    email = fields.String()