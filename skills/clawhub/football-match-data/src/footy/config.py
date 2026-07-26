"""Project configuration and paths."""
from __future__ import annotations

from pathlib import Path

# Resolve paths relative to the repo root (footy-edge/), not the package.
# Primary: D drive (more space), fallback: project-local
_D_PRIMARY = Path("D:/ZCodeProject/footy-edge")
if _D_PRIMARY.exists():
    PROJECT_ROOT = _D_PRIMARY
    DATA_DIR = _D_PRIMARY / "data"
else:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
DB_PATH = DATA_DIR / "footy.db"
PARAMS_PATH = DATA_DIR / "model_params.json"
LEDGER_PATH = DATA_DIR / "ledger.csv"

# football-data.co.uk league codes for the five major European leagues.
# E0 = Premier League, SP1 = La Liga, I1 = Serie A, D1 = Bundesliga, F1 = Ligue 1.
LEAGUE_CODES = {
    "E0": "Premier League",
    "SP1": "La Liga",
    "I1": "Serie A",
    "D1": "Bundesliga",
    "F1": "Ligue 1",
}

BASE_URL = "https://www.football-data.co.uk/mmz4281/{season}/{league}.csv"

# Closing-odds columns we care about, by bookmaker prefix. These are the
# bookmaker's final pre-match odds — the gold standard for backtesting.
ODDS_BOOKMAKERS = ["B365", "BW", "IW", "PS", "WH", "VC", "Max", "Avg"]


def ensure_dirs() -> None:
    """Create the data directories if missing."""
    for d in (DATA_DIR, RAW_DIR):
        d.mkdir(parents=True, exist_ok=True)
