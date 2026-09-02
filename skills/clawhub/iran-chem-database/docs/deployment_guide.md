# Deployment Guide

## One-command deployment (Docker Compose)

```bash
cp .env.example .env      # set DB_PASSWORD (and optionally SEARCH_API_KEY)
./install.sh              # installs httrack + docker, builds, seeds, starts
```

Or manually:

```bash
docker compose up -d postgres redis
alembic upgrade head
python -m src.scripts.seed_suppliers
docker compose up -d
python -m src.scripts.trigger_initial_crawl
```

## Services

| Service | Port | Role |
|---|---|---|
| nginx | 80 | reverse proxy (API + dashboard) |
| app | 8000 | FastAPI REST API |
| dashboard | 8501 | Streamlit UI (incl. HTTrack mirror monitor) |
| crawler | — | Celery worker running httrack mirrors |
| scheduler | — | Celery Beat (6h/24h/72h mirror intervals, weekly discovery) |
| postgres | 5432 | PostgreSQL 15 (live molecule DB) |
| redis | 6379 | Celery broker / cache |

## Persistent storage

- `httrack_mirrors` volume → host path `/var/lib/iran_chem_db/mirrors`
  (survives container restarts; the mirror store is the source of truth)
- `pgdata` volume → PostgreSQL data

## Bare-metal

Requires: Python 3.11+, PostgreSQL 15+, Redis, and `sudo apt install httrack`.

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
alembic upgrade head
uvicorn src.api.app:app --host 0.0.0.0 --port 8000
streamlit run src/dashboard/app.py --server.port=8501
celery -A src.tasks.celery_app worker --loglevel=info
celery -A src.tasks.celery_app beat --loglevel=info
```

## Polite crawling policy

- robots.txt honored (`--robots=2` default)
- rate-limited (`--connection-per-second`, `--max-rate`)
- identifiable User-Agent (`IranChemDB/1.0`)
- per-supplier overrides in `config.yaml` (`httrack.supplier_overrides`)

## Production hardening

The API and dashboard are trusted-network services by default. Before exposing
them publicly:

1. **Authenticate the API** — add auth (e.g. nginx basic-auth or an API-key
   middleware) in front of `/api/v1/`.
2. **Scope egress** — if you run an egress firewall, allowlist only the supplier
   domains you actually mirror, plus `pubchem.ncbi.nlm.nih.gov` and your search
   provider.
3. **Use TLS** — terminate HTTPS at nginx.
4. **Rate-limit the dashboard** and keep the mirror store on a dedicated volume.
