from flask_restful_swagger_2 import Schema


class NotifyResponse(Schema):
    type = 'object'
    properties = {
        'status': {'type': 'integer'},
        'message': {'type': 'string'}
    }
