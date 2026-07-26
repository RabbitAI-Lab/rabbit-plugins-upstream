"""Shared model loading utilities for the match data pipeline.

Extracts model-loading logic so both the CLI and auto_checklist can reuse it
without circular imports.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from .poisson import PoissonModel, PoissonParams
from .dixon_coles import DixonColesModel, DixonColesParams

log = logging.getLogger(__name__)

# Resolve data/ relative to the repo root (footy-edge/).
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_DEFAULT_PARAMS_PATH = _PROJECT_ROOT / "data" / "model_params.json"


def load_fitted_model(
    params_path: str | Path | None = None,
) -> Optional[DixonColesModel | PoissonModel]:
    """Load a fitted Dixon-Coles (or Poisson) model from a JSON params file.

    Args:
        params_path: Path to model_params.json. Defaults to ``data/model_params.json``
                     under the repo root.

    Returns:
        A fitted model instance, or ``None`` if the file is missing or unreadable.
    """
    path = Path(params_path) if params_path else _DEFAULT_PARAMS_PATH
    if not path.exists():
        log.info("No fitted model at %s — Poisson predictions unavailable.", path)
        return None

    try:
        blob = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        log.warning("Failed to read model params %s: %s", path, exc)
        return None

    model_name = blob.get("model", "Dixon-Coles")
    params_cls = PoissonParams if model_name == "Poisson" else DixonColesParams
    mdl = PoissonModel() if model_name == "Poisson" else DixonColesModel()

    p = blob["params"]
    mdl.params = params_cls(
        attack=p["attack"],
        defence=p["defence"],
        home_adv=p["home_adv"],
        intercept=p["intercept"],
        rho=p.get("rho", 0.0),
    )
    log.info("Loaded %s model (%d teams).", model_name, len(p["attack"]))
    return mdl


def find_most_likely_score(grid, max_goals: int = 10) -> tuple[int, int]:
    """Return (home_goals, away_goals) with the highest joint probability."""
    import numpy as np
    idx = np.unravel_index(np.argmax(grid), grid.shape)
    return int(idx[0]), int(idx[1])
