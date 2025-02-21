# 📌 Containerized Application with Red Hat UBI

## 🚀 Overview
This project is a **containerized web application** built using **Flask and PostgreSQL**, optimized with **Red Hat Universal Base Image (UBI)** for enterprise environments. It includes **CI/CD automation**, **Kubernetes deployment**, **security scanning**, and **real-time monitoring.**

---

## 🏗️ Architecture

![Architecture Diagram](https://example.com/sample-architecture.png)  
*Illustration of the complete architecture of the project.*

---

## 🌟 Features
- **Containerization with Red Hat UBI**
- **Kubernetes Deployment (OpenShift & Kubernetes)**
- **Security Scanning (Trivy, Clair, Aqua Security)**
- **Automated CI/CD Pipeline (GitHub Actions, Jenkins, Tekton)**
- **Real-time Logging & Monitoring (Prometheus & Grafana)**
- **Secure RBAC & Network Policies**
- **Health Checks & Readiness Probes**

---

## 🏗️ Folder Structure
```
📂 containerized-ubi-app/  # Root Project Directory
├── 📂 app/                 # Application source code
│   ├── main.py             # Flask main app file
│   ├── config.py           # Configuration settings
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # UBI-based Docker configuration
│   ├── wsgi.py             # WSGI entry point
│   ├── 📂 routes/          # API route handlers
│   ├── 📂 models/          # Database models
│   ├── 📂 templates/       # HTML templates (optional)
│   ├── 📂 static/          # Static assets
│   ├── 📂 tests/           # Unit & Integration Tests
│   ├── __init__.py         # App initialization
│
├── 📂 database/            # Database migrations
│   ├── schema.sql          # PostgreSQL schema
│   ├── seed_data.sql       # Initial data
│   ├── init_db.py          # DB initialization script
│
├── 📂 k8s/                 # Kubernetes deployment files
│   ├── deployment.yaml     # Flask App Deployment
│   ├── service.yaml        # Kubernetes Service
│   ├── ingress.yaml        # Ingress Rules
│   ├── rbac.yaml           # Role-Based Access Control
│   ├── monitoring.yaml     # Prometheus & Grafana setup
│
├── 📂 cicd/                # CI/CD pipeline setup
│   ├── github-actions.yaml # GitHub Actions workflow
│   ├── tekton-pipeline.yaml # Tekton CI/CD pipeline
│
├── 📂 monitoring/          # Monitoring & Logging Setup
│   ├── prometheus-config.yaml
│   ├── grafana-dashboard.json
│   ├── fluentd-config.yaml
│
├── .gitignore              # Git ignore rules
├── docker-compose.yaml     # Local Development Setup
├── LICENSE                 # Open-source license
├── README.md               # Project Documentation
```

---

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/containerized-ubi-app.git
cd containerized-ubi-app
```

### 2️⃣ Build & Run the Application (Docker)
```bash
docker build -t ubi-flask-app .
docker run -p 5000:5000 ubi-flask-app
```

### 3️⃣ Run with Docker Compose (Local Setup)
```bash
docker-compose up -d
```

### 4️⃣ Deploy to Kubernetes (OpenShift/K8s)
```bash
kubectl apply -f k8s/
```

---

## 🔍 CI/CD Pipeline (Tekton)
**Tekton pipeline includes:**
- **Clone Repository** ✅
- **Run Unit & Integration Tests** ✅
- **Build Container Image (Buildah)** ✅
- **Security Scan (Trivy)** ✅
- **Push Image to Container Registry** ✅
- **Deploy to Kubernetes** ✅

To trigger the pipeline:
```bash
kubectl apply -f cicd/tekton-pipeline.yaml
```

---

## 🔐 Security Features
- **Trivy Security Scan** (Scans container images for vulnerabilities)
- **RBAC Policies** (Secure access control using `rbac.yaml`)
- **Pod Security Policies** (Restrict container privileges)
- **Network Policies** (Limit communication between services)

---

## 📊 Monitoring & Logging
### 🛠️ **Prometheus & Grafana Setup**
![Grafana Dashboard](https://example.com/grafana-dashboard.png)

```bash
kubectl apply -f monitoring/prometheus-config.yaml
kubectl apply -f monitoring/grafana-dashboard.json
```

### 📜 **Fluentd Logging Configuration**
```bash
kubectl apply -f monitoring/fluentd-config.yaml
```

---

## 📞 API Endpoints
### 🔹 **User Management**
| Method | Endpoint        | Description        |
|--------|---------------|--------------------|
| GET    | `/api/users`  | Get all users     |
| POST   | `/api/users`  | Create a user     |

### 🔹 **Health Check**
| Method | Endpoint         | Description           |
|--------|----------------|-----------------------|
| GET    | `/api/health`  | Application Health   |

---

## 📌 Contributing
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature-name`)
5. Create a Pull Request

---

## 📄 License
This project is licensed under the **MIT License**.

---

## 📞 Contact
📧 Email: ydalayi8@gmail.com 
🔗 LinkedIn: [Yuvaraju Dalayi](https://www.linkedin.com/in/yuvarajdalayi/)  

