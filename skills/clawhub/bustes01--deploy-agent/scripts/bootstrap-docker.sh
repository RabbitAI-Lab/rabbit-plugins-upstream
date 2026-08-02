#!/usr/bin/env bash
# bootstrap-docker.sh - Install Docker Engine + Compose Plugin on Ubuntu/Debian
# Safe to run multiple times (idempotent)
set -euo pipefail

if command -v docker &>/dev/null; then
    echo "[✓] Docker already installed: $(docker --version 2>/dev/null || true)"
    docker compose version 2>/dev/null && echo "[✓] Compose plugin ready" || echo "[!] Compose plugin missing"
    exit 0
fi

echo "[*] Installing Docker Engine..."
sudo apt-get update -qq
sudo apt-get install -y -qq ca-certificates curl

sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update -qq
sudo apt-get install -y -qq docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add current user to docker group (avoid sudo)
sudo usermod -aG docker "$(whoami)" 2>/dev/null || true

echo "[✓] Docker installed: $(docker --version)"
echo "[✓] Compose: $(docker compose version 2>/dev/null || echo 'error')"
echo ""
echo "[!] You may need to log out and back in for docker group to take effect."
echo "    Or run: newgrp docker"
