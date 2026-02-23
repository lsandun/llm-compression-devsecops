# Secure CI/CD Pipeline for ML/LLM API

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

![Architecture Diagram](https://via.placeholder.com/800x400?text=DevSecOps+Pipeline+Architecture)

## Overview

Welcome to the **Secure CI/CD Pipeline for ML/LLM API**! This is a comprehensive DevSecOps portfolio project demonstrating a fully automated CI/CD pipeline for a robust FastAPI backend. It emphasizes "shift-left" security practices and utilizes Kubernetes orchestration for highly available, scalable deployments.

## Technologies Used

*   **Python (FastAPI)**: High-performance backend framework for the Mock API.
*   **Docker**: Containerization ensuring consistent environments.
*   **GitHub Actions**: Automated CI/CD orchestrator.
*   **Kubernetes (kind)**: Local cluster orchestration and scalable deployments.
*   **Bandit (SAST)**: Static application security testing for Python code.
*   **Trivy (Container Scanning)**: Vulnerability scanning for OS and dependencies.
*   **Pytest**: Automated unit testing framework.

## Two-Tier Security Architecture (Shift-Left)

This pipeline integrates security deeply into the development lifecycle through two distinct automated gates:

1.  **Level 1: Code Security (SAST)**: Using **Bandit** to preemptively scan the raw Python source code for security vulnerabilities (e.g., unsafe host bindings, hardcoded passwords) before any build step is executed. This enforces secure coding standards early in the deployment lifecycle.
2.  **Level 2: Container Security**: Using **Trivy** to conduct extensive vulnerability scanning on the fully built Docker image. This crucial step detects hidden OS-level and library-related vulnerabilities prior to deployment into production-like environments.

## Application Logic

The core application provides a Mock LLM Compression API via the `/compress` POST endpoint. To simulate the concept of token reduction common in LLM architectures, the backend receives a JSON string, programmatically strips all vowels (`a, e, i, o, u`), and returns the tightly compressed text along with original and compressed string lengths. 

## How to Run Locally (GitHub Codespaces / Linux)

Follow these exact steps to run the comprehensive DevSecOps pipeline architecture locally using `kind` (Kubernetes IN Docker):

1.  **Install `kind` and create a cluster**:
    ```bash
    kind create cluster --name devsecops-cluster
    ```
2.  **Build the Docker image**:
    ```bash
    docker build -t llm-compression-api:latest .
    ```
3.  **Load the image into your kind cluster**:
    ```bash
    kind load docker-image llm-compression-api:latest --name devsecops-cluster
    ```
4.  **Apply the Kubernetes deployment and service manifests**:
    ```bash
    kubectl apply -f k8s/
    ```
5.  **Verify that the applications pods are running correctly**:
    ```bash
    kubectl get pods
    ```
6.  **Forward the service port to your local machine**:
    ```bash
    kubectl port-forward svc/llm-compression-service 8000:80
    ```
    *The API will now be securely accessible at `http://localhost:8000`.*

---

### Author
**S.M.L.S. Aberathna**
