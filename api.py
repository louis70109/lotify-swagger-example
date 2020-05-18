import os

from flask import Flask
from flask_cors import CORS
from flask_restful_swagger_2 import Api

from controller.authorizer_controller import RootController, CallbackController, RevokeTokenController
from controller.event_controller import TextController, StickerController, ImageUrlController, ImagePathController

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*", "supports_credentials": True}})


def is_local():
    return True if os.environ.get('IS_OFFLINE', None) else False


# https://github.com/swagger-api/swagger-codegen/issues/7847#issuecomment-374512375
api = Api(app,
          host=os.environ.get('API_DOMAIN') if not is_local() else 'localhost:5000',
          schemes=['https'] if not is_local() else ['http'],
          base_path='/',
          api_version='0.0.1',
          api_spec_url='/api/swagger')

api.add_resource(RootController, "/")
api.add_resource(CallbackController, "/callback")
api.add_resource(RevokeTokenController, "/notify/revoke")
api.add_resource(TextController, "/notify/send")
api.add_resource(StickerController, "/notify/sticker")
api.add_resource(ImageUrlController, "/notify/url")
api.add_resource(ImagePathController, "/notify/path")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
