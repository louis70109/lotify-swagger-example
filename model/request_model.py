from flask_restful_swagger_2 import Schema


class TextRequestBody(Schema):
    type = 'object'
    properties = {
        'token': {
            'type': 'string'
        },
        'message': {
            'type': 'string'
        }
    }
    required = ['token', 'message']


class StickerRequestBody(Schema):
    type = 'object'
    properties = {
        'token': {
            'type': 'string'
        },
        'message': {
            'type': 'string'
        },
        'sticker_id': {
            'type': 'integer'
        },
        'package_id': {
            'type': 'integer'
        }
    }
    required = ['token', 'message', 'sticker_id', 'package_id']


class ImageUrlRequestBody(Schema):
    type = 'object'
    properties = {
        'token': {
            'type': 'string'
        },
        'message': {
            'type': 'string'
        },
        'url': {
            'type': 'integer'
        }
    }
    required = ['token', 'message', 'url']


class ImagePathRequestBody(Schema):
    type = 'object'
    properties = {
        'token': {
            'type': 'string'
        },
        'message': {
            'type': 'string'
        },
        'url': {
            'type': 'integer'
        }
    }
    required = ['token', 'message', 'url']
