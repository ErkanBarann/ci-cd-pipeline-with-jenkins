# CI/CD Pipeline with Jenkins

This sample project demonstrates a **medium‑complexity** end‑to‑end CI/CD pipeline using **Jenkins**, **Docker**, and **Kubernetes** to build, test, and deploy a small Python (Flask) microservice.

## Tech Stack

| Layer          | Technology |
| -------------- | ---------- |
| Application    | Python 3.11 / Flask |
| Testing        | pytest |
| Container      | Docker |
| CI/CD          | Jenkins (Declarative Pipeline) |
| Deployment     | Kubernetes |

## Repository Layout

```
.
├── app/
│   ├── src/
│   │   └── main.py            # Flask entry‑point
│   ├── tests/
│   │   └── test_app.py        # Unit tests
│   ├── requirements.txt       # Python dependencies
│   └── Dockerfile             # Container image recipe
├── Jenkinsfile                # Declarative pipeline
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
└── README.md                  # You are here
```

## How It Works

1. **Checkout & Dependency Caching** – Jenkins pulls this repo.
2. **Unit Tests** – `pytest` ensures the code passes basic health checks.
3. **Build Docker Image** – The `Dockerfile` packages the service.
4. **Push to Registry** – The image is pushed to Docker Hub (or your registry of choice).
5. **Deploy to Kubernetes** – The deployment is updated via `kubectl set image`.

The entire flow is captured in `Jenkinsfile`.  
Feel free to extend the pipeline with parallel stages, code coverage or security scanning.

## Quick Start (Local)

```bash
# 1) Run the service locally
cd app
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

Visit http://localhost:5000 to see the JSON greeting.

## Jenkins Setup Checklist

1. **Freestyle vs Multibranch?** – Choose *Multibranch Pipeline* pointing at this repo.
2. **Install Plugins** – Docker, Blue Ocean, Kubernetes CLI etc.
3. **Credentials**  
   * `docker-hub` – Username & password / token for your registry  
   * (Optional) `kubeconfig` – If running `kubectl` from Jenkins agents
4. **Agent Requirements** – Docker CLI + buildx + Python if you run tests on the same node.
5. **Trigger** – Poll SCM or webhook.

## Kubernetes Deployment

- Edit `kubernetes/deployment.yaml` to match your namespace & image repo.  
- Apply once: `kubectl apply -f kubernetes/`

Jenkins will later reuse the same deployment and only swap the image tag (`kubectl set image ...`).

## Contributing

Pull requests are welcome! Open an issue first to discuss improvements.

---
© 2025 Erkan Baran
