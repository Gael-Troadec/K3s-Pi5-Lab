# 🐙 Project Architeuthis: DevSecOps Edge Lab

![CI Status](https://github.com/Gael-Troadec/K3s-Pi5-Lab/actions/workflows/docker-build.yml/badge.svg)
![Platform](https://img.shields.io/badge/platform-linux%2Farm64-orange)
![Status](https://img.shields.io/badge/status-learning-yellow)

## 📋 About The Project

**Architeuthis** is a personal lab project designed to simulate a fleet of autonomous underwater drones.

As a ex-Military transitioning to DevSecOps, my goal with this project is to build a complete **distributed infrastructure** from scratch. I am moving away from "click-ops" to fully automated, code-driven deployments on constrained hardware (Raspberry Pi 5).

**Core Learning Objectives:**
* Mastering **Linux** & **Networking** fundamentals.
* Building a complete **CI/CD pipeline** (GitHub Actions -> Docker Hub).
* Orchestrating containers with **Kubernetes (K3s)**.
* Managing **Infrastructure as Code (IaC)**.

---

## 📍 Current Progress (Day 16)

I am currently in **Phase 2 (Orchestration)** of the roadmap.

- [x] **Hardware Setup:** Raspberry Pi 5 (8GB) configured with OS Lite.
- [x] **CI/CD:** Pipeline functional. Commits on `main` trigger a multi-arch build (ARM64/AMD64) via QEMU.
- [x] **Docker:** Python agents are containerized and optimized.
- [x] **K3s Cluster:** Single-node cluster up and running.
- [x] **Networking:** Service Discovery (NodePort) and Ingress (Traefik) are configured.
- [x] **Scaling:** Deployment configured with replicas and self-healing tested.
- [ ] **Persistence:** Database and storage implementation (Next Step).
- [ ] **Security:** Hardening and Policies (Planned).

---

## 🛠️ Technical Architecture

The workflow mimics a production environment but adapted for a home lab:

1.  **Dev Environment:** Code written on Windows 11 (WSL2 - Ubuntu).
2.  **Continuous Integration:** GitHub Actions builds the Docker image.
3.  **Registry:** Images stored on Docker Hub.
4.  **Edge Node (Prod):** Raspberry Pi 5 running K3s pulls the image and updates the deployment.

 ### 📡 Architecture Diagram

```mermaid
graph TD
    subgraph Dev ["Command & Control (WSL2/PC)"]
        Developer[👱 Gael] -->|Push Code| GitHub[GitHub Repo]
        GitHub -->|Trigger| Actions[GitHub Actions CI]
    end

    subgraph DockerInfra ["Docker Infrastructure"]
        Actions -->|Build & Test| QEMU[QEMU Multi-Arch Build]
        QEMU -->|Push Image| Hub[Docker Hub Registry]
    end

    subgraph Edge ["Edge Layer (Raspberry Pi 5 / K3s)"]
        K3s[K3s Cluster] -->|Pull Image| Hub
        
        subgraph Cluster ["Cluster K3s Internal"]
            Ingress[Traefik Ingress] -->|Route Traffic| Service[K8s Service]
            Service -->|Load Balance| Pod1[🦈 Agent 1]
            Service -->|Load Balance| Pod2[🦈 Agent 2]
        end
    end

    style Edge fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style Pod1 fill:#ffccbc,stroke:#ff5722
    style Pod2 fill:#ffccbc,stroke:#ff5722

### Tech Stack
* **Language:** Python (Flask)
* **Container:** Docker
* **Orchestration:** K3s (Lightweight Kubernetes)
* **Ingress:** Traefik
* **Tools:** VS Code, Git, K9s

---

## 🚀 How to Run (Reproduction)

If you want to replicate this setup on a Raspberry Pi, follow these steps:

### 1. Install K3s
First, install the lightweight Kubernetes engine on the Pi (with user permissions enabled):

```bash
curl -sfL [https://get.k3s.io](https://get.k3s.io) | INSTALL_K3S_EXEC="--write-kubeconfig-mode 644" sh -
````

### 2\. Deploy the Fleet

Clone the repository and apply the Kubernetes manifests:

```bash
git clone [https://github.com/Gael-Troadec/K3s-Pi5-Lab.git](https://github.com/Gael-Troadec/K3s-Pi5-Lab.git)
cd K3s-Pi5-Lab
kubectl apply -f manifests/
```

### 3\. Access the Dashboard

Since this is a local lab without a real domain name, you need to map the local domain.

Add this line to your local `/etc/hosts` (Linux/Mac) or `C:\Windows\System32\drivers\etc\hosts` (Windows):

```text
192.168.1.XXX   architeuthis.local
```

*(Replace `192.168.1.XXX` with your Raspberry Pi IP address)*

Then open your browser and navigate to: **http://architeuthis.local**

-----

## 🗺️ Roadmap

| Phase | Focus | Status |
| :--- | :--- | :--- |
| **I. Foundations** | Linux, Docker, CI/CD | ✅ Done |
| **II. Orchestration** | K3s, Ingress, GitOps | 🔄 In Progress |
| **III. Persistence** | Storage, Database, State | ⏳ Planned |
| **IV. Mutation** | Rewrite in Golang | ⏳ Planned |
| **V. Security** | CKS Prep, Hardening | ⏳ Planned |

-----

*Project maintained by Gael Troadec.*

```
```
