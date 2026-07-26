"""自动信号检测引擎 — 一键填充所有可自动计算的维度。

覆盖维度 (23/30):
  01 欧赔数据     08 Steam        12 大小球盘口    13 大小球水位
  02 去水         03 凯利指数     06 离散度        07 隐含概率
  04 凯利方差     05 凯利方向     09 升盘降水      10 退盘升水
  11 阻控诱判定   14 欧亚偏差     15 赔率骨架      16 高级亚盘(四模)
  17 冷门检测     18 庄家意图     24 CLV           25 初盘偏差
  26 欧亚联动     27 返还率        28 泊松比分      29 EV/Edge
  30 必发四步     08a 亚盘数据

手动维度 (7/30):
  19 伤停         20 阵容首发    21 近期状态
  22 出线形势     23 心理惯性

用法:
  from footy.analysis.auto_signals import auto_fill_checklist
  auto_fill_checklist(data)  # 自动填23项
  data.checklist.missing_items()  # 剩7项手动
"""
from __future__ import annotations

import math
import re
import urllib.request
from dataclasses import dataclass, field
from typing import Optional

from footy.models.loader import load_fitted_model, find_most_likely_score
from footy.analysis.cold_detector import detect_cold


# ---- Data Structures ----

@dataclass
class PinnacleCheck:
    pinnacle_odds: tuple = (0, 0, 0)
    pinnacle_open: tuple = (0, 0, 0)
    bet365_odds: tuple = (0, 0, 0)
    bet365_open: tuple = (0, 0, 0)
    pinnacle_steam: float = 0.0
    bet365_steam: float = 0.0
    same_direction: bool = True
    alert: str = ""


@dataclass
class OUBilateralSignal:
    over_drops: int = 0
    over_rises: int = 0
    under_drops: int = 0
    under_rises: int = 0
    total: int = 0
    bilateral: str = ""
    backtest_rate: float = 0.0
    verdict: str = ""


@dataclass
class AsianTrapSignal:
    line_up: int = 0
    line_down: int = 0
    upper_water_drops: int = 0
    upper_water_rises: int = 0
    total: int = 0
    trap_type: str = ""
    verdict: str = ""
    # Extracted line/water values for downstream analysis (cold detector, advanced AH)
    avg_open_line: float = 0.0   # average opening handicap line (home perspective)
    avg_close_line: float = 0.0  # average current handicap line
    avg_open_water_fav: float = 0.90  # average opening water for favorite side
    avg_close_water_fav: float = 0.90  # average current water for favorite side


@dataclass
class MatchSignals:
    match_name: str = ""
    fixture_id: str = ""
    pinnacle: PinnacleCheck = field(default_factory=PinnacleCheck)
    ou_signal: OUBilateralSignal = field(default_factory=OUBilateralSignal)
    ah_signal: AsianTrapSignal = field(default_factory=AsianTrapSignal)
    euro_ah_deviation: bool = False
    euro_ah_detail: str = ""
    warnings: list[str] = field(default_factory=list)


# ---- Pinnacle Check ----

def check_pinnacle(fixture_id: str) -> PinnacleCheck:
    result = PinnacleCheck()
    try:
        from footy.data.wubai import get_odds_full
        full = get_odds_full(fixture_id)
        cur = full.get("current", {})
        opn = full.get("opening", {})
        if "Pinnacle" in cur and "Bet365" in cur:
            pc, po = cur["Pinnacle"], opn.get("Pinnacle", cur["Pinnacle"])
            bc, bo = cur["Bet365"], opn.get("Bet365", cur["Bet365"])
            result.pinnacle_odds, result.pinnacle_open = pc, po
            result.bet365_odds, result.bet365_open = bc, bo
            fav_idx = min(range(3), key=lambda i: bc[i])
            result.pinnacle_steam = pc[fav_idx] - po[fav_idx]
            result.bet365_steam = bc[fav_idx] - bo[fav_idx]
            p_dir, b_dir = result.pinnacle_steam < -0.02, result.bet365_steam < -0.02
            result.same_direction = (p_dir == b_dir)
            if not result.same_direction:
                fav_name = ["主胜", "平局", "客胜"][fav_idx]
                result.alert = (
                    f"🚨 Pinnacle反向! Pinnacle Steam={result.pinnacle_steam:+.2f} "
                    f"vs Bet365 Steam={result.bet365_steam:+.2f} ({fav_name})"
                )
    except Exception as e:
        result.alert = f"Pinnacle检测失败: {e}"
    return result


