#!/bin/bash
# Iran Chemical Database — Installer (HTTrack-powered live crawling system)
set -euo pipefail

echo "============================================"
echo "  Iran Chemical Database - Installer"
echo "  HTTrack-Powered Live Crawling System"
echo "============================================"

# --- 1) Detect distro and install system packages -------------------------
if [ -f /etc/debian_version ]; then
    echo "[*] Detected Debian/Ubuntu"
    sudo apt-get update
    sudo apt-get install -y httrack libhttrack-dev docker.io docker-compose-v2 \
        python3 python3-pip python3-venv
elif [ -f /etc/fedora-release ]; then
    echo "[*] Detected Fedora"
    sudo dnf install -y httrack docker docker-compose python3 python3-pip
elif [ -f /etc/arch-release ]; then
    echo "[*] Detected Arch"
    sudo pacman -S --noconfirm httrack docker docker-compose python python-pip
else
    echo "[!] Unsupported distro. Please install httrack and docker manually."
    exit 1
fi

# --- 2) Verify HTTrack ----------------------------------------------------
echo "[*] Verifying HTTrack installation..."
httrack --version || { echo "HTTrack installation failed!"; exit 1; }

# --- 3) Create directories (ownership set at creation, no recursive chown) --
echo "[*] Creating directories..."
sudo install -d -o "$USER" -g "$USER" /var/lib/iran_chem_db/mirrors
sudo install -d -o "$USER" -g "$USER" /var/log/iran_chem_db

# --- 4) Python environment ------------------------------------------------
echo "[*] Setting up Python environment..."
python3 -m venv venv
# shellcheck disable=SC1091
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium

# --- 5) Environment -------------------------------------------------------
if [ ! -f .env ]; then
    echo "[*] Creating .env file..."
    cp .env.example .env
    echo "[!] IMPORTANT: Edit .env and set DB_PASSWORD and SEARCH_API_KEY"
fi

# --- 6) Start services ----------------------------------------------------
echo "[*] Starting Docker services..."
docker compose up -d postgres redis
sleep 5

# --- 7) Migrations --------------------------------------------------------
echo "[*] Running database migrations..."
alembic upgrade head

# --- 8) Seed supplier list ------------------------------------------------
echo "[*] Seeding supplier database..."
python -m src.scripts.seed_suppliers

# --- 9) Start everything --------------------------------------------------
echo "[*] Starting all services..."
docker compose up -d

# --- 10) First crawl ------------------------------------------------------
echo "[*] Triggering initial supplier discovery and HTTrack mirroring..."
python -m src.scripts.trigger_initial_crawl

echo ""
echo "============================================"
echo "  Installation complete!"
echo "  Dashboard: http://localhost:8501"
echo "  API:       http://localhost:80/api/v1/"
echo "  HTTrack mirrors: /var/lib/iran_chem_db/mirrors/"
echo "============================================"
