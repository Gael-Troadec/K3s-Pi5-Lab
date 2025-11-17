# K3s Pi5 Lab

Single-node Kubernetes on Raspberry Pi 5. Personal lab for learning container orchestration and integrating with CI/CD.

## What I Did Today (Day 1)

- Flashed Ubuntu 24.04.3 LTS ARM64 on SD card
- SSH hardened with ED25519 keys (no password auth)
- Fixed netplan network chaos (Ethernet DHCP works, WiFi too complex for now)
- Installed K3s: `curl -sfL https://get.k3s.io | sh -`
- Verified: `kubectl get nodes` → pi5-lab Ready

## Why K3s?

Lightweight Kubernetes (~100MB). Perfect for edge devices. CKA cert requires real cluster to practice on, this is mine.

## Issues I Hit

1. **netplan routing conflicts:** Two config files (wlan0 + eth0) fighting. Fixed by removing WiFi, keeping Ethernet DHCP only.
2. **SSH dead after apt upgrade:** Service stopped. Fixed with `systemctl restart ssh`.

## Next

Deploy Flask app from my CI/CD pipeline directly to K3s. GitOps integration later.
