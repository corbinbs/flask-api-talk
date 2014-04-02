from happy_birthday import app
import json


def test_happy_birthday_flask():
    """
        Verify GET /happy/birthday/flask returns the proper response
    """
    with app.test_client() as client:
        response = client.get('/happy/birthday/flask')
        assert response.status_code == 200
        assert response.data == 'Happy Birthday, Flask'


def test_happy_birthday_flask_json():
    """
        Verify GET /happy/birthday/flask.json returns the proper response
    """
    with app.test_client() as client:
        response = client.get('/happy/birthday/flask.json')
        assert response.status_code == 200
        response_json = json.loads(response.data)
        assert response_json['happy'] == {"birthday": "Flask"}
