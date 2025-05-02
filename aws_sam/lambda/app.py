import json

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))  # For debugging

    method = event.get("httpMethod", "GET")

    cors_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }

    if method == "GET":
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps({
                "form": {
                    "title": "Contact Us",
                    "description": "Please fill out this form and we will get back to you shortly.",
                    "fields": [
                        {"name": "name", "type": "text", "label": "Full Name", "required": True, "placeholder": "John Doe"},
                        {"name": "email", "type": "email", "label": "Email Address", "required": True, "placeholder": "john@example.com"},
                        {"name": "phone", "type": "tel", "label": "Phone Number", "required": False, "placeholder": "(123) 456-7890"},
                        {"name": "message", "type": "textarea", "label": "Your Message", "required": True, "placeholder": "How can we help you?"}
                    ]
                }
            })
        }

    elif method == "POST":
        try:
            body = json.loads(event.get("body") or "{}")
            name = body.get("name", "Anonymous")
            email = body.get("email", "")
            phone = body.get("phone", "")
            message = body.get("message", "")

            return {
                "statusCode": 200,
                "headers": cors_headers,
                "body": json.dumps({
                    "status": "success",
                    "message": f"Thanks {name}, we received your message.",
                    "data": body
                })
            }

        except Exception as e:
            return {
                "statusCode": 400,
                "headers": cors_headers,
                "body": json.dumps({
                    "error": f"Failed to process request: {str(e)}"
                })
            }

    else:
        return {
            "statusCode": 405,
            "headers": cors_headers,
            "body": json.dumps({
                "error": f"Method {method} not allowed"
            })
        }
