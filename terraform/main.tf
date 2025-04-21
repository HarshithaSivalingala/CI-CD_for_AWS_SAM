provider "aws" {
  region = "us-east-2"  # or your preferred region
}

resource "aws_api_gateway_rest_api" "contact_form_api" {
  name        = "ContactFormAPI"
  description = "API for Contact Form submissions"
}

resource "aws_api_gateway_resource" "contact_resource" {
  rest_api_id = aws_api_gateway_rest_api.contact_form_api.id
  parent_id   = aws_api_gateway_rest_api.contact_form_api.root_resource_id
  path_part   = "contact"
}

resource "aws_api_gateway_method" "contact_options" {
  rest_api_id   = aws_api_gateway_rest_api.contact_form_api.id
  resource_id   = aws_api_gateway_resource.contact_resource.id
  http_method   = "OPTIONS"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "contact_get" {
  rest_api_id   = aws_api_gateway_rest_api.contact_form_api.id
  resource_id   = aws_api_gateway_resource.contact_resource.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "contact_post" {
  rest_api_id   = aws_api_gateway_rest_api.contact_form_api.id
  resource_id   = aws_api_gateway_resource.contact_resource.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda_integration_options" {
  rest_api_id = aws_api_gateway_rest_api.contact_form_api.id
  resource_id = aws_api_gateway_resource.contact_resource.id
  http_method = aws_api_gateway_method.contact_options.http_method
  type        = "MOCK"
  
  request_templates = {
    "application/json" = jsonencode({
      statusCode = 200
    })
  }
}

# GET Method Integration
resource "aws_api_gateway_integration" "lambda_integration_get" {
  rest_api_id = aws_api_gateway_rest_api.contact_form_api.id
  resource_id = aws_api_gateway_resource.contact_resource.id
  http_method = aws_api_gateway_method.contact_get.http_method
  
  integration_http_method = "POST"
  type                   = "AWS_PROXY"
  uri                    = aws_lambda_function.example.invoke_arn
}

# POST Method Integration
resource "aws_api_gateway_integration" "lambda_integration_post" {
  rest_api_id = aws_api_gateway_rest_api.contact_form_api.id
  resource_id = aws_api_gateway_resource.contact_resource.id
  http_method = aws_api_gateway_method.contact_post.http_method
  
  integration_http_method = "POST"
  type                   = "AWS_PROXY"
  uri                    = aws_lambda_function.example.invoke_arn
}

resource "aws_api_gateway_method_response" "options_200" {
  rest_api_id = aws_api_gateway_rest_api.contact_form_api.id
  resource_id = aws_api_gateway_resource.contact_resource.id
  http_method = aws_api_gateway_method.contact_options.http_method
  status_code = "200"
  
  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = true,
    "method.response.header.Access-Control-Allow-Methods" = true,
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}

# GET Method Response
resource "aws_api_gateway_method_response" "get_200" {
  rest_api_id = aws_api_gateway_rest_api.contact_form_api.id
  resource_id = aws_api_gateway_resource.contact_resource.id
  http_method = aws_api_gateway_method.contact_get.http_method
  status_code = "200"
  
  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = true
  }
}

# POST Method Response
resource "aws_api_gateway_method_response" "post_200" {
  rest_api_id = aws_api_gateway_rest_api.contact_form_api.id
  resource_id = aws_api_gateway_resource.contact_resource.id
  http_method = aws_api_gateway_method.contact_post.http_method
  status_code = "200"
  
  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = true
  }
}

resource "aws_api_gateway_integration_response" "options_integration_response" {
  rest_api_id = aws_api_gateway_rest_api.contact_form_api.id
  resource_id = aws_api_gateway_resource.contact_resource.id
  http_method = aws_api_gateway_method.contact_options.http_method
  status_code = aws_api_gateway_method_response.options_200.status_code
  
  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
    "method.response.header.Access-Control-Allow-Methods" = "'OPTIONS,GET,POST'",
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }
}
resource "aws_api_gateway_deployment" "api_deployment" {
  depends_on = [
    aws_api_gateway_integration.lambda_integration_get,
    aws_api_gateway_integration.lambda_integration_post
  ]

  rest_api_id = aws_api_gateway_rest_api.contact_form_api.id
}

resource "aws_api_gateway_stage" "prod" {
  stage_name    = "prod"
  rest_api_id   = aws_api_gateway_rest_api.contact_form_api.id
  deployment_id = aws_api_gateway_deployment.api_deployment.id
}

resource "aws_lambda_permission" "api_gateway_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.example.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.contact_form_api.execution_arn}/*/*/*"
}

resource "aws_lambda_function" "example" {
  function_name    = var.lambda_function_name
  handler          = var.lambda_handler
  runtime          = var.lambda_runtime
  filename         = var.lambda_zip_path
  source_code_hash = filebase64sha256(var.lambda_zip_path)
  role             = aws_iam_role.lambda_exec.arn
}

resource "aws_iam_role" "lambda_exec" {
  name = "${var.lambda_function_name}-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}