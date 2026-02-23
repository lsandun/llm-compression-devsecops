# Secure CI/CD Pipeline for ML/LLM API

## Overview

Welcome to the **Secure CI/CD Pipeline for ML/LLM API**! This is a DevSecOps portfolio project demonstrating a fully automated CI/CD pipeline for a secure backend FastAPI application. This project illustrates the principles of "shift-left" security, automated testing, and scalable container orchestration in a modern GitOps workflow.

## Application Logic (Mock LLM Compression)

This FastAPI application provides a single REST endpoint (`/compress`) that simulates Large Language Model (LLM) token reduction techniques. 

To mimic compression, the pipeline takes an input JSON string and programmatically removes all vowels (`a, e, i, o, u`). It then returns a JSON response containing:
1. The compressed text.
2. The original length of the text.
3. The compressed length of the text.

This lightweight logic serves as the foundation for the automated testing and deployment steps.

## DevSecOps Pipeline Architecture

This project utilizes GitHub Actions to orchestrate a secure, automated CI/CD pipeline. The pipeline executes the following checks on every push to the `main` branch:

1. **SAST Scan (Static Application Security Testing)**: 
   Uses **Bandit** to scan the Python source code (`main.py`) for common security issues and code vulnerabilities before any software is built.
   
2. **Automated Unit Testing**: 
   Uses **pytest** and **httpx** to execute automated unit tests (`test_main.py`), verifying the integrity and correctness of the underlying mock LLM compression logic. The pipeline will fail if these tests do not pass.

3. **Secure Containerization**: 
   Builds a highly secure Docker image using a lightweight base image (`python:3.9-slim`). The Dockerfile configuration enforces the principle of least privilege by creating and executing the application under a non-root user account (`appuser`).
   
4. **Container Security Scan**: 
   Uses **Trivy** to perform a comprehensive vulnerability scan on the built Docker image. It checks for both OS-level and library-level vulnerabilities, enforcing shift-left security by identifying risks prior to deployment.

## Kubernetes Deployment

To demonstrate scalable and highly available deployment strategies, this project includes Kubernetes (K8s) manifests located in the `/k8s` directory: 

- `deployment.yaml`: Defines a Kubernetes Deployment set to maintain **3 replicas** of the application, ensuring high availability and load balancing. It utilizes the locally built image (`imagePullPolicy: IfNotPresent`).
- `service.yaml`: Defines a Kubernetes `ClusterIP` Service to route internal network traffic from port 80 to target port 8000 on the application pods.

---

### Author
**S.M.L.S. Aberathna**  
Computer Science (SEU/IS/20/PS/034)  
*South Eastern University of Sri Lanka*
