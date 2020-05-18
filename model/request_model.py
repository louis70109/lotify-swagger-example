from flask_restful_swagger_2 import Schema


class PartRequestBody(Schema):
    type = 'object'
    properties = {
        'part_num': {
            'type': 'string'
        },
        'barcode': {
            'type': 'string'
        },
        'fw_ver': {
            'type': 'string'
        }
    }
    required = ['part_num', 'barcode', 'fw_ver']


class PartMeta(Schema):
    type = 'object'
    properties = {
        'mid': {'type': 'string'},
        'part_num': {'type': 'string'},
    }


class CreateBikeRequestBody(Schema):
    type = 'object'
    properties = {
        'vin': {'type': 'string'},
        'spec_id': {'type': 'integer'},
        'parts': {
            'type': 'array',
            'items': PartMeta
        }
    }
    required = ['vin', 'spec_id', 'parts']


class CompareBikeRequestBody(Schema):
    type = 'object'
    properties = {
        'vin': {'type': 'string'},
        'parts': {
            'type': 'array',
            'items': PartMeta
        }
    }
    required = ['vin', 'parts']
