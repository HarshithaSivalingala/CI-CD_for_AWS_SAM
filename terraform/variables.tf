variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-2"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "contact-form-handler"
}

variable "lambda_handler" {
  description = "Lambda function handler"
  type        = string
  default     = "app.lambda_handler"
}

variable "lambda_runtime" {
  description = "Lambda runtime"
  type        = string
  default     = "python3.9"
}

variable "lambda_zip_path" {
  description = "Path to the Lambda deployment package"
  type        = string
  default     = "../lambda.zip"
}