from flask import Flask, url_for

def test_base_route():
    app = Flask(__name__)
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200

test_base_route()