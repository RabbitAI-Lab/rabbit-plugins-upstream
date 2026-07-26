"""Bet ledger: record real wagers and track the bankroll curve."""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from ..config import LEDGER_PATH


@dataclass
class Wager:
    date: str  # ISO date placed
    event: str  # e.g. "Arsenal vs Chelsea"
    market: str  # e.g. "1X2-H"
    selection: str  # human label, e.g. "Arsenal"
    odds: float
    stake: float  # units
    result: str = ""  # "" open, "win", "loss", "push"
    payout: float = 0.0

    @property
    def settled(self) -> bool:
        return self.result in ("win", "loss", "push")

    @property
    def pnl(self) -> float:
        if self.result == "win":
            return self.stake * (self.odds - 1)
        if self.result == "loss":
            return -self.stake
        return 0.0


_HEADER = [
    "date", "event", "market", "selection", "odds", "stake", "result", "payout",
]


def add_wager(w: Wager, path: Path | None = None) -> None:
    path = path or LEDGER_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        if new_file:
            wr.writerow(_HEADER)
        wr.writerow([getattr(w, h) for h in _HEADER])


def load_wagers(path: Path | None = None) -> list[Wager]:
    path = path or LEDGER_PATH
    if not path.exists():
        return []
    out: list[Wager] = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out.append(
                Wager(
                    date=row["date"],
                    event=row["event"],
                    market=row["market"],
                    selection=row["selection"],
                    odds=float(row["odds"]),
                    stake=float(row["stake"]),
                    result=row.get("result", ""),
                    payout=float(row.get("payout") or 0),
                )
            )
    return out


def settle_wager(index: int, result: str, path: Path | None = None) -> None:
    """Mark the wager at `index` (0-based, settled-bet order) as win/loss/push."""
    path = path or LEDGER_PATH
    wagers = load_wagers(path)
    wagers[index].result = result
    with open(path, "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(_HEADER)
        for w in wagers:
            wr.writerow([getattr(w, h) for h in _HEADER])


def summary(wagers: list[Wager]) -> dict:
    settled = [w for w in wagers if w.settled]
    open_bets = [w for w in wagers if not w.settled]
    total_staked = sum(w.stake for w in settled)
    total_pnl = sum(w.pnl for w in settled)
    wins = sum(1 for w in settled if w.result == "win")
    return {
        "n_settled": len(settled),
        "n_open": len(open_bets),
        "wins": wins,
        "hit_rate": wins / len(settled) if settled else 0.0,
        "staked": total_staked,
        "pnl": total_pnl,
        "roi": total_pnl / total_staked if total_staked else 0.0,
    }
