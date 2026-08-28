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
    # The ClawHub registry strips leading-dot files from published artifacts,
    # so .env.example may be absent even though it exists in the source tree.
    # env.example is the non-dotfile twin that always survives packaging.
    ENV_TEMPLATE=""
    for cand in .env.example env.example; do
        [ -f "$cand" ] && { ENV_TEMPLATE="$cand"; break; }
    done
    if [ -z "$ENV_TEMPLATE" ]; then
        echo "[!] Missing .env.example / env.example in this release; cannot safely continue."
        echo "    Reinstall a corrected release or create .env with DB_PASSWORD."
        exit 1
    fi
    cp "$ENV_TEMPLATE" .env
    echo "[!] Created .env from $ENV_TEMPLATE. Set a strong DB_PASSWORD before continuing."
fi

# Load local values for the installer without logging them.
set -a
# shellcheck disable=SC1091
. ./.env
set +a

if [ -z "${DB_PASSWORD:-}" ] || [ "$DB_PASSWORD" = "change-this-to-a-long-random-password" ]; then
    echo "[!] DB_PASSWORD is missing or still a placeholder in .env."
    echo "    Set it, then rerun ./install.sh."
    echo "    Recover with: sed -i 's/^DB_PASSWORD=.*/DB_PASSWORD=<strong-random-value>/' .env"
    exit 1
fi

# --- 6) Start services ----------------------------------------------------
echo "[*] Starting Docker services..."
docker compose up -d postgres redis || { echo "[!] postgres/redis failed to start — check 'docker compose ps' and logs."; exit 1; }
echo "[*] Waiting for PostgreSQL readiness..."
for _ in $(seq 1 30); do
    if docker compose exec -T postgres pg_isready -U chemdb >/dev/null 2>&1; then
        break
    fi
    sleep 2
done

# --- 7) Migrations --------------------------------------------------------
echo "[*] Running database migrations..."
alembic -c alembic/alembic.ini upgrade head

# --- 8) Seed supplier list ------------------------------------------------
echo "[*] Seeding supplier database..."
python -m src.scripts.seed_suppliers

# --- 9) Start everything --------------------------------------------------
echo "[*] Starting all services..."
docker compose up -d || { echo "[!] services failed to start — check 'docker compose ps' and logs."; exit 1; }

# --- 10) First crawl (QUEUED — never synchronous) -------------------------
echo "[*] Queueing initial seed crawl (async; discovery is separate and optional)..."
python -m src.scripts.trigger_initial_crawl

echo ""
echo "============================================"
echo "  Installation provides SOFTWARE, not a"
echo "  populated dataset. Services and jobs are"
echo "  initialized; initial supplier crawling has"
echo "  been QUEUED and may take hours or days."
echo ""
echo "  Monitor coverage with:"
echo "    curl -s http://localhost/api/v1/coverage"
echo "    curl -s http://localhost/api/v1/stats"
echo "    curl -s http://localhost/api/v1/crawl-logs?limit=200"
echo ""
echo "  Do NOT treat an export as complete until all"
echo "  selected suppliers have a terminal crawl status."
echo ""
echo "  Dashboard: http://localhost:8501"
echo "  API:       http://localhost:80/api/v1/"
echo "  HTTrack mirrors: /var/lib/iran_chem_db/mirrors/"
echo "============================================"
