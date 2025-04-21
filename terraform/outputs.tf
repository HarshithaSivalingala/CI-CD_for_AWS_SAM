output "api_gateway_url" {
  description = "The base URL of the API Gateway"
  value       = "https://${aws_api_gateway_rest_api.contact_form_api.id}.execute-api.${var.aws_region}.amazonaws.com/${aws_api_gateway_stage.prod.stage_name}${aws_api_gateway_resource.contact_resource.path}"
}