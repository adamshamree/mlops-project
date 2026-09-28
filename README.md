# Fraud Detector — MLOps Pipeline

End-to-end MLOps pipeline simulating a real-world DevOps engineering
environment. Built as a hands-on learning project covering the full
deployment lifecycle from containerisation to cloud infrastructure.

## Architecture

## Tech Stack

| Layer | Tools |
|-------|-------|
| Containerisation | Docker |
| Orchestration | Kubernetes (3 replicas, self-healing, rolling updates) |
| Package Management | Helm Charts |
| CI/CD | GitHub Actions, GitOps |
| Experiment Tracking | MLflow |
| Infrastructure as Code | Terraform (EKS, S3, ECR) |

## Project Structure

## Quick Start

```bash
# Build and run with Docker
docker build -t fraud-detector ./docker
docker run -p 5000:5000 fraud-detector

# Deploy to Kubernetes
kubectl apply -f kubernetes/

# Deploy with Helm
helm install fraud-detector ./fraud-detector-chart
