"""Central logging configuration (rotating file + console)."""
from __future__ import annotations

import logging
import logging.handlers
import sys
from pathlib import Path


def setup_logging(level: str = "INFO", file: str = "/var/log/iran_chem_db/app.log",
                  max_size_mb: int = 100, backup_count: int = 10) -> logging.Logger:
    root = logging.getLogger()
    if root.handlers:  # already configured
        return root
    root.setLevel(getattr(logging, level.upper(), logging.INFO))
    fmt = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s")

    console = logging.StreamHandler(sys.stderr)
    console.setFormatter(fmt)
    root.addHandler(console)

    log_path = Path(file)
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        fh = logging.handlers.RotatingFileHandler(
            log_path, maxBytes=max_size_mb * 1024 * 1024, backupCount=backup_count
        )
        fh.setFormatter(fmt)
        root.addHandler(fh)
    except OSError:
        root.warning("could not open log file %s; logging to console only", file)

    return root


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
