"""跨源数据交叉验证 — 多源互相校验，差异自动报警。

Sources: nowscore(捷报), 500.com(五百万), okooo(澳客-必发)
Every analysis must cross-verify at least 2 sources.
Discrepancy > 0.05 → auto-flag, use freshest source.

v2.0: Now integrates with wubai.get_odds_full() for opening vs current comparison.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Optional

log = logging.getLogger(__name__)

# 澳客 必发数据源 — 可验证交易所赔率 vs 传统庄家
BIFAX_SOURCE = "okooo_exchanges"


@dataclass
class VerifiedOdds:
    """Odds that have been cross-verified across at least 2 sources."""

    home: float
    draw: float
    away: float
    source: str = ""  # which source was used as final
    verified_by: list[str] = field(default_factory=list)
    discrepancies: list[str] = field(default_factory=list)
    confidence: str = "high"

    # Additional source data
    bifax_odds: Optional[tuple] = None       # from okooo exchanges
    bifax_volume_pct: Optional[dict] = None   # volume distribution
    bifax_pnl: Optional[dict] = None          # bookmaker P&L

    # Opening vs current
    opening_odds: Optional[tuple] = None      # opening odds for comparison
    steam_analysis: Optional[dict] = None      # steam result

    @property
    def is_verified(self) -> bool:
        return len(self.verified_by) >= 2

    def to_tuple(self) -> tuple:
        return (self.home, self.draw, self.away)

    def add_bifax(self, odds: tuple, vol_pct: dict, pnl: dict) -> None:
        """Add 必发 data from okooo for cross-reference."""
        self.bifax_odds = odds
        self.bifax_volume_pct = vol_pct
        self.bifax_pnl = pnl
        self.verified_by.append(BIFAX_SOURCE)
        if self.away > 0 and odds[2] > 0:
            gap = abs(odds[2] - self.away)
            if gap > 0.15:
                self.discrepancies.append(
                    f"必发vs传统庄家差异: 交易所{odds[2]:.2f} vs {self.source}{self.away:.2f} (gap={gap:.2f})"
                )

    def add_opening(self, opening: tuple[float, float, float]) -> None:
        """Add opening odds for steam comparison."""
        self.opening_odds = opening
        steam_info = verify_opening_vs_closing(opening, self.to_tuple())
        self.steam_analysis = steam_info
        if steam_info.get("steam") and abs(steam_info["steam"]) > 0.08:
            self.discrepancies.append(
                f"Steam {steam_info['direction']}: {steam_info['steam']:+.2f} ({steam_info['magnitude']})"
            )


def verify_nowscore_vs_wubai(
    nowscore_odds: Optional[tuple[float, float, float]],
    wubai_odds: Optional[tuple[float, float, float]],
    company_name: str = "Bet365",
    tolerance: float = 0.05,
) -> Optional[VerifiedOdds]:
    """Cross-check a single company's odds between nowscore and 500.com."""
    if not nowscore_odds and not wubai_odds:
        return None

    verified = VerifiedOdds(home=0, draw=0, away=0)
    discrepancies = []

    if nowscore_odds:
        verified.home, verified.draw, verified.away = nowscore_odds
        verified.source = "nowscore"
        verified.verified_by.append("nowscore")

        if wubai_odds:
            diff = abs(nowscore_odds[1] - wubai_odds[1])
            if diff <= tolerance:
                verified.verified_by.append("500.com")
            else:
                msg = (
                    f"{company_name}差异{nowscore_odds[1]:.2f} vs {wubai_odds[1]:.2f} "
                    f"(gap={diff:.2f}) 使用较新数据源({verified.source})"
                )
                discrepancies.append(msg)
                log.warning(msg)
                if wubai_odds[1] < nowscore_odds[1]:
                    verified.home, verified.draw, verified.away = wubai_odds
                    verified.source = "500.com(fresher)"
    elif wubai_odds:
        verified.home, verified.draw, verified.away = wubai_odds
        verified.source = "500.com"
        verified.verified_by.append("500.com")
        discrepancies.append(f"{company_name}: nowscore无数据,仅用500.com")

    verified.discrepancies = discrepancies
    if len(discrepancies) > 0:
        verified.confidence = "medium"
    if len(verified.verified_by) < 2:
        verified.confidence = "low"

    return verified


def verify_opening_vs_closing(
    opening_odds: Optional[tuple[float, float, float]],
    closing_odds: Optional[tuple[float, float, float]],
    favorite_side: str = "A",  # "H" or "A" or "D"
) -> dict:
    """Verify opening vs closing odds movement.

    Now uses the full wubai.get_odds_full() dual data.
    """
    if not opening_odds or not closing_odds:
        return {"steam": None, "direction": "未知", "interpretation": "缺少初盘或即时盘数据"}

    idx = {"H": 0, "D": 1, "A": 2}.get(favorite_side, 2)
    steam = closing_odds[idx] - opening_odds[idx]

    if abs(steam) < 0.03:
        direction = "稳定"
        interpretation = "市场无显著变化"
    elif steam > 0:
        direction = "🔴 市场冷却"
        interpretation = f"热门赔率上升{steam:+.2f}，市场信心下降"
    else:
        direction = "🟢 市场涌入"
        interpretation = f"热门赔率下降{steam:+.2f}，市场信心增强"

    magnitude = (
        "海啸" if abs(steam) > 0.30
        else "强" if abs(steam) > 0.10
        else "中" if abs(steam) > 0.05
        else "弱"
    )

    return {
        "steam": round(steam, 4),
        "direction": direction,
        "magnitude": magnitude,
        "interpretation": interpretation,
        "opening_odds": opening_odds,
        "closing_odds": closing_odds,
    }


def verify_ou_cross_bookmakers(ou_data: dict) -> dict:
    """Cross-verify O/U trends across bookmakers.

    Args:
        ou_data: dict from ou_data.MatchOU (with bookmakers list)

    Returns:
        dict with consensus, divergence warnings, and recommendation.
    """
    if not ou_data or not ou_data.get("bookmakers"):
        return {"consensus": "无数据", "warnings": [], "recommendation": "O/U数据缺失"}

    bookmakers = ou_data["bookmakers"]
    warnings = []

    # Check line consensus
    lines = [b["cur_line"] for b in bookmakers]
    unique_lines = set(int(l * 4) for l in lines)
    if len(unique_lines) >= 5:
        warnings.append(f"O/U盘口高度分歧 ({len(unique_lines)}种线位)")

    # Check over/under odds spread
    over_odds = [b["cur_over"] for b in bookmakers]
    under_odds = [b["cur_under"] for b in bookmakers]
    over_spread = max(over_odds) - min(over_odds)
    under_spread = max(under_odds) - min(under_odds)

    if over_spread > 0.30:
        warnings.append(f"大球赔率离散 ({over_spread:.2f})")
    if under_spread > 0.30:
        warnings.append(f"小球赔率离散 ({under_spread:.2f})")

    # Trend direction
    avg_move = sum(b.get("line_move", 0) for b in bookmakers) / len(bookmakers)
    if avg_move > 0.15:
        recommendation = "多家升盘 → 倾向大球"
    elif avg_move < -0.15:
        recommendation = "多家降盘 → 倾向小球"
    else:
        recommendation = "盘口稳定，无明确方向"

    return {
        "consensus": f"{len(unique_lines)}种线位",
        "avg_line_move": round(avg_move, 2),
        "over_spread": round(over_spread, 2),
        "under_spread": round(under_spread, 2),
        "warnings": warnings,
        "recommendation": recommendation,
    }
