"""基本面自动采集模块 — 填充清单 19-23 项（伤停/阵容/状态/出线/心理）。

数据源：
  19 伤停  — nowscore Infocat (intel.py)
  20 阵容  — nowscore Infocat (阵型+首发提示)
  21 状态  — SQLite DB 历史比赛 (form.py 近期战绩)
  22 出线  — DB 联赛排名推断
  23 心理  — 连胜/连败/不败趋势分析
"""
from __future__ import annotations

import logging
from datetime import date, timedelta
from typing import Optional

log = logging.getLogger(__name__)


def auto_fill_fundamentals(data) -> int:
    """Auto-fill checklist items 19-23 from available fundamental data sources.

    Args:
        data: MatchData with at minimum .fixture_id, .home, .away, .checklist

    Returns:
        Number of items filled (max 5).
    """
    cl = data.checklist
    filled = 0
    home = data.home or ""
    away = data.away or ""

    # ------------------------------------------------------------------
    # 19 + 20: 伤停 + 阵容 (try nowscore Infocat)
    # ------------------------------------------------------------------
    intel = _try_fetch_intel(data.fixture_id)
    if intel and (intel.home_absences or intel.away_absences or intel.home_formation):
        # Item 19 — 伤停
        h_abs = len(intel.home_absences)
        a_abs = len(intel.away_absences)
        h_imp = intel.home_impact_score
        a_imp = intel.away_impact_score
        if h_abs + a_abs > 0:
            cl.mark(
                "19",
                f"主{h_abs}人缺阵(影响{h_imp:.1f}), 客{a_abs}人缺阵(影响{a_imp:.1f})",
                status="⚠️" if (h_abs >= 2 or a_abs >= 2) else "✅",
            )
        else:
            cl.mark("19", "双方无重大伤停", status="✅")
        filled += 1

        # Item 20 — 阵容
        parts = []
        if intel.home_formation:
            parts.append(f"主{intel.home_formation}")
        if intel.away_formation:
            parts.append(f"客{intel.away_formation}")
        if intel.home_lineup_hints or intel.away_lineup_hints:
            total_hints = len(intel.home_lineup_hints) + len(intel.away_lineup_hints)
            parts.append(f"{total_hints}条阵容线索")
        if parts:
            cl.mark("20", " | ".join(parts))
        else:
            cl.mark("20", "阵型/阵容待确认", status="⚠️")
        filled += 1
    else:
        cl.mark("19", "待手动采集(Infocat无数据)", status="⚠️")
        cl.mark("20", "待手动采集(Infocat无数据)", status="⚠️")
        filled += 2

    # ------------------------------------------------------------------
    # 21: 近期状态 (from DB)
    # ------------------------------------------------------------------
    try:
        hf, af = _compute_both_forms(home, away)
        if hf and af:
            h_trend = _trend_label(hf.trend)
            a_trend = _trend_label(af.trend)
            cl.mark(
                "21",
                f"主{hf.ppg:.1f}分/场(GF{hf.avg_gf:.1f}/GA{hf.avg_ga:.1f}, {h_trend}), "
                f"客{af.ppg:.1f}分/场(GF{af.avg_gf:.1f}/GA{af.avg_ga:.1f}, {a_trend})",
            )
            filled += 1
        elif hf:
            cl.mark("21", f"主{hf.ppg:.1f}分/场(GF{hf.avg_gf:.1f}/GA{hf.avg_ga:.1f}), 客无数据", status="⚠️")
            filled += 1
        elif af:
            cl.mark("21", f"主无数据, 客{af.ppg:.1f}分/场(GF{af.avg_gf:.1f}/GA{af.avg_ga:.1f})", status="⚠️")
            filled += 1
        else:
            cl.mark("21", "待手动采集(无历史数据)", status="⚠️")
    except Exception:
        cl.mark("21", "待手动采集(无法计算状态)", status="⚠️")

    # ------------------------------------------------------------------
    # 22: 出线形势 (basic league-position inference)
    # ------------------------------------------------------------------
    try:
        pos_info = _infer_positions(home, away)
        if pos_info:
            cl.mark("22", pos_info)
        else:
            cl.mark("22", "待手动采集(无联赛积分数据)", status="⚠️")
    except Exception:
        cl.mark("22", "待手动采集(无法推断出线形势)", status="⚠️")

    # ------------------------------------------------------------------
    # 23: 心理惯性 (streak analysis)
    # ------------------------------------------------------------------
    try:
        streak_info = _analyze_streaks(home, away)
        if streak_info:
            cl.mark("23", streak_info)
            filled += 1
        else:
            cl.mark("23", "待手动采集(无历史数据)", status="⚠️")
    except Exception:
        cl.mark("23", "待手动采集(无法分析心理惯性)", status="⚠️")

    return filled


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _try_fetch_intel(fixture_id: str):
    """Attempt to fetch intel from nowscore Infocat. Returns MatchIntel or None."""
    try:
        from footy.data.intel import fetch_intel
        return fetch_intel(fixture_id)
    except Exception as exc:
        log.debug("Infocat fetch failed for %s: %s", fixture_id, exc)
        return None


