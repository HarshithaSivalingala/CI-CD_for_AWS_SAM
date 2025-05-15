
# CI/CD for AWS Serverless Applications

This repository demonstrates **CI/CD pipelines** using tools like **Terraform**, **AWS SAM**, and **Serverless Framework**. It also includes a **React frontend** (`react-frontend` branch) that connects to all backend deployments.

Each setup integrates **GitHub Actions** for CI/CD automation and includes a React frontend connected to a Lambda backend via API Gateway.

---

##  Branch Overview

| Branch Name            | Description                                                         |
|------------------------|---------------------------------------------------------------------|
| `terraform`            | Backend deployment using **Terraform**                              |
| `aws-sam`              | Backend deployment using **AWS Serverless Application Model (SAM)** |
| `serverlessframework`  | Backend deployment using **Serverless Framework**                   |
| `react-frontend`       | React app that communicates with all deployed backends              |


---
## React Frontend (`react-frontend` branch)

The `react-frontend` branch contains a **React application** that interacts with backend services deployed via different CI/CD tools. API endpoints are configured via environment variables.

---

## Features

- Infrastructure as Code with **Terraform / SAM / Serverless Framework**
- CI/CD automation using **GitHub Actions**
- REST API setup using **API Gateway**
- Backend logic in **AWS Lambda**
- Frontend in **React**, deployed to **S3/CloudFront**

---

## How to Deploy Each Tool seperately

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

### 4. react-frontend

```bash
npm install
npm start
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
