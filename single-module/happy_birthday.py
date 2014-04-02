import json

from flask import Flask, Response, jsonify, request

app = Flask(__name__)
# http://flask.pocoo.org/docs/config/
app.config['DEBUG'] = True


@app.route('/happy/birthday/flask')
def happy_birthday():
    return "Happy Birthday, Flask"


@app.route('/happy/birthday/flask.json')
def happy_birthday_json():
    return Response(json.dumps({"happy": {"birthday": "Flask"}, "request_args": request.args}),
                    mimetype="application/json")


@app.route('/v2/happy/birthday/flask.json', methods=['GET', 'POST'])
def happy_birthday_json_v2():
    return jsonify({
        "happy": {
            "birthday": "Flask"
        },
        "request_args": request.args,
        "request_form": request.form,
        "request_values": request.values,
        "request_headers": dict(request.headers),
        "request_url": request.url,
    })


@app.route('/json/echo', methods=['POST'])
def json_echo():
    return jsonify({
        "happy": {
            "birthday": "Flask"
        },
        "echo": request.json,
    })


@app.route('/happy/birthday/flask.xml')
def happy_birthday_xml():
    return Response("<happy><birthday>Flask</birthday></happy>", mimetype="application/xml")

if __name__ == "__main__":
    app.run()