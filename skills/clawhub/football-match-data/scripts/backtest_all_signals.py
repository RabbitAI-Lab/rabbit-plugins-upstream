#!/usr/bin/env python
"""全信号历史回测 — 对 DB 中全部历史比赛批量计算 8 类信号并统计准确率。

用法:
  python scripts/backtest_all_signals.py            # 全部比赛
  python scripts/backtest_all_signals.py --league E0 # 仅英超
  python scripts/backtest_all_signals.py --min-odds 1.20 --max-odds 5.00

信号清单:
  1. Steam 方向        — 初盘→收盘赔率变化 vs 热门胜率
  2. O/U 双边水位       — over/under 水位联动 vs 大小球率
  3. O/U 盘路升降       — 大小球盘口线移动 vs 大小球率
  4. AH 盘路升降        — 亚盘盘口线移动 vs 上盘率
  5. Pinnacle 反向      — Pinnacle vs Bet365 Steam 背离 → 冷门率
  6. 离散度             — 赔率方差 vs 冷门率
  7. 初盘偏差           — 开盘 vs 公允价差距 vs 结果
  8. CLV 方向           — 收盘线价值方向 vs 实际结果
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# Ensure src is on path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))


# ── Data structures ────────────────────────────────────────────────────────

@dataclass
class SignalResult:
    name: str
    signal: str           # e.g. "涌入", "升盘", "浅开"
    category: str          # e.g. "Steam", "O/U双边"
    matches: int = 0
    hits: int = 0          # signal direction was correct
    total_pnl: float = 0.0 # flat 1-unit staking

    @property
    def accuracy(self) -> float:
        return self.hits / self.matches * 100 if self.matches else 0

    @property
    def roi(self) -> float:
        return self.total_pnl / self.matches * 100 if self.matches else 0


# ── Helpers ─────────────────────────────────────────────────────────────────

def _fav_idx(odds: tuple) -> int:
    """Index of the favorite (lowest odds)."""
    return min(range(3), key=lambda i: odds[i])


def _opposite_idx(fav: int) -> int:
    """Index of the opposite side (not favorite, not draw)."""
    if fav == 0:
        return 2
    elif fav == 2:
        return 0
    return 0  # draw is fav, pick home as opposite


def _result_to_idx(result: str) -> int:
    return {"H": 0, "D": 1, "A": 2}[result]


def _safe_odds(odds_dict: dict, book: str) -> Optional[tuple]:
    """Get (h,d,a) tuple for a bookmaker, or None."""
    val = odds_dict.get(book)
    if val and len(val) == 3 and all(v > 1.0 for v in val):
        return tuple(val)
    return None


def _safe_ou(odds_dict: dict, book: str) -> Optional[tuple]:
    """Get (over, under) tuple for O/U 2.5, or None."""
    val = odds_dict.get(book)
    if val and len(val) == 2 and all(v > 1.0 for v in val):
        return tuple(val)
    return None


# ── Signal computation functions ────────────────────────────────────────────

def steam_signal(open_odds, close_odds, book="B365") -> Optional[str]:
    """Return steam signal label for the favorite side."""
    oc = _safe_odds(open_odds, book)
    cc = _safe_odds(close_odds, book)
    if not oc or not cc:
        return None
    fi = _fav_idx(cc)
    steam = cc[fi] - oc[fi]
    if steam < -0.05:
        return "强涌入"
    elif steam < -0.02:
        return "涌入"
    elif steam > 0.05:
        return "强冷却"
    elif steam > 0.02:
        return "冷却"
    return "稳定"


def steam_did_fav_win(open_odds, close_odds, result, book="B365") -> Optional[bool]:
    """Did the favorite win when steam was in their direction?"""
    oc = _safe_odds(open_odds, book)
    cc = _safe_odds(close_odds, book)
    if not oc or not cc:
        return None
    fi = _fav_idx(cc)
    steam = cc[fi] - oc[fi]
    # Steam = odds dropping = money coming in = bullish for favorite
    fav_won = (fi == _result_to_idx(result))
    return fav_won


def ou_bilateral_signal(ou_odds, book="B365") -> Optional[str]:
    """O/U bilateral water signal."""
    ou = _safe_ou(ou_odds, book)
    if not ou:
        return None
    # Check if we have open O/U data too (from odds_open_json)
    # For now, use closing only — look for over/under imbalance
    over_odds, under_odds = ou
    if over_odds < 1.85 and under_odds > 2.05:
        return "大球热门"
    elif under_odds < 1.85 and over_odds > 2.05:
        return "小球热门"
    return "均衡"


def ou_line_signal(ah_data, book="B365") -> Optional[str]:
    """O/U line movement signal from AH data (which includes O/U in some CSVs)."""
    # Asian handicap data is stored as (line, home_water, away_water)
    # We need actual O/U line data from the CSV — not all matches have it
    # Try to extract from CSV OH columns
    return None  # O/U line data not reliably in DB


def ah_line_signal(ah_data) -> Optional[str]:
    """AH line movement signal."""
    # AH data stored as dict[book] = (line, home_water, away_water)
    # We only have closing AH, not opening — can't compute movement
    return None


def pinnacle_reversal(open_odds, close_odds, result) -> Optional[bool]:
    """Check if Pinnacle odds moved opposite to Bet365, and if favorite lost."""
    po = _safe_odds(open_odds, "PS")
    pc = _safe_odds(close_odds, "PS")
    bo = _safe_odds(open_odds, "B365")
    bc = _safe_odds(close_odds, "B365")
    if not all([po, pc, bo, bc]):
        return None
    fi = _fav_idx(pc)
    ps_steam = pc[fi] - po[fi]
    b365_steam = bc[fi] - bo[fi]
    # Pinnacle reversal: one is positive (cooling) while other is negative (steaming)
    reversal = (ps_steam < -0.02 and b365_steam > 0.02) or (ps_steam > 0.02 and b365_steam < -0.02)
    if not reversal:
        return None
    fav_won = (fi == _result_to_idx(result))
    return not fav_won  # True = cold/upset happened


def dispersion(close_odds) -> Optional[float]:
    """Coefficient of variation of home odds across available bookmakers."""
    if not close_odds:
        return None
    h_vals = [v[0] for v in close_odds.values() if len(v) == 3 and v[0] > 1.0]
    if len(h_vals) < 3:
        return None
    mean_h = sum(h_vals) / len(h_vals)
    if mean_h == 0:
        return None
    cv = (max(h_vals) - min(h_vals)) / mean_h
    return cv


def opening_deviation(open_odds) -> Optional[str]:
    """Classify opening deviation: 浅开 (shallow) or 深开 (deep)."""
    oc = _safe_odds(open_odds, "B365")
    if not oc:
        return None
    # Implied probabilities
    h, d, a = oc
    imp_sum = 1/h + 1/d + 1/a
    ph = (1/h) / imp_sum
    pa = (1/a) / imp_sum
    # If home is heavy favorite but odds aren't that low
    gap = abs(ph - pa)
    if gap > 0.50:
        return "深开"  # big gap = deep line
    elif gap < 0.10:
        return "浅开"  # small gap = shallow line
    return "正常"


def clv_signal(open_odds, close_odds, book="B365") -> Optional[str]:
    """CLV direction for the favorite."""
    oc = _safe_odds(open_odds, book)
    cc = _safe_odds(close_odds, book)
    if not oc or not cc:
        return None
    fi = _fav_idx(cc)
    clv = (cc[fi] - oc[fi]) / oc[fi]
    if clv < -0.05:
        return "正CLV"  # odds dropped = good for favorite
    elif clv > 0.05:
        return "负CLV"
    return "平CLV"


# ── Main backtest ───────────────────────────────────────────────────────────

def run_backtest(matches, league_filter=None, min_odds=1.10, max_odds=10.0):
    """Run all 8 signal backtests over a list of matches.

    Returns dict: category -> signal -> SignalResult
    """
    results: dict[str, dict[str, SignalResult]] = defaultdict(dict)

    for m in matches:
        if league_filter and m.league != league_filter:
            continue
        if not m.is_finished:
            continue
        result = m.result
        if not result:
            continue

        close = m.odds_1x2
        open_ = m.odds_open_1x2
        ou_cl = m.odds_ou25
        ah = m.asian_handicap

        # Odds filter
        bc = _safe_odds(close, "B365")
        if not bc:
            continue
        fi = _fav_idx(bc)
        if bc[fi] < min_odds or bc[fi] > max_odds:
            continue

        # ── 1. Steam ──
        if open_:
            sig = steam_signal(open_, close)
            if sig:
                fav_won = steam_did_fav_win(open_, close, result)
                if fav_won is not None:
                    key = sig
                    if key not in results["Steam"]:
                        results["Steam"][key] = SignalResult("Steam方向", key, "Steam")
                    r = results["Steam"][key]
                    r.matches += 1
                    if fav_won:
                        r.hits += 1
                        r.total_pnl += (bc[fi] - 1.0)
                    else:
                        r.total_pnl -= 1.0

        # ── 2. O/U 双边 ──
        if ou_cl:
            sig = ou_bilateral_signal(ou_cl)
            if sig and sig != "均衡":
                total_goals = (m.home_goals or 0) + (m.away_goals or 0)
                over_hit = total_goals > 2.5
                correct = (sig == "大球热门" and over_hit) or (sig == "小球热门" and not over_hit)
                ou_odds = _safe_ou(ou_cl, "B365") or _safe_ou(ou_cl, "Avg")
                settle_odds = 0
                if ou_odds:
                    settle_odds = ou_odds[0] if sig == "大球热门" else ou_odds[1]
                key = sig
                if key not in results["O/U双边"]:
                    results["O/U双边"][key] = SignalResult("O/U双边水位", key, "O/U双边")
                r = results["O/U双边"][key]
                r.matches += 1
                if correct:
                    r.hits += 1
                    r.total_pnl += (settle_odds - 1.0) if settle_odds > 0 else 0
                else:
                    r.total_pnl -= 1.0

        # ── 5. Pinnacle 反向 ──
        if open_:
            is_cold = pinnacle_reversal(open_, close, result)
            if is_cold is not None:
                key = "Pinnacle反向"
                if key not in results["Pinnacle"]:
                    results["Pinnacle"][key] = SignalResult("Pinnacle反向", key, "Pinnacle")
                r = results["Pinnacle"][key]
                r.matches += 1
                if is_cold:
                    r.hits += 1  # cold happened → signal correct

        # ── 6. 离散度 ──
        cv = dispersion(close)
        if cv is not None:
            if cv > 0.20:
                key = "高离散"
            elif cv > 0.10:
                key = "中离散"
            else:
                key = "低离散"
            fav_won = (fi == _result_to_idx(result))
            if key not in results["离散度"]:
                results["离散度"][key] = SignalResult("离散度", key, "离散度")
            r = results["离散度"][key]
            r.matches += 1
            # High dispersion = more uncertainty = cold more likely
            if key == "高离散":
                if not fav_won:
                    r.hits += 1
            else:
                if fav_won:
                    r.hits += 1

        # ── 7. 初盘偏差 ──
        if open_:
            sig = opening_deviation(open_)
            if sig and sig != "正常":
                fav_won = (fi == _result_to_idx(result))
                key = sig
                if key not in results["初盘偏差"]:
                    results["初盘偏差"][key] = SignalResult("初盘偏差", key, "初盘偏差")
                r = results["初盘偏差"][key]
                r.matches += 1
                if fav_won:
                    r.hits += 1

        # ── 8. CLV ──
        if open_:
            sig = clv_signal(open_, close)
            if sig and sig != "平CLV":
                fav_won = (fi == _result_to_idx(result))
                key = sig
                if key not in results["CLV"]:
                    results["CLV"][key] = SignalResult("CLV方向", key, "CLV")
                r = results["CLV"][key]
                r.matches += 1
                if (sig == "正CLV" and fav_won) or (sig == "负CLV" and not fav_won):
                    r.hits += 1

    return results


# ── Report ──────────────────────────────────────────────────────────────────

def print_report(results: dict, total_matches: int):
    """Print a formatted backtest report."""
    print()
    print("═" * 70)
    print(f"  全信号历史回测报告 ({total_matches} 场, 五大联赛)")
    print("═" * 70)

    categories_order = ["Steam", "O/U双边", "Pinnacle", "离散度", "初盘偏差", "CLV"]

    for cat in categories_order:
        if cat not in results or not results[cat]:
            continue
        print(f"\n📊 {cat}")
        print(f"  {'信号':<16} {'场次':>6} {'命中':>6} {'准确率':>8} {'ROI':>8}")
        print(f"  {'─' * 16} {'─' * 6} {'─' * 6} {'─' * 8} {'─' * 8}")
        for key, sr in sorted(results[cat].items(), key=lambda x: -x[1].matches):
            print(
                f"  {key:<16} {sr.matches:>6} {sr.hits:>6} "
                f"{sr.accuracy:>7.1f}% {sr.roi:>7.1f}%"
            )

    print()
    print("═" * 70)
    print("  🏆 信号强度排名 (按准确率, 最少30场)")
    print("═" * 70)

    all_signals = []
    for cat_results in results.values():
        for sr in cat_results.values():
            if sr.matches >= 30:
                all_signals.append(sr)
    all_signals.sort(key=lambda x: -x.accuracy)

    print(f"  {'排名':<4} {'信号':<24} {'场次':>6} {'准确率':>8} {'ROI':>8}")
    print(f"  {'─' * 4} {'─' * 24} {'─' * 6} {'─' * 8} {'─' * 8}")
    for i, sr in enumerate(all_signals[:15], 1):
        print(
            f"  {i:<4} {sr.category+'/'+sr.signal:<24} {sr.matches:>6} "
            f"{sr.accuracy:>7.1f}% {sr.roi:>7.1f}%"
        )

    print()


# ── CLI ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="全信号历史回测")
    parser.add_argument("--league", default=None, help="联赛代码 (E0/SP1/I1/D1/F1)")
    parser.add_argument("--min-odds", type=float, default=1.10, help="最低赔率")
    parser.add_argument("--max-odds", type=float, default=10.0, help="最高赔率")
    parser.add_argument("--save", action="store_true", help="保存结果到 state.json")
    args = parser.parse_args()

    from footy.data.store import get_matches

    print("📡 加载历史比赛数据...")
    matches = get_matches(finished_only=True)
    print(f"   共 {len(matches)} 场完场比赛")

    # Filter to matches with Pinnacle closing odds
    valid = [m for m in matches if _safe_odds(m.odds_1x2, "B365")]
    print(f"   其中 {len(valid)} 场有 Bet365 收盘赔率")

    results = run_backtest(valid, args.league, args.min_odds, args.max_odds)
    print_report(results, len(valid))

    if args.save:
        from footy.config import DATA_DIR
        import json as _json
        state_path = DATA_DIR / "state.json"
        if state_path.exists():
            state = _json.loads(state_path.read_text(encoding="utf-8"))
        else:
            state = {}
        # Convert results to serializable dict
        backtest_data = {}
        for cat, sigs in results.items():
            backtest_data[cat] = {}
            for key, sr in sigs.items():
                backtest_data[cat][key] = {
                    "matches": sr.matches,
                    "hits": sr.hits,
                    "accuracy": round(sr.accuracy, 1),
                    "roi": round(sr.roi, 1),
                }
        state["backtest"] = backtest_data
        state["last_updated"] = __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat()
        state_path.write_text(_json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"✅ 回测结果已保存到 {state_path}")
