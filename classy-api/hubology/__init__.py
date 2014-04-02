from __future__ import absolute_import
import uuid

from flask import Flask, Blueprint, g

app = Flask(__name__)
# http://flask.pocoo.org/docs/config/
app.config['DEBUG'] = True


from hubology.views.v1 import api_views as v1_api_views
from hubology.views.v2 import api_views as v2_api_views

api_v1_blueprint = Blueprint('api-v1', __name__)

for view in v1_api_views:
    view.register(api_v1_blueprint)

api_v2_blueprint = Blueprint('api-v2', __name__)

for view in v2_api_views:
    view.register(api_v2_blueprint)


@api_v1_blueprint.before_request
def before_request():
    g.request_id = uuid.uuid4().hex


@api_v2_blueprint.before_request
def before_request():
    g.request_id = uuid.uuid4().hex

app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')
app.register_blueprint(api_v2_blueprint, url_prefix='/api/v2')
