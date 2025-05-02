import os
import sys
import json
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import lambda_handler

class TestLambdaHandler(unittest.TestCase):

    def test_get_request(self):
        event = {
            "httpMethod": "GET"
        }
        context = {}
        response = lambda_handler(event, context)

        self.assertEqual(response["statusCode"], 200)
        self.assertIn("form", json.loads(response["body"]))
        self.assertEqual(response["headers"]["Content-Type"], "application/json")

    def test_post_request_success(self):
        event = {
            "httpMethod": "POST",
            "body": json.dumps({
                "name": "John Doe",
                "email": "john@example.com",
                "phone": "123-456-7890",
                "message": "Hello!"
            })
        }
        context = {}
        response = lambda_handler(event, context)

        self.assertEqual(response["statusCode"], 200)
        body = json.loads(response["body"])
        self.assertEqual(body["status"], "success")
        self.assertIn("Thanks John Doe", body["message"])

    def test_post_request_missing_body(self):
        event = {
            "httpMethod": "POST",
            "body": None
        }
        context = {}
        response = lambda_handler(event, context)

        self.assertEqual(response["statusCode"], 200)
        body = json.loads(response["body"])
        self.assertEqual(body["status"], "success")
        self.assertIn("Anonymous", body["message"])

    def test_post_request_invalid_body(self):
        event = {
            "httpMethod": "POST",
            "body": "invalid json"
        }
        context = {}
        response = lambda_handler(event, context)

        self.assertEqual(response["statusCode"], 400)
        body = json.loads(response["body"])
        self.assertIn("Failed to process request", body["error"])

    def test_unsupported_method(self):
        event = {
            "httpMethod": "PUT"
        }
        context = {}
        response = lambda_handler(event, context)

        self.assertEqual(response["statusCode"], 405)
        body = json.loads(response["body"])
        self.assertIn("Method PUT not allowed", body["error"])

if __name__ == "__main__":
    unittest.main()