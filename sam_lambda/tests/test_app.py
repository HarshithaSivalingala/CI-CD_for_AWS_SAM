import json
from app import lambda_handler

def test_lambda_handler():
    event = {
        "httpMethod": "GET",
        "path": "/contact"
    }
    response = lambda_handler(event, None)
    assert response["statusCode"] == 200
    assert "form" in json.loads(response["body"])