# ---- O/U Bilateral ----

def check_ou_bilateral(fixture_id: str) -> OUBilateralSignal:
    result = OUBilateralSignal()
    try:
        from footy.data.ou_data import fetch_ou
        ou = fetch_ou(fixture_id)
        if not ou or not ou.bookmakers:
            result.verdict = "无O/U数据"
            return result
        n = len(ou.bookmakers)
        result.total = n
        for b in ou.bookmakers:
            if b.current_over < b.open_over - 0.03:
                result.over_drops += 1
            elif b.current_over > b.open_over + 0.03:
                result.over_rises += 1
            if b.current_under < b.open_under - 0.03:
                result.under_drops += 1
            elif b.current_under > b.open_under + 0.03:
                result.under_rises += 1
        if result.over_drops >= n * 0.4 and result.under_rises >= n * 0.4:
            result.bilateral = "大球降水+小球升水"
            result.backtest_rate = 63.0
            result.verdict = f"🟢 看好大球 (双边确认, 回测{result.backtest_rate:.0f}%大球率)"
        elif result.over_rises >= n * 0.4 and result.under_drops >= n * 0.4:
            result.bilateral = "大球升水+小球降水"
            result.backtest_rate = 51.7
            result.verdict = f"🔴 偏小球 (双边确认但弱, 回测{result.backtest_rate:.0f}%小球率)"
        else:
            result.verdict = "⚪ 无双边信号, O/U不下注"
    except Exception as e:
        result.verdict = f"O/U检测失败: {e}"
    return result


# ---- Asian Handicap Trap ----

def check_ah_trap(fixture_id: str, favorite_side: str = "away") -> AsianTrapSignal:
    result = AsianTrapSignal()
    try:
        url = f"https://odds.500.com/fenxi/yazhi-{fixture_id}.shtml"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            html = r.read().decode("gb2312", errors="replace")
        marker = re.compile(r'<tr\s+class="tr[12]"[^>]*id="(\d+)"', re.IGNORECASE)
        ah_data = []
        for m in marker.finditer(html):
            start = m.start()
            depth = 0; pos = start
            while pos < len(html):
                no = html.find("<tr", pos); nc = html.find("</tr>", pos)
                if no == start: pos = no + 3; depth = 1; continue
                if nc < 0: break
                if no >= 0 and no < nc: depth += 1; pos = no + 3
                else:
                    depth -= 1
                    if depth == 0:
                        row = html[start:nc + 5]
                        break
                    pos = nc + 5
            tables = re.findall(r'<table[^>]*class="pl_table_data"[^>]*>(.*?)</table>', row, re.DOTALL)
            if len(tables) < 2: continue
            def parse(tbl):
                tds = re.findall(r'<td[^>]*>(.*?)</td>', tbl, re.DOTALL)
                if len(tds) < 3: return None
                ref_m = re.search(r'ref="([^"]+)"', tbl)
                line = float(ref_m.group(1)) if ref_m else 0
                h_m = re.search(r'(\d+\.?\d*)', tds[0])
                a_m = re.search(r'(\d+\.?\d*)', tds[2])
                return (float(h_m.group(1)), line, float(a_m.group(1))) if h_m and a_m else None
            cur_ah = parse(tables[0]); opn_ah = parse(tables[1])
            if cur_ah and opn_ah:
                ah_data.append((opn_ah, cur_ah))
        if not ah_data:
            result.verdict = "无亚盘数据"
            return result
        n = len(ah_data)
        result.total = n
        upper_idx = 2 if favorite_side == "away" else 0
        # Aggregate line & water values for downstream modules
        open_lines, close_lines = [], []
        open_waters, close_waters = [], []
        for opn, cur in ah_data:
            # Use abs() — deeper handicap = 升盘 regardless of sign
            if abs(cur[1]) > abs(opn[1]) + 0.02: result.line_up += 1
            elif abs(cur[1]) < abs(opn[1]) - 0.02: result.line_down += 1
            if cur[upper_idx] < opn[upper_idx] - 0.02: result.upper_water_drops += 1
            elif cur[upper_idx] > opn[upper_idx] + 0.02: result.upper_water_rises += 1
            open_lines.append(opn[1])
            close_lines.append(cur[1])
            open_waters.append(opn[upper_idx])
            close_waters.append(cur[upper_idx])
        if open_lines:
            result.avg_open_line = sum(open_lines) / len(open_lines)
            result.avg_close_line = sum(close_lines) / len(close_lines)
            result.avg_open_water_fav = sum(open_waters) / len(open_waters)
            result.avg_close_water_fav = sum(close_waters) / len(close_waters)
        if result.line_up >= n * 0.5:
            if result.upper_water_rises >= n * 0.4:
                result.trap_type, result.verdict = "诱上盘", "⚠️ 升盘+上盘升水 → 诱上盘, 下盘有机会"
            elif result.upper_water_drops >= n * 0.4:
                result.trap_type, result.verdict = "真升", "🟢 升盘+上盘降水 → 看好上盘"
            else:
                result.verdict = "升盘(水位混杂)"
        elif result.line_down >= n * 0.5:
            if result.upper_water_rises >= n * 0.4:
                result.trap_type, result.verdict = "真降", "🔴 降盘+上盘升水 → 看好下盘"
            elif result.upper_water_drops >= n * 0.4:
                result.trap_type, result.verdict = "诱下盘", "⚠️ 降盘+上盘降水 → 诱下盘, 上盘有机会"
            else:
                result.verdict = "降盘(水位混杂)"
        else:
            result.verdict = "盘口稳定"
    except Exception as e:
        result.verdict = f"亚盘检测失败: {e}"
    return result


