
# CI/CD for AWS Serverless Applications

This project demonstrates three CI/CD approaches to deploying AWS Serverless applications using:

- **Terraform**
- **AWS SAM (Serverless Application Model)**
- **Serverless Framework**

Each setup integrates **GitHub Actions** for CI/CD automation and includes a React frontend connected to a Lambda backend via API Gateway.

---

##  Branch Overview

| Branch                  | Stack Used                | Description                                                   |
|-------------------------|---------------------------|---------------------------------------------------------------|
| `main`                  | Terraform                 | Infra setup using Terraform for Lambda, API Gateway, S3, etc. |
| `aws-sam`               | AWS SAM                   | SAM template-based CI/CD for Lambda and API Gateway           |
| `serverless-framework`  | Serverless Framework      | Deploys using `serverless.yml` and GitHub Actions             |

---

## Project Structure

```plaintext
.github/workflows/        # GitHub Actions CI/CD pipelines
lambda-react-frontend/    # React app frontend (deployed via S3/CloudFront)
lambda/ or sam-backend/   # Lambda function code (Node.js/Python)
terraform/                # Terraform modules (main branch only)
sam-template.yaml         # SAM template (aws-sam branch)
serverless.yml            # Serverless Framework config (serverless-framework branch)
```

---

## Features

- Infrastructure as Code with **Terraform / SAM / Serverless Framework**
- CI/CD automation using **GitHub Actions**
- REST API setup using **API Gateway**
- Backend logic in **AWS Lambda**
- Frontend in **React**, deployed to **S3/CloudFront**

---

## How to Deploy

### 1. Terraform (main branch)

```bash
cd terraform
terraform init
terraform apply
```

### 2. AWS SAM (aws-sam branch)

```bash
sam build
sam deploy --guided
```

### 3. Serverless Framework (serverless-framework branch)

```bash
npm install -g serverless
sls deploy
```

---

## Security & Quality

- Static code analysis with `tfsec`, `Checkov`
- Secure IAM policies via templates and Terraform modules
- Secrets stored using **AWS Secrets Manager** or **SSM Parameter Store**

---

## Monitoring & Observability

- **CloudWatch Alarms** for Lambda errors, throttles, and latency
- Logs routed to **CloudWatch Logs**
- CI/CD pipeline metrics tracked via GitHub Actions

---

## Sample Flow (Frontend to Lambda)

1. React app submits a form (`POST /submit`)
2. API Gateway routes the request to Lambda
3. Lambda processes input (e.g., store in DynamoDB, send SNS)
4. Response returned to the React frontend

---

## Contributors

- **Sai Harshitha Sivalingala**  
- **Toral Chauhan**  
- **Shalini Mutyala**

---

## License

This project is open-source and available 
