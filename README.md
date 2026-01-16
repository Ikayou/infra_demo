infra_demo
Overview

This project is an infrastructure-focused demo application built to practice deploying a containerized web service using Docker and Kubernetes.

It was created as part of my preparation for a full-time infrastructure/Kubernetes-focused role starting in February.

The main goal of this project is not application complexity, but rather learning how to:

Containerize an application using Docker

Run and validate it locally with Docker Compose

Deploy it to a Kubernetes cluster (kind)

Connect it to a PostgreSQL database

Configure services, health checks, and environment variables

Debug common Kubernetes issues (e.g., image pull errors, misconfigurations)

Architecture
Client
  |
  v
Service (Kubernetes)
  |
  v
FastAPI Application (Pod)
  |
  v
PostgreSQL (Pod + PVC)

Tech Stack

FastAPI (Python)

PostgreSQL

Docker

Docker Compose

Kubernetes (kind)

ConfigMap / Secret

PersistentVolumeClaim (PVC)

Features

Simple FastAPI web server

PostgreSQL connectivity check

Health check endpoint for Kubernetes

Dockerized environment

Kubernetes deployment configuration

Environment-based configuration

Endpoints
Endpoint	Description
/	Basic health check
/db	Verifies database connectivity
/healthz	Used for Kubernetes liveness/readiness probes
Local Development (Docker Compose)
Build and start services
docker compose up --build

Access

App: http://localhost:8000

DB check: http://localhost:8000/db

Stop
Ctrl + C


or

docker compose down

Kubernetes Deployment (kind)
1. Create a cluster
kind create cluster

2. Build the application image
docker build -t infra-demo:0.1 -f docker/Dockerfile .

3. Load image into kind
kind load docker-image infra-demo:0.1 --name kind

4. Apply Kubernetes manifests
kubectl apply -f k8s/

5. Check resources
kubectl -n infra-demo get pods,svc

6. Access via port-forward
kubectl -n infra-demo port-forward svc/app 8080:80


Then open:

http://localhost:8080

http://localhost:8080/db

Configuration

This project uses environment variables for configuration.

Example values are provided in .env.example.

Actual secrets and local values should be stored in .env, which is excluded from Git.

Health Checks

Kubernetes health probes are configured:

Readiness Probe: /healthz

Liveness Probe: /healthz

These ensure that Kubernetes can automatically restart unhealthy containers.

Troubleshooting
ImagePullBackOff / ErrImagePull

Make sure the image exists locally:

docker images


And is loaded into kind:

kind load docker-image infra-demo:0.1 --name kind

Pod not starting
kubectl describe pod <pod-name>
kubectl logs <pod-name>

What I Learned

Through this project, I practiced:

Writing Dockerfiles

Building and tagging Docker images

Using Docker Compose for local development

Deploying applications to Kubernetes

Understanding Deployments, Services, ConfigMaps, Secrets, and PVCs

Debugging Kubernetes issues

Managing environment-based configurations

Using health checks for container orchestration

Future Improvements

Add Ingress + TLS

Resource limits (CPU/memory)

Horizontal Pod Autoscaling

CI/CD pipeline

Monitoring (Prometheus, Grafana)

Author

Ikayou

Important Note

This is a learning project.
All credentials and configuration values are for demonstration purposes only.