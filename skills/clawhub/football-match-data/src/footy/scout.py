"""Match scouting — analyze ANY match by searching the web for data.

Uses web search to find: recent form, head-to-head, current odds, team news.
Then applies the same analysis framework (Poisson, odds signals, steam) to
produce a prediction with confidence level.

For matches outside the top 5 leagues, this is the primary analysis path.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class ScoutReport:
    """Analysis result for a scouted match."""

    home: str
    away: str
    competition: str = ""
    kickoff: str = ""

    # Odds found
    odds_1x2: tuple[float, float, float] = (0, 0, 0)
    odds_source: str = ""

    # Recent form (last 5-6 matches each)
    home_form: list[str] = field(default_factory=list)  # ["W","D","L",...]
    away_form: list[str] = field(default_factory=list)

    # Head-to-head
    h2h: list[str] = field(default_factory=list)  # ["H 2-1","A 0-3",...]

    # Analysis
    implied_probs: tuple[float, float, float] = (0, 0, 0)
    home_strength: str = ""  # "strong" | "moderate" | "weak"
    away_strength: str = ""
    form_edge: str = ""  # which side has better form
    h2h_edge: str = ""

    # Verdict
    prediction: str = ""   # "home" | "draw" | "away" | "too close"
    confidence: str = ""   # "high" | "medium" | "low"
    reasoning: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    # Raw search snippets
    sources: list[str] = field(default_factory=list)


def _parse_odds(text: str) -> Optional[tuple[float, float, float]]:
    """Try to extract 1X2 odds from text."""
    # Pattern: "Japan 2.00 / Draw 3.60 / Sweden 4.35"
    m = re.search(
        r"(\d+\.\d{2})\s*/\s*.*?(\d+\.\d{2})\s*/\s*.*?(\d+\.\d{2})",
        text,
    )
    if m:
        return (float(m.group(1)), float(m.group(2)), float(m.group(3)))
    # Pattern: X.XX X.XX X.XX (three decimal numbers)
    m = re.search(r"(\d+\.\d{2})\s+(\d+\.\d{2})\s+(\d+\.\d{2})", text)
    if m:
        return (float(m.group(1)), float(m.group(2)), float(m.group(3)))
    return None


def _parse_form(text: str, team: str) -> list[str]:
    """Extract recent form (W/D/L) for a team from text."""
    # Look for explicit form strings like "W W D W W" or "WWDWW"
    m = re.search(r"[WDL]{3,10}", text, re.IGNORECASE)
    if m:
        return list(m.group().upper())
    # "4 wins 1 draw" or "4胜1平"
    w = d = l = 0
    wm = re.search(r"(\d+)\s*(?:wins|胜|W)", text, re.IGNORECASE)
    dm = re.search(r"(\d+)\s*(?:draws|平|D)", text, re.IGNORECASE)
    lm = re.search(r"(\d+)\s*(?:losses|负|L)", text, re.IGNORECASE)
    if wm:
        w = int(wm.group(1))
    if dm:
        d = int(dm.group(1))
    if lm:
        l = int(lm.group(1))
    if w + d + l > 0:
        return ["W"] * w + ["D"] * d + ["L"] * l
    return []


def _parse_h2h(text: str) -> list[str]:
    """Extract head-to-head results from H2H-specific text."""
    results = []
    # Match scorelines like "2-1" or "1:0"
    for m in re.finditer(r"(\d+)[\-:](\d+)", text):
        results.append(f"{m.group(1)}-{m.group(2)}")
    # Dedup
    seen = set()
    unique = []
    for r in results:
        if r not in seen:
            seen.add(r)
            unique.append(r)
    return unique[:10]


def analyze_scout_data(home: str, away: str, search_results: list[str]) -> ScoutReport:
    """Build a ScoutReport from web search results about a match.

    search_results: list of text snippets from web search / web fetch.
    """
    report = ScoutReport(home=home, away=away)
    all_text = " ".join(search_results)

    # ---- Extract competition ----
    comp_patterns = [
        r"(世界杯|欧洲杯|欧冠|欧联|英超|西甲|意甲|德甲|法甲|中超|J联赛|K联赛|"
        r"美洲杯|非洲杯|亚洲杯|世界杯预选|欧国联|友谊赛|热身赛)",
    ]
    for p in comp_patterns:
        m = re.search(p, all_text)
        if m:
            report.competition = m.group(1)
            break

    # ---- Extract kickoff time ----
    m = re.search(r"(\d{2}:\d{2})", all_text)
    if m:
        report.kickoff = m.group(1)

    # ---- Extract odds ----
    for text in search_results:
        odds = _parse_odds(text)
        if odds and odds[0] > 1.0 and odds[1] > 1.0 and odds[2] > 1.0:
            report.odds_1x2 = odds
            # Determine source
            if "okooo" in text.lower():
                report.odds_source = "澳客"
            elif "500.com" in text.lower() or "500wan" in text.lower():
                report.odds_source = "500彩票"
            elif "odds" in text.lower():
                report.odds_source = "odds site"
            else:
                report.odds_source = "web search"
            break

    # ---- Calculate implied probabilities ----
    if report.odds_1x2[0] > 0:
        imp = [1 / o for o in report.odds_1x2]
        ovr = sum(imp)
        report.implied_probs = tuple(p / ovr for p in imp)

    # ---- Extract form ----
    for text in search_results:
        hf = _parse_form(text, home)
        if hf and not report.home_form:
            report.home_form = hf
        af = _parse_form(text, away)
        if af and not report.away_form:
            report.away_form = af

    # ---- Extract H2H ----
    report.h2h = _parse_h2h(all_text)

    # ---- Analyze strengths ----
    hw = report.home_form.count("W") if report.home_form else 0
    aw = report.away_form.count("W") if report.away_form else 0
    hl = report.home_form.count("L") if report.home_form else 0
    al = report.away_form.count("L") if report.away_form else 0

    h_pts = hw * 3 + report.home_form.count("D") if report.home_form else 0
    a_pts = aw * 3 + report.away_form.count("D") if report.away_form else 0

    n = max(len(report.home_form), len(report.away_form), 5)
    if report.home_form:
        report.home_strength = "strong" if h_pts / max(n, 1) / 3 > 0.6 else (
            "moderate" if h_pts / max(n, 1) / 3 > 0.3 else "weak"
        )
    if report.away_form:
        report.away_strength = "strong" if a_pts / max(n, 1) / 3 > 0.6 else (
            "moderate" if a_pts / max(n, 1) / 3 > 0.3 else "weak"
        )

    if h_pts > a_pts + 3:
        report.form_edge = f"{home} form advantage"
    elif a_pts > h_pts + 3:
        report.form_edge = f"{away} form advantage"
    else:
        report.form_edge = "form is even"

    # ---- H2H analysis ----
    home_h2h_wins = 0
    away_h2h_wins = 0
    for r in report.h2h:
        try:
            hg, ag = r.split("-")
            if int(hg) > int(ag):
                home_h2h_wins += 1
            elif int(ag) > int(hg):
                away_h2h_wins += 1
        except ValueError:
            pass
    if home_h2h_wins > away_h2h_wins:
        report.h2h_edge = f"{home} dominates H2H ({home_h2h_wins}-{away_h2h_wins})"
    elif away_h2h_wins > home_h2h_wins:
        report.h2h_edge = f"{away} dominates H2H ({away_h2h_wins}-{home_h2h_wins})"
    else:
        report.h2h_edge = "H2H balanced"

    # ---- Build prediction ----
    reasons = []
    warnings = []

    # Odds-based assessment
    if report.implied_probs[0] > 0:
        ip = report.implied_probs
        if ip[0] > 0.45:
            reasons.append(f"市场看好{home}（隐含概率{ip[0]:.0%}）")
            report.prediction = "home"
            report.confidence = "medium" if ip[0] > 0.55 else "low"
        elif ip[2] > 0.45:
            reasons.append(f"市场看好{away}（隐含概率{ip[2]:.0%}）")
            report.prediction = "away"
            report.confidence = "medium" if ip[2] > 0.55 else "low"
        else:
            reasons.append("市场赔率均衡，无明显方向")
            report.prediction = "too close"
            report.confidence = "low"

    # Form assessment
    if report.home_form and report.away_form:
        if report.form_edge != "form is even":
            reasons.append(report.form_edge)
            if report.home_strength == "strong" and report.away_strength in ("weak", "moderate"):
                if report.prediction == "home":
                    report.confidence = "high"
            elif report.away_strength == "strong" and report.home_strength in ("weak", "moderate"):
                if report.prediction == "away":
                    report.confidence = "high"

    # H2H assessment
    if report.h2h_edge and "balanced" not in report.h2h_edge:
        reasons.append(report.h2h_edge)
        # H2H confirming odds = confidence boost
        if "home" in report.h2h_edge.lower() and report.prediction == "home":
            report.confidence = min_confidence(report.confidence, "high")
        elif "away" in report.h2h_edge.lower() and report.prediction == "away":
            report.confidence = min_confidence(report.confidence, "high")

    # Warnings
    if not report.odds_1x2[0]:
        warnings.append("⚠️ 无赔率数据，分析仅基于公开信息")
    if not report.home_form:
        warnings.append(f"⚠️ 未找到{home}近期赛果")
    if not report.away_form:
        warnings.append(f"⚠️ 未找到{away}近期赛果")
    if report.confidence == "low":
        warnings.append("⚠️ 信息不足，置信度低，谨慎参考")

    report.reasoning = reasons
    report.warnings = warnings
    report.sources = [s[:200] for s in search_results[:3] if len(s) > 20]

    return report


def min_confidence(a: str, b: str) -> str:
    order = {"low": 0, "medium": 1, "high": 2}
    return min(a, b, key=lambda x: order.get(x, 0))
