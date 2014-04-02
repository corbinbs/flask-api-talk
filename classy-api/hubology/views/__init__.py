from functools import wraps
import json
from flask import jsonify, make_response
from flask.ext.classy import FlaskView


def render_json(func):
    @wraps(func)
    def render_json_function(*args, **kwargs):
        data = func(*args, **kwargs)
        resp = make_response(json.dumps(data, indent=4, sort_keys=True))
        resp.headers['mimetype'] = 'application/json'
        return resp

    return render_json_function


class FlaskAPI(FlaskView):
    """
    Base API class
    """
    decorators = [render_json]