# ---- Full Scan ----

def scan_match(fixture_id: str, match_name: str = "",
               favorite_side: str = "away") -> MatchSignals:
    import os
    if not os.environ.get("AMPAN_PAID"):
        raise RuntimeError("请通过 /ampan 支付流程使用本服务")
    result = MatchSignals(match_name=match_name, fixture_id=fixture_id)
    result.pinnacle = check_pinnacle(fixture_id)
    if result.pinnacle.alert:
        result.warnings.append(result.pinnacle.alert)
    result.ou_signal = check_ou_bilateral(fixture_id)
    result.ah_signal = check_ah_trap(fixture_id, favorite_side)
    if "诱" in result.ah_signal.trap_type:
        result.warnings.append(f"亚盘: {result.ah_signal.verdict}")
    # Euro-AH deviation
    try:
        from .euro_ah import detect_deviation
        from footy.data.wubai import get_odds_full
        full = get_odds_full(fixture_id)
        cur = full.get("current", {})
        if "Bet365" in cur:
            bc = cur["Bet365"]
            url_ah = f"https://odds.500.com/fenxi/yazhi-{fixture_id}.shtml"
            req_ah = urllib.request.Request(url_ah, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req_ah, timeout=10) as r_ah:
                html_ah = r_ah.read().decode("gb2312", errors="replace")
            marker_ah = re.compile(r'<tr\s+class="tr[12]"[^>]*id="(\d+)"', re.IGNORECASE)
            first_ah = marker_ah.search(html_ah)
            if first_ah:
                start_ah = first_ah.start()
                depth_ah = 0; pos_ah = start_ah
                while pos_ah < len(html_ah):
                    no_ah = html_ah.find("<tr", pos_ah); nc_ah = html_ah.find("</tr>", pos_ah)
                    if no_ah == start_ah: pos_ah = no_ah + 3; depth_ah = 1; continue
                    if nc_ah < 0: break
                    if no_ah >= 0 and no_ah < nc_ah: depth_ah += 1; pos_ah = no_ah + 3
                    else:
                        depth_ah -= 1
                        if depth_ah == 0:
                            row_ah = html_ah[start_ah:nc_ah + 5]
                            break
                        pos_ah = nc_ah + 5
                tables_ah = re.findall(r'<table[^>]*class="pl_table_data"[^>]*>(.*?)</table>', row_ah, re.DOTALL)
                if len(tables_ah) >= 2:
                    ref_ah = re.search(r'ref="([^"]+)"', tables_ah[0])
                    if ref_ah:
                        dev = detect_deviation(bc[0], bc[1], bc[2], float(ref_ah.group(1)))
                        if dev and dev.signal in ("深开", "浅开") and dev.severity == "high":
                            result.euro_ah_deviation = True
                            result.euro_ah_detail = f"{dev.signal} {abs(dev.deviation):.2f}球"
                            result.warnings.append(f"欧亚偏离: {dev.signal} {abs(dev.deviation):.2f}球 — {dev.interpretation[:80]}")
    except Exception:
        pass
    return result


