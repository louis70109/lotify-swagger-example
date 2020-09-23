import os

from flask import Flask
from flask_cors import CORS
from flask_restful_swagger_2 import Api

from controller.authorizer_controller import RootController, CallbackController, RevokeTokenController
from controller.event_controller import TextController, StickerController, ImageUrlController, ImageFileController

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*", "supports_credentials": True}})

local = os.environ.get('IS_OFFLINE')


def is_local():
    return True if local else False


# https://github.com/swagger-api/swagger-codegen/issues/7847#issuecomment-374512375
api = Api(app,
          host='localhost:5000' if local else '0.0.0.0:5000',
          schemes=['http' if local else 'https'],
          base_path='/',
          api_version='0.0.1',
          api_spec_url='/api/swagger')
api.add_resource(RootController, "/")
api.add_resource(CallbackController, "/callback")
api.add_resource(RevokeTokenController, "/notify/revoke")
api.add_resource(TextController, "/notify/send")
api.add_resource(StickerController, "/notify/sticker")
api.add_resource(ImageUrlController, "/notify/url")
api.add_resource(ImageFileController, "/notify/file")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
