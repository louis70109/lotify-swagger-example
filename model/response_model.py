from flask_restful_swagger_2 import Schema
from swagger_model._response_attachment_model import (
    Firmware,
    Part,
    PartSpec,
    Customer,
    QwicBikeModel,
    CreateBike,
    FirmwareFile,
    BikeBundle
)


class QueryFirmwareResponseBody(Schema):
    type = 'object'
    properties = {
        'result': {
            "type": 'array',
            'items': Firmware
        }
    }


class PartResponseBody(Schema):
    type = 'object'
    properties = {'result': Part}


class PartSpecResponseBody(Schema):
    type = 'object'
    properties = {'result': PartSpec}


class CustomerResponseBody(Schema):
    type = 'object'
    properties = {'result': Customer}


class QwicBikeModelResponse(Schema):
    type = 'object'
    properties = {'result': QwicBikeModel}


class CreateBikeResponse(Schema):
    type = 'object'
    properties = {'result': CreateBike}


class CreateQwicBikeResponse(Schema):
    type = 'object'
    properties = {'result': CreateBike}


class CompareQwicBikeResponse(Schema):
    type = 'object'
    properties = {
        'result': {
            'type': 'object',
            'properties': {
               'compare_type': {'type': 'string'},
            }
        }
    }


class MessageGatewayResponse(Schema):
    type = 'object'
    properties = {
        'result': {
            'type': 'object',
            'properties': {
                'NewVersion': {'type': 'string'},
                'DownloadUrl': {'type': 'string'}
            }
        }
    }


class GetFirmwareFileResponse(Schema):
    type = 'object'
    properties = {
        'result': {
            "type": 'array',
            'items': FirmwareFile
        }
    }


class QueryBikeBundleResponse(Schema):
    type = 'object'
    properties = {
        'result': {
            "type": 'array',
            'items': BikeBundle
        }
    }
