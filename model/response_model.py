from flask_restful_swagger_2 import Schema


class NotifyResponse(Schema):
    type = 'object'
    properties = {
        'status': {'type': 'integer'},
        'message': {'type': 'string'}
    }


class LinkResponse(Schema):
    type = 'object'
    properties = {
        'link': {'type': 'string'}
    }


class CodeResponse(Schema):
    type = 'object'
    properties = {
        'token': {'type': 'string'}
    }
