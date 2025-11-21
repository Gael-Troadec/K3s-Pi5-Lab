# 🐙 Project Architeuthis: Autonomous Edge Fleet Lab

![CI Status](https://github.com/Gael-Troadec/K3s-Pi5-Lab/actions/workflows/docker-build.yml/badge.svg)
![Platform](https://img.shields.io/badge/platform-linux%2Farm64-orange)
![Status](https://img.shields.io/badge/status-operational-brightgreen)

## 📋 About The Project

**Architeuthis** is a personal lab project designed to simulate a fleet of autonomous underwater drones.

As an ex-Military transitioning to DevSecOps, my goal with this project is to build a complete **distributed infrastructure** from scratch. I am moving away from "click-ops" to fully automated, code-driven deployments on constrained hardware (Raspberry Pi 5).

**Core Learnings Achieved:**
* Complete **CI/CD pipeline** (Multi-Arch Buildx -> Docker Hub).
* Orchestration with **Kubernetes (K3s)**.
* **Stateful Architecture** (Data Persistence with PV/PVC).
* **SecOps Foundations** (Secrets Management & Env Injection).

---

## 📍 Current Progress (Day 17)

I have successfully **COMPLETED Phase II (Orchestration)** and **Phase III (Persistence)**. The system is now resilient to reboots and secure.

- [x] **Hardware Setup:** Raspberry Pi 5 (8GB) configured with OS Lite.
- [x] **CI/CD:** Multi-arch build (ARM64/AMD64) via Docker Buildx & QEMU.
- [x] **Containerization:** Python agents optimized for Edge execution.
- [x] **K3s Cluster:** Single-node cluster operational.
- [x] **Networking:** Ingress (Traefik) and Internal DNS Service Discovery.
- [x] **State Separation:** Redis deployed in Stateful mode.
- [x] **Disk Storage (PVC):** Persistent Volume Claims implemented. Data survives Pod deletion.
- [x] **Security:** Secrets management implemented (No plain-text passwords).
- [ ] **Observability:** Monitoring stack (Prometheus/Grafana). (Next Focus)

---

## 🛠️ Technical Architecture

### 📡 Infrastructure Flow (Updated)

```mermaid
graph LR
    subgraph Dev_Env ["Development Environment"]
        User("Gael") -->|Code & Push| GitHub("GitHub Repo")
    end
    
    subgraph CI_CD ["CI / Registry"]
        GitHub -->|Trigger| Actions{"GitHub Actions"}
        Actions -->|Push Image| Hub[("Docker Hub")]
    end
    
    subgraph Edge ["Raspberry Pi 5"]
        Hub -->|Pull Image| K3s["K3s Cluster"]
        
        subgraph Cluster ["Internal Architecture"]
            Ingress("Traefik") --> AppSvc("Architeuthis Service")
            
            subgraph Pods ["Pod Layer"]
                Secret["K8s Secret"] -.->|Inject Env Var| AppPod("Agent Pod")
                AppPod -->|Auth & Write| RedisPod("Redis Pod")
            end
            
            RedisPod -->|Persist Data| PVC[("PVC / Disk")]
        end
    end
    
    %% Links
    Dev_Env -.-> CI_CD
    CI_CD -.-> Edge
```

### Tech Stack
* **Language:** Python (Flask)
* **Container:** Docker (Multi-Arch)
* **Orchestration:** K3s (Lightweight Kubernetes)
* **Storage:** Local-Path Provisioner (PV/PVC)
* **Security:** Kubernetes Secrets (Base64)
* **Ingress:** Traefik

---

## 🚀 How to Run (Reproduction)

If you want to replicate this setup on a Raspberry Pi, follow these steps:

### 1. Install K3s
First, install the lightweight Kubernetes engine on the Pi:

```bash
curl -sfL [https://get.k3s.io](https://get.k3s.io) | INSTALL_K3S_EXEC="--write-kubeconfig-mode 644" sh -
```

### 2. Deploy the Fleet

Clone the repository and apply the Kubernetes manifests.
*Note: This will deploy the Storage Claims, Secrets, Database, and Application.*

```bash
git clone [https://github.com/Gael-Troadec/K3s-Pi5-Lab.git](https://github.com/Gael-Troadec/K3s-Pi5-Lab.git)
cd K3s-Pi5-Lab

# Apply all manifests (Order matters, but K8s handles convergence)
kubectl apply -f manifests/
```

### 3. Access the Dashboard

Map the local domain in your `/etc/hosts` (Linux/Mac) or `C:\Windows\System32\drivers\etc\hosts` (Windows):

```text
192.168.1.XXX   architeuthis.local
```

*(Replace `192.168.1.XXX` with your Raspberry Pi IP address)*

Then navigate to: **http://architeuthis.local**

---

## 🗺️ Roadmap

| Phase | Focus | Status |
| :--- | :--- | :--- |
| **I. Foundations** | Linux, Docker, CI/CD | ✅ Done |
| **II. Orchestration** | K3s, Ingress, GitOps | ✅ Done |
| **III. Persistence** | Storage, Database, State | ✅ Done |
| **IV. Security** | Secrets, Hardening | 🔄 Started |
| **V. Mutation** | Rewrite in Golang | ⏳ Planned |

---

*Project maintained by Gael Troadec.*