def _compute_both_forms(home: str, away: str):
    """Return (home_TeamForm, away_TeamForm) or (None, None)."""
    if not home or not away:
        return None, None
    try:
        from footy.data.store import get_matches
        from footy.models.form import compute_form

        # Use today as reference date — form model only looks at past matches
        ref_date = date.today().isoformat()
        matches = get_matches(finished_only=True)
        if not matches:
            return None, None

        hf = compute_form(matches, home, ref_date, window=6)
        af = compute_form(matches, away, ref_date, window=6)
        return hf, af
    except Exception as exc:
        log.debug("Form computation failed for %s/%s: %s", home, away, exc)
        return None, None


def _trend_label(trend: float) -> str:
    """Convert a trend slope to a Chinese label."""
    if trend > 0.20:
        return "↑强上升"
    elif trend > 0.05:
        return "↑上升"
    elif trend < -0.20:
        return "↓强下降"
    elif trend < -0.05:
        return "↓下降"
    else:
        return "→平稳"


def _infer_positions(home: str, away: str) -> str:
    """Basic league-position inference from DB match data."""
    try:
        from footy.data.store import get_conn

        with get_conn() as conn:
            # Count wins/draws/losses for each team from finished matches
            for team, label in [(home, "主"), (away, "客")]:
                pass  # placeholder

            # Simple approach: count total wins in DB for each team
            cur = conn.execute(
                """SELECT
                     SUM(CASE WHEN home = ? AND home_goals > away_goals THEN 1
                              WHEN away = ? AND away_goals > home_goals THEN 1 ELSE 0 END) as wins,
                     COUNT(*) as total
                 FROM matches
                 WHERE home_goals IS NOT NULL AND (home = ? OR away = ?)""",
                (home, home, home, home),
            )
            h_row = cur.fetchone()
            cur = conn.execute(
                """SELECT
                     SUM(CASE WHEN home = ? AND home_goals > away_goals THEN 1
                              WHEN away = ? AND away_goals > home_goals THEN 1 ELSE 0 END) as wins,
                     COUNT(*) as total
                 FROM matches
                 WHERE home_goals IS NOT NULL AND (home = ? OR away = ?)""",
                (away, away, away, away),
            )
            a_row = cur.fetchone()

            if h_row and a_row and h_row["total"] >= 5 and a_row["total"] >= 5:
                h_wr = h_row["wins"] / h_row["total"] * 100
                a_wr = a_row["wins"] / a_row["total"] * 100
                return f"主队胜率{h_wr:.0f}%({h_row['total']}场), 客队胜率{a_wr:.0f}%({a_row['total']}场)"
    except Exception as exc:
        log.debug("Position inference failed: %s", exc)

    return ""


def _analyze_streaks(home: str, away: str) -> str:
    """Analyze recent result streaks for both teams."""
    try:
        from footy.data.store import get_matches

        matches = get_matches(finished_only=True)
        if not matches:
            return ""

        h_streak = _team_streak(matches, home)
        a_streak = _team_streak(matches, away)

        parts = []
        if h_streak:
            parts.append(f"主{h_streak}")
        if a_streak:
            parts.append(f"客{a_streak}")

        if not parts:
            return ""

        # Determine psychological edge
        h_good = "胜" in (h_streak or "") or "不败" in (h_streak or "")
        a_good = "胜" in (a_streak or "") or "不败" in (a_streak or "")
        if h_good and not a_good:
            parts.append("心理优势在主队")
        elif a_good and not h_good:
            parts.append("心理优势在客队")

        return ", ".join(parts)
    except Exception as exc:
        log.debug("Streak analysis failed: %s", exc)
        return ""


def _team_streak(matches, team: str) -> str:
    """Return a streak label for the team's most recent matches, e.g. '3连胜' or '2场不胜'."""
    # Filter team's matches, sorted by date descending
    team_matches = [
        m for m in matches
        if (m.home == team or m.away == team) and m.is_finished
    ]
    if not team_matches:
        return ""
    team_matches.sort(key=lambda m: m.date, reverse=True)

    # Analyse last 5 matches
    recent = team_matches[:5]
    results = []
    for m in recent:
        if m.home == team:
            if m.home_goals > m.away_goals:
                results.append("W")
            elif m.home_goals < m.away_goals:
                results.append("L")
            else:
                results.append("D")
        else:
            if m.away_goals > m.home_goals:
                results.append("W")
            elif m.away_goals < m.home_goals:
                results.append("L")
            else:
                results.append("D")

    if not results:
        return ""

    # Count current streak
    first = results[0]
    streak = 1
    for r in results[1:]:
        if r == first:
            streak += 1
        else:
            break

    if first == "W":
        return f"{streak}连胜" if streak >= 2 else "上场取胜"
    elif first == "L":
        return f"{streak}连败" if streak >= 2 else "上场失利"
    elif first == "D":
        return f"{streak}连平" if streak >= 2 else "上场平局"

    # Mixed — check unbeaten streak
    unbeaten = 0
    for r in results:
        if r in ("W", "D"):
            unbeaten += 1
        else:
            break
    if unbeaten >= 3:
        return f"{unbeaten}场不败"

    winless = 0
    for r in results:
        if r in ("L", "D"):
            winless += 1
        else:
            break
    if winless >= 3:
        return f"{winless}场不胜"

    return ""
