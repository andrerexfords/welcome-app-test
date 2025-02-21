# Welcome App Test Solution

This repository contains a complete solution for the technical test, implementing a simple web application with Docker containerization, Kubernetes deployment, and GitHub Actions CI/CD pipeline.

## Project Structure

```
welcome-app/
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker image definition
├── docker-compose.yaml       # Docker Compose configuration
├── .github/
│   └── workflows/
│       └── build-deploy.yml  # GitHub Actions workflow
├── k8s/
│   ├── configmap-secret.yaml # Kubernetes ConfigMap and Secret
│   ├── deployment.yaml       # Kubernetes Deployment
│   ├── service.yaml          # Kubernetes Service
│   ├── ingress.yaml          # Kubernetes Ingress
│   └── ingress-tls.yaml      # Kubernetes Ingress with TLS
└── gcp/
    ├── README.md             # GCP architecture documentation
    └── architecture.svg      # GCP architecture diagram
```

## 1. Simple Coding

A Flask application that implements the `/welcome/{nama}` route. If a name is provided, it displays "Selamat datang {nama}", otherwise it shows "Anonymous".

### Running Locally

```bash
pip install -r requirements.txt
python app.py
```

Access the application at http://localhost:5000/welcome/yourname

## 2. Container - Docker

### A. Docker Image

Build the Docker image:
```bash
docker build -t testing/welcome .
```

Run the container:
```bash
docker run -d -p 8000:5000 testing/welcome
```

### B. Docker Compose

Run using Docker Compose:
```bash
docker-compose up -d
```

Access the application at http://localhost:8000/welcome/yourname

## 3. CI/CD - GitHub Actions

The GitHub Actions workflow in `.github/workflows/build-deploy.yml` performs:
- Building the Docker image with both latest and version tags
- Pushing the image to Docker Hub
- Creating a GitHub release
- Deploying to a VM via SSH (bonus)

To use the workflow:
1. Add the following secrets to your GitHub repository:
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`
   - `SSH_HOST`
   - `SSH_USERNAME`
   - `SSH_PRIVATE_KEY`
2. Trigger the workflow manually, providing a release tag (e.g., v1.0.0)

## 4. Kubernetes

Kubernetes manifests are in the `k8s/` directory:
- ConfigMap and Secret for configuration
- Deployment for running the application
- Service for internal access
- Ingress for external access
- TLS-enabled Ingress with Let's Encrypt (bonus)

### Applying to a Kubernetes Cluster

```bash
kubectl apply -f k8s/configmap-secret.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
# For TLS:
kubectl apply -f k8s/ingress-tls.yaml
```

## 5. Cloud Infra - GCP

The GCP architecture for deploying this application is documented in `gcp/README.md` with a visual diagram in `gcp/architecture.svg`.

Key components:
- VPC Network with Cloud Load Balancer
- GKE Cluster with separate node pools
- Artifact Registry for container images
- Cloud SQL for database
- Secret Manager for sensitive data
