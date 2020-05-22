import os

from flask import request
from flask_restful_swagger_2 import Resource, swagger
from lotify.client import Client

from model.request_model import ImageUrlRequestBody, StickerRequestBody, TextRequestBody
from model.response_model import NotifyResponse

CLIENT_ID = os.getenv('LINE_NOTIFY_CLIENT_ID')
SECRET = os.getenv('LINE_NOTIFY_CLIENT_SECRET')
URI = os.getenv('LINE_NOTIFY_REDIRECT_URI')

"""
If your keys are 

LINE_NOTIFY_CLIENT_ID, LINE_NOTIFY_CLIENT_SECRET, LINE_NOTIFY_REDIRECT_URI

you can drop them in Client() cause they are default environment name.
"""
lotify = Client(client_id=CLIENT_ID, client_secret=SECRET, redirect_uri=URI)


class TextController(Resource):
    @swagger.doc({
        'tags': ['Text'],
        'description': 'Send LINE Noitfy text message',
        'operationId': 'sendText',
        'parameters': [{
            'name': 'body',
            'description': 'Send LINE Noitfy text message',
            'in': 'body',
            'schema': TextRequestBody,
            'required': True
        }],
        'responses': {
            '200': {
                'description': 'Text message',
                'schema': NotifyResponse,
                'examples': {
                    'application/json': {'status': 200, 'message': 'ok'}
                }
            }
        }
    })
    def post(self):
        payload = request.get_json()
        response = lotify.send_message(
            access_token=payload.get('token'),
            message=payload.get('message')
        )
        return response


class StickerController(Resource):
    @swagger.doc({
        'tags': ['Text'],
        'description': 'Send LINE Noitfy text message',
        'operationId': 'sendText',
        'parameters': [{
            'name': 'body',
            'description': 'Send LINE Noitfy text message',
            'in': 'body',
            'schema': StickerRequestBody,
            'required': True
        }],
        'responses': {
            '200': {
                'description': 'Text message',
                'schema': NotifyResponse,
                'examples': {
                    'application/json': {'status': 200, 'message': 'ok'}
                }
            }
        }
    })
    def post(self):
        payload = request.get_json()
        response = lotify.send_message_with_sticker(
            access_token=payload.get('token'),
            message=payload.get('message'),
            sticker_id=payload.get('sticker_id'),
            sticker_package_id=payload.get('package_id')
        )
        return response


class ImageUrlController(Resource):
    @swagger.doc({
        'tags': ['Text'],
        'description': 'Send LINE Noitfy text message',
        'operationId': 'sendText',
        'parameters': [{
            'name': 'body',
            'description': 'Send LINE Noitfy text message',
            'in': 'body',
            'schema': ImageUrlRequestBody,
            'required': True
        }],
        'responses': {
            '200': {
                'description': 'Text message',
                'schema': NotifyResponse,
                'examples': {
                    'application/json': {'status': 200, 'message': 'ok'}
                }
            }
        }
    })
    def post(self):
        payload = request.get_json()
        response = lotify.send_message_with_image_url(
            access_token=payload.get('token'),
            message=payload.get('message'),
            image_fullsize=payload.get('url'),
            image_thumbnail=payload.get('url')
        )
        return response


class ImageFileController(Resource):
    @swagger.doc({
        'tags': ['Text'],
        'description': 'Send LINE Noitfy text message',
        'operationId': 'sendText',
        'parameters': [{
            'name': 'file',
            'description': 'Upload file',
            'in': 'formData',
            'type': 'file',
            'required': True
        }, {
            'name': 'message',
            'description': 'Send LINE Noitfy text message',
            'in': 'formData',
            'type': 'string',
            'required': True
        }, {
            'name': 'token',
            'description': 'LINE Notify access token',
            'in': 'formData',
            'type': 'string',
            'required': True
        }],
        'responses': {
            '200': {
                'description': 'Text message',
                'schema': NotifyResponse,
                'examples': {
                    'application/json': {'status': 200, 'message': 'ok'}
                }
            }
        }
    })
    def post(self):
        file = request.files.get('file')
        token = request.form.get('token')
        message = request.form.get('message')
        response = lotify.send_message_with_image_file(
            access_token=token,
            message=message,
            file=file
        )
        return response