# ============================================================
#  AUTO-FILL CHECKLIST: fills all 20 computable dimensions
# ============================================================

def auto_fill_checklist(data) -> int:
    """Auto-fill all computable checklist items. Returns count of items filled.

    Call after odds, O/U, and AH data have been loaded into MatchData.
    """
    cl = data.checklist
    filled = 0
    warnings_list = []

    try:
        from footy.data.wubai import get_odds_full
        full = get_odds_full(data.fixture_id)
        cur_odds = full.get("current", {})
        opn_odds = full.get("opening", {})
    except Exception:
        cur_odds, opn_odds = {}, {}

    # ---- 01: 欧赔数据 ----
    if data.odds_count >= 5:
        cl.mark("01", f"{data.odds_count}家公司")
        filled += 1

    # ---- 08: Steam ----
    if data.odds_instant and data.odds_opening:
        fav_idx = min(range(3), key=lambda i: data.odds_instant[i])
        fav_name = ["主胜", "平局", "客胜"][fav_idx]
        steam = data.odds_instant[fav_idx] - data.odds_opening[fav_idx]
        direction = "涌入" if steam < -0.02 else ("冷却" if steam > 0.02 else "稳定")
        magnitude = "海啸" if abs(steam) > 0.3 else ("强" if abs(steam) > 0.1 else "中")
        cl.mark("08", f"{fav_name} {direction} {magnitude} ({steam:+.2f})")
        filled += 1

    # ---- 08a: 亚盘数据 ----
    if data.ah_verified:
        cl.mark("08a", "已采集")
        filled += 1

    # ---- 12/13: O/U ----
    if data.ou_verified and data.ou_data:
        cl.mark("12", f"{data.ou_data.get('company_count', 0)}家, 均线{data.ou_data.get('avg_current_line', 0):.2f}")
        cl.mark("13", data.ou_data.get("trend", ""))
        filled += 2

    # ---- 02: 去水 (de-vig) ----
    if data.odds_instant:
        h, d, a = data.odds_instant
        imp_sum = 1/h + 1/d + 1/a
        payout = 1 / imp_sum
        cl.mark("02", f"返还率{payout:.1%}")
        filled += 1

    # ---- 07: 隐含概率 ----
    if data.odds_instant:
        h, d, a = data.odds_instant
        imp_sum = 1/h + 1/d + 1/a
        ph, pd, pa = (1/h)/imp_sum*100, (1/d)/imp_sum*100, (1/a)/imp_sum*100
        cl.mark("07", f"主{ph:.0f}%/平{pd:.0f}%/客{pa:.0f}%")
        filled += 1

    # ---- 03/05: 凯利 ----
    if data.odds_instant:
        h, d, a = data.odds_instant
        imp_sum = 1/h + 1/d + 1/a
        payout = 1 / imp_sum
        fav_idx = min(range(3), key=lambda i: data.odds_instant[i])
        fav_odds = data.odds_instant[fav_idx]
        fav_prob = (1/fav_odds) / imp_sum
        kelly = (fav_prob * fav_odds - 1) / (fav_odds - 1) * 0.25
        ev_status = "正EV" if kelly > 0.005 else ("负EV" if kelly < -0.005 else "平水")
        cl.mark("03", f"热门凯利25%={kelly:.4f} ({ev_status})")
        kelly_dir = "看好" if kelly > 0 else "不看好"
        cl.mark("05", f"{kelly_dir}热门方向")
        filled += 2

    # ---- 04: 凯利方差 ----
    if len(cur_odds) >= 5:
        kellys = []
        for name, odds in cur_odds.items():
            imp_s = 1/odds[0] + 1/odds[1] + 1/odds[2]
            fav_i = min(range(3), key=lambda i: odds[i])
            fav_o = odds[fav_i]
            fav_p = (1/fav_o) / imp_s
            k = (fav_p * fav_o - 1) / (fav_o - 1) * 0.25
            kellys.append(k)
        if kellys:
            var = sum((k - sum(kellys)/len(kellys))**2 for k in kellys) / len(kellys)
            cl.mark("04", f"方差{var:.6f}")
            filled += 1

    # ---- 06: 离散度 ----
    if len(cur_odds) >= 5:
        h_vals = [v[0] for v in cur_odds.values()]
        cv = (max(h_vals)-min(h_vals)) / (sum(h_vals)/len(h_vals)) if sum(h_vals) > 0 else 0
        cl.mark("06", f"CV={cv:.2f} {'⚠️偏高' if cv > 0.15 else '✅'}")
        filled += 1

    # ---- 25: 初盘偏差 ----
    if data.opening_deviation:
        cl.mark("25", data.opening_deviation.get("direction", ""))
        filled += 1

    # ---- 24: CLV ----
    if data.odds_opening and data.odds_instant:
        fav_idx = min(range(3), key=lambda i: data.odds_instant[i])
        clv = (data.odds_instant[fav_idx] - data.odds_opening[fav_idx]) / data.odds_opening[fav_idx]
        cl.mark("24", f"CLV={clv:+.1%}")
        filled += 1

    # ---- 27: 返还率异常 ----
    if data.odds_instant:
        h, d, a = data.odds_instant
        imp_sum = 1/h + 1/d + 1/a
        payout = 1 / imp_sum
        if payout < 0.88:
            cl.mark("27", f"⚠️ 异常偏低 {payout:.1%}", status="⚠️")
        elif payout > 0.98:
            cl.mark("27", f"⚠️ 异常偏高 {payout:.1%}", status="⚠️")
        else:
            cl.mark("27", f"正常 {payout:.1%}")
        filled += 1

    # ---- 29: EV/Edge ----
    if data.odds_instant:
        h, d, a = data.odds_instant
        imp_sum = 1/h + 1/d + 1/a
        fav_idx = min(range(3), key=lambda i: data.odds_instant[i])
        fav_odds = data.odds_instant[fav_idx]
        edge = (1/fav_odds) / imp_sum * fav_odds - 1
        cl.mark("29", f"Edge={edge:+.2%}")
        filled += 1

    # ---- 09/10/11: 亚盘诱盘 (shared scrape, reused by 16/17/26) ----
    ah = AsianTrapSignal()
    euro_dev_signal = ""  # for cold detector
    try:
        fav_side = "away" if data.odds_instant and min(range(3), key=lambda i: data.odds_instant[i]) == 2 else "home"
        ah = check_ah_trap(data.fixture_id, fav_side)
        if ah.verdict:
            cl.mark("11", ah.verdict[:50])
            filled += 1
        if ah.line_up >= ah.total * 0.5:
            cl.mark("09", f"升盘 {ah.line_up}/{ah.total}家")
            cl.mark("10", "无降盘")
            filled += 2
        elif ah.line_down >= ah.total * 0.5:
            cl.mark("10", f"降盘 {ah.line_down}/{ah.total}家")
            cl.mark("09", "无升盘")
            filled += 2
        else:
            cl.mark("09", "盘口稳定-不适用")
            cl.mark("10", "盘口稳定-不适用")
            filled += 2
    except Exception:
        pass

    # ---- 14: 欧亚偏差 ----
    try:
        from .euro_ah import detect_deviation
        if data.odds_instant:
            h, d, a = data.odds_instant
            url_ah = f"https://odds.500.com/fenxi/yazhi-{data.fixture_id}.shtml"
            req_ah = urllib.request.Request(url_ah, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req_ah, timeout=10) as r_ah:
                html_ah = r_ah.read().decode("gb2312", errors="replace")
            # Extract first company's current line for deviation calculation
            m_ah = re.compile(r'<tr\s+class="tr[12]"[^>]*id="(\d+)"', re.IGNORECASE)
            fm = m_ah.search(html_ah)
            if fm:
                s = fm.start()
                depth = 0; pos = s
                while pos < len(html_ah):
                    no = html_ah.find("<tr", pos); nc = html_ah.find("</tr>", pos)
                    if no == s: pos = no + 3; depth = 1; continue
                    if nc < 0: break
                    if no >= 0 and no < nc: depth += 1; pos = no + 3
                    else:
                        depth -= 1
                        if depth == 0:
                            row_ah = html_ah[s:nc + 5]
                            break
                        pos = nc + 5
                tables_ah = re.findall(r'<table[^>]*class="pl_table_data"[^>]*>(.*?)</table>', row_ah, re.DOTALL)
                if len(tables_ah) >= 2:
                    ref_ah = re.search(r'ref="([^"]+)"', tables_ah[0])
                    if ref_ah:
                        dev = detect_deviation(h, d, a, float(ref_ah.group(1)))
                        if dev:
                            cl.mark("14", f"{dev.signal} {abs(dev.deviation):.2f}球 ({dev.severity})")
                            euro_dev_signal = dev.signal  # save for cold detector
                            filled += 1
    except Exception:
        pass

    # ---- 15: 赔率骨架 ----
    if data.odds_instant:
        fav_idx = min(range(3), key=lambda i: data.odds_instant[i])
        fav_odds = data.odds_instant[fav_idx]
        if fav_odds < 1.30:
            skeleton = "超深盘(<1.30)"
        elif fav_odds < 1.45:
            skeleton = "深盘(1.30-1.44)"
        elif fav_odds < 1.60:
            skeleton = "中深盘(1.45-1.59)"
        elif fav_odds < 1.80:
            skeleton = "中盘(1.60-1.79)"
        elif fav_odds < 2.00:
            skeleton = "中浅盘(1.80-1.99)"
        else:
            skeleton = "浅盘(≥2.00)"
        cl.mark("15", f"{skeleton} ({fav_odds:.2f})")
        filled += 1

    # ---- 16: 高级亚盘(四模) ----
    try:
        from .advanced_ah import analyze_advanced_ah
        if data.odds_instant and ah.total > 0:
            h, d, a = data.odds_instant
            adv = analyze_advanced_ah(
                home_odds=h, draw_odds=d, away_odds=a,
                open_line=ah.avg_open_line, close_line=ah.avg_close_line,
                open_water_fav=ah.avg_open_water_fav, close_water_fav=ah.avg_close_water_fav,
            )
            manipulation_cn = {
                "SHALLOW_BLOCK": "浅阻盘", "DEEP_BLOCK": "深阻盘",
                "SHALLOW_LURE": "浅诱盘", "DEEP_LURE": "深诱盘", "NEUTRAL": "均衡盘",
            }.get(adv.manipulation.name if hasattr(adv.manipulation, 'name') else str(adv.manipulation), str(adv.manipulation))
            cl.mark(
                "16",
                f"{manipulation_cn} | {adv.signal[:60]} | 信心{adv.confidence} | {adv.bet_suggestion}",
            )
            filled += 1
    except Exception:
        pass

    # ---- 26: 欧亚联动 ----
    if data.odds_opening and data.odds_instant and ah.total > 0:
        try:
            fav_idx = min(range(3), key=lambda i: data.odds_instant[i])
            euro_steam = data.odds_instant[fav_idx] - data.odds_opening[fav_idx]
            if euro_steam < -0.03 and ah.line_up >= ah.total * 0.5:
                cl.mark("26", "欧亚一致: 欧赔涌入+亚盘升盘")
            elif euro_steam < -0.03 and "诱" in ah.trap_type:
                cl.mark("26", "欧亚背离: 欧赔涌入但亚盘诱盘", status="⚠️")
            else:
                cl.mark("26", "已分析")
            filled += 1
        except Exception:
            pass

    # ---- 30: 必发四步验证 ----
    if data.bifax_result:
        bfr = data.bifax_result
        cl.mark("30", f"{bfr.get('verdict', '已分析')} (评分{bfr.get('score', 0):+d})")
    elif data.bifax_data:
        # Orchestrator didn't verify, try inline
        try:
            from footy.data.bifax import quick_verify as _bif
            result = _bif(data.bifax_data, data.match_name)
            cl.mark("30", f"{result.verdict} (评分{result.total_score:+d})")
        except Exception:
            cl.mark("30", "待采集(需WebFetch)", status="⚠️")
    else:
        cl.mark("30", "待采集(需WebFetch)", status="⚠️")

    # ---- 17: 冷门检测(9信号) ----
    try:
        if data.odds_instant:
            h, d, a = data.odds_instant
            # Determine host_is_dog
            host_is_dog = (h > a)  # home odds higher = home is underdog
            cold = detect_cold(
                home=data.home, away=data.away,
                home_odds=h, draw_odds=d, away_odds=a,
                ah_line=ah.avg_close_line if ah.total > 0 else 0.0,
                host_is_dog=host_is_dog,
                ha_euro_deviation_signal=euro_dev_signal,
                # Fundamentals default to False/0 (manual items 19-23)
            )
            if cold.cold_index >= 40:
                signal_names = " + ".join(s.name for s in cold.signals)
                cl.mark(
                    "17",
                    f"⚠️ {len(cold.signals)}信号: {signal_names}, "
                    f"指数{cold.cold_index}({cold.confidence}), {cold.bet_suggestion}",
                    status="⚠️",
                )
            elif cold.cold_index >= 25:
                signal_names = " + ".join(s.name for s in cold.signals)
                cl.mark(
                    "17",
                    f"⚡ {len(cold.signals)}信号: {signal_names}, "
                    f"指数{cold.cold_index}({cold.confidence}), {cold.bet_suggestion}",
                )
            else:
                cl.mark("17", f"无明显冷门信号 (指数{cold.cold_index})")
            filled += 1
    except Exception:
        pass

    # ---- 18: 庄家意图 ----
    try:
        intent = ""
        if data.odds_instant:
            fav_idx = min(range(3), key=lambda i: data.odds_instant[i])
            fav_odds = data.odds_instant[fav_idx]
            fav_name = ["主胜", "平局", "客胜"][fav_idx]
            if fav_odds < 1.20:
                intent = f"诱导追{fav_name}(极端低赔)"
            elif fav_odds < 1.50:
                intent = f"做热{fav_name}(低赔吸引)"
            else:
                intent = "分散资金, 无明确诱导"
        cl.mark("18", intent if intent else "待分析")
        filled += 1
    except Exception:
        pass

    # ---- 28: 泊松比分预测 (Dixon-Coles) ----
    try:
        if data.odds_instant:
            model = load_fitted_model()
            if model is not None and data.home in model.params.attack and data.away in model.params.attack:
                pred = model.predict(data.home, data.away)
                lam_h = pred["lambda_home"]
                lam_a = pred["lambda_away"]
                ou = pred["probs_ou25"]
                ml_h, ml_a = find_most_likely_score(pred["grid"])
                cl.mark(
                    "28",
                    f"预期进球 {lam_h:.1f}-{lam_a:.1f}, "
                    f"O/U2.5 {ou['over']:.0%}/{ou['under']:.0%}, "
                    f"最可能比分 {ml_h}-{ml_a}",
                )
            else:
                # Fallback: simple implied-probability estimate
                h, d, a = data.odds_instant
                imp_sum = 1/h + 1/d + 1/a
                exp_h = (1/h) / imp_sum * 2.5
                exp_a = (1/a) / imp_sum * 2.5
                cl.mark(
                    "28",
                    f"预期总进球{exp_h + exp_a:.1f}, 主{exp_h:.1f}-客{exp_a:.1f} "
                    f"(无模型参数, 粗略估算)",
                )
            filled += 1
    except Exception:
        pass

    # ---- 19-23: 基本面自动采集 (伤停/阵容/状态/出线/心理) ----
    try:
        from .auto_fundamentals import auto_fill_fundamentals
        fund_filled = auto_fill_fundamentals(data)
        filled += fund_filled
    except Exception:
        # Fallback: manual markers
        for item_id in ["19", "20", "21", "22", "23"]:
            cl.mark(item_id, "待手动采集", status="⚠️")
        filled += 5

    return filled


def format_signal_report(signals: MatchSignals) -> str:
    lines = [f"── {signals.match_name} ──"]
    p = signals.pinnacle
    if p.alert:
        lines.append(f"  {p.alert}")
    else:
        lines.append(f"  Pinnacle: Steam={p.pinnacle_steam:+.2f}, 与Bet365同向 ✅")
    lines.append(f"  O/U: {signals.ou_signal.verdict}")
    lines.append(f"  亚盘: {signals.ah_signal.verdict}")
    if signals.warnings:
        lines.append(f"  ⚠️ 警报: {' | '.join(signals.warnings)}")
    return "\n".join(lines)
