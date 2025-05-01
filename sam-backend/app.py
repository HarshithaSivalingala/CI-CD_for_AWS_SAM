# lambda/app.py
import json
import re
from datetime import datetime

# CORS headers
BASE_HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
}

def lambda_handler(event, context):
    try:
        http_method = event.get('httpMethod', 'GET')
        
        # Handle OPTIONS request for CORS preflight
        if http_method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': BASE_HEADERS,
                'body': json.dumps({'message': 'CORS preflight success'})
            }
        
        # GET request - Return form structure
        elif http_method == 'GET':
            return {
                'statusCode': 200,
                'headers': {
                    **BASE_HEADERS,
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'form': {
                        'title': 'Contact Us',
                        'description': 'Please fill out this form and we will get back to you shortly.',
                        'fields': [
                            {
                                'name': 'name',
                                'type': 'text',
                                'label': 'Full Name',
                                'required': True,
                                'placeholder': 'John Doe'
                            },
                            {
                                'name': 'email',
                                'type': 'email',
                                'label': 'Email Address',
                                'required': True,
                                'placeholder': 'john@example.com'
                            },
                            {
                                'name': 'phone',
                                'type': 'tel',
                                'label': 'Phone Number',
                                'required': False,
                                'placeholder': '(123) 456-7890'
                            },
                            {
                                'name': 'message',
                                'type': 'textarea',
                                'label': 'Your Message',
                                'required': True,
                                'placeholder': 'How can we help you?'
                            }
                        ]
                    }
                })
            }
        
        # POST request - Process form submission
        elif http_method == 'POST':
            # Parse request body
            try:
                body = json.loads(event.get('body', '{}'))
            except json.JSONDecodeError:
                return {
                    'statusCode': 400,
                    'headers': {
                        **BASE_HEADERS,
                        'Content-Type': 'application/json'
                    },
                    'body': json.dumps({
                        'success': False,
                        'error': 'Invalid JSON format'
                    })
                }
            
            # Validate required fields
            required_fields = ['name', 'email', 'message']
            missing_fields = [field for field in required_fields if not body.get(field)]
            
            if missing_fields:
                return {
                    'statusCode': 400,
                    'headers': {
                        **BASE_HEADERS,
                        'Content-Type': 'application/json'
                    },
                    'body': json.dumps({
                        'success': False,
                        'error': f'Missing required fields: {", ".join(missing_fields)}'
                    })
                }
            
            # Validate email format
            email = body.get('email', '')
            if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                return {
                    'statusCode': 400,
                    'headers': {
                        **BASE_HEADERS,
                        'Content-Type': 'application/json'
                    },
                    'body': json.dumps({
                        'success': False,
                        'error': 'Invalid email format'
                    })
                }
            
            # Process the form data (in a real app, you might save to a database)
            submission = {
                'timestamp': datetime.utcnow().isoformat(),
                'name': body.get('name'),
                'email': body.get('email'),
                'phone': body.get('phone', ''),
                'message': body.get('message')
            }
            
            # Log the submission (in production, you'd save to a database)
            print(f"Form submission received: {json.dumps(submission)}")
            
            # Return success response
            return {
                'statusCode': 200,
                'headers': {
                    **BASE_HEADERS,
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'success': True,
                    'message': 'Thank you for your submission!',
                    'data': {
                        'reference_id': f"ref-{datetime.utcnow().timestamp():.0f}"
                    }
                })
            }
        
        else:
            return {
                'statusCode': 405,
                'headers': BASE_HEADERS,
                'body': json.dumps({
                    'success': False,
                    'error': 'Method not allowed'
                })
            }
    
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': BASE_HEADERS,
            'body': json.dumps({
                'success': False,
                'error': 'Internal server error'
            })
        }