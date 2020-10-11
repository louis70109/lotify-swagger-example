import os

from flask import Flask
from flask_cors import CORS
from flask_restful_swagger_2 import Api

from controller.authorizer_controller import RootController, CallbackController, RevokeTokenController, LinkController, \
    CodeChangeController
from controller.event_controller import TextController, StickerController, ImageUrlController, ImageFileController

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*", "supports_credentials": True}})

DOMAIN = os.environ.get('DOMAIN_NAME')
PORT = os.environ.get('PORT')


def is_local():
    return True if os.environ.get('LOCAL') else False


api = Api(app,
          host=f'localhost:{PORT}' if is_local else DOMAIN,
          schemes=['http' if is_local else 'https'],
          base_path='/',
          api_version='0.0.1',
          api_spec_url='/api/swagger')

api.add_resource(RootController, "/")
api.add_resource(CallbackController, "/callback")
api.add_resource(LinkController, "/notify/link")
api.add_resource(CodeChangeController, "/notify/change")
api.add_resource(RevokeTokenController, "/notify/revoke")
api.add_resource(TextController, "/notify/send")
api.add_resource(StickerController, "/notify/sticker")
api.add_resource(ImageUrlController, "/notify/url")
api.add_resource(ImageFileController, "/notify/file")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
