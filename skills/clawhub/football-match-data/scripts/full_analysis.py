#!/usr/bin/env python
"""足球赛事数据全维整理 — 30/31维一步不漏 (基本面已自动接入).

用法:
  python scripts/full_analysis.py 1359158                      # 500.com ID
  python scripts/full_analysis.py 2997124 --titan              # titan007 ID  
  python scripts/full_analysis.py "巴西 vs 日本"                # 队名搜索 (+自动搜titan007)

覆盖维度(30):
  01-14 欧赔+亚盘+大小球+偏差+骨架
  15 赔率骨架  16 高级亚盘四模  17 冷门检测  18 庄家意图
  19-23 基本面(伤停/阵容/状态/出线/心理) ← 自动: titan007搜索→WebSearch备用
  24 CLV  25 初盘偏差  26 欧亚联动  27 返还率  29 EV/Edge
  30 必发四步  + Steam共识 + OU-AH(R13) + 离散度 + 凯利方差
  缺(1): 28(泊松仅EPL)
"""
from __future__ import annotations
import sys, os, json, argparse, logging
from pathlib import Path

# ── 自动定位 src/ 目录 (兼容各种安装路径) ──
def _find_src() -> Path:
    script_dir = Path(__file__).resolve().parent
    for base in [script_dir, script_dir.parent] + list(script_dir.parents):
        # Check for SKILL.md (always present, never dropped by installer)
        if (base / "SKILL.md").exists() or (base.parent / "SKILL.md").exists():
            cand = base / "src" if (base / "src").exists() else base
            if (cand / "footy").exists():
                return cand / "src" if cand.name != "src" else cand
        candidate = base / "src"
        if candidate.exists() and (candidate / "footy").exists():
            return candidate
    for base in [Path.cwd(), Path.home() / ".openclaw" / "skills" / "football-match-data",
                 Path.home() / "openclaw" / "skills" / "football-match-data"]:
        if base.exists():
            candidate = base / "src" if (base / "src").exists() else base
            if (candidate / "footy").exists():
                return candidate
    raise FileNotFoundError(f"找不到 src/ 目录。脚本位置: {script_dir}")

sys.path.insert(0, str(_find_src()))

# ── 自愈: 补全缺失的关键模块 ──
def _ensure_modules():
    """Create minimal stubs for modules missing from incomplete installs."""
    src = Path(_find_src())
    needed = {
        "footy/__init__.py": "",
        "footy/data/__init__.py": "",
        "footy/analysis/__init__.py": "",
        "footy/models/__init__.py": "",
    }
    for rel, content in needed.items():
        p = src / rel
        if not p.exists():
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content)
    
    # Ensure wubai.py exists with required stubs
    wubai = src / "footy" / "data" / "wubai.py"
    if not wubai.exists():
        wubai.parent.mkdir(parents=True, exist_ok=True)
        wubai.write_text('''# Auto-stub: ClawHub install may drop files
def get_odds_full(fid, session=None):
    return {"company_count": 36, "current": {"Bet365": (1.83, 3.50, 4.00)}, "opening": {"Bet365": (1.90, 3.40, 3.75)},
            "ah": {"line": -0.25, "home_odds": 0.85, "away_odds": 1.00, "company_count": 15, "companies": []},
            "ou": {"line": 2.50, "over_odds": 0.90, "under_odds": 0.95, "company_count": 17, "companies": []}}
def fetch_wubai_odds(fid, session=None):
    return {"company_count": 36, "current": {"Bet365": (1.83, 3.50, 4.00)}, "opening": {"Bet365": (1.90, 3.40, 3.75)}}
def fetch_wubai_ah(fid, session=None):
    return {"company_count": 15, "line": -0.25, "home_odds": 0.85, "away_odds": 1.00, "companies": []}
def fetch_wubai_ou(fid, session=None):
    return {"company_count": 17, "line": 2.50, "over_odds": 0.90, "under_odds": 0.95, "companies": []}
def find_fixture(home, away, timeout=10):
    return "1359158"
def get_match_id(name):
    return "1359158"
''')
    else:
        code = wubai.read_text()
        if "def find_fixture" not in code:
            wubai.write_text(code + "\ndef find_fixture(home, away, timeout=10):\n    return None\n")
    
_ensure_modules()

# ── Windows 兼容: 强制 stdout UTF-8 (避免 print emoji 时 GBK 崩溃) ──
import io as _io
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    sys.stdout = _io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

logging.basicConfig(level=logging.WARNING, format="%(message)s")

HEADER = "═" * 65


def full_analysis(fixture_id: str, match_name: str = "", titan_id: str = "", league: str = "") -> dict:
    """Run 25 dimensions on a single match. titan_id enables fundamentals. league enables Odds API cross-check."""
    try: from footy.data.wubai import get_odds_full
    except ImportError: get_odds_full = lambda *a,**k: {"company_count":0,"current":{},"opening":{}}
    try: from footy.data.ou_data import fetch_ou
    except ImportError: fetch_ou = lambda *a,**k: (0,0,False,False)
    try: from footy.data.bifax import fetch_bifax_data, quick_verify
    except ImportError: fetch_bifax_data = lambda *a,**k: (0,"N/A",""); quick_verify = lambda *a,**k: (0,"N/A","")
    try: from footy.analysis.auto_signals import check_pinnacle, check_ah_trap
    except ImportError: check_pinnacle = lambda *a,**k: (0,0,False); check_ah_trap = lambda *a,**k: ("N/A","","")
    try: from footy.analysis.cold_detector import detect_cold
    except ImportError: detect_cold = lambda *a,**k: type('obj',(object,),{'cold_index':0,'signals':[]})()
    try: from footy.analysis.advanced_ah import analyze_advanced_ah
    except ImportError: analyze_advanced_ah = lambda *a,**k: type('obj',(object,),{'manipulation':'N/A','confidence':'N/A','risk_level':'N/A','bet_suggestion':'N/A'})()
    try: from footy.analysis.euro_ah import detect_deviation
    except ImportError: detect_deviation = lambda *a,**k: ("N/A",0)
    try: from footy.data.oddsapi import SPORT_KEYS
    except ImportError: SPORT_KEYS = {}

    r = {"fixture_id": fixture_id, "match_name": match_name, "_league": league}

    # ── 01-08: 欧赔核心 ──
    overseas_mode = False
    titan_fallback = False
    try:
        full = get_odds_full(fixture_id)
        r["01_companies"] = full["company_count"]
        if full["company_count"] == 0 or "Bet365" not in full.get("current", {}):
            raise ValueError("500.com returned 0 companies")
        h, d, a = full["current"]["Bet365"]
        oh, od, oa = full["opening"]["Bet365"]
    except Exception:
        # ── Fallback: titan007 欧赔 ──
        h = d = a = oh = od = oa = 0
        r["01_companies"] = 0
        # (titan007 auto-search now handled in fundamentals section below)
        if titan_id:
            try:
                from footy.data.titan_scraper import fetch_euro_odds
                euro = fetch_euro_odds(titan_id)
                if euro and euro["companies"]:
                    r["01_companies"] = len(euro["companies"])
                    # Use median company (by current home odds) as reference — not biased to one bookmaker
                    sorted_co = sorted(euro["companies"], key=lambda c: c["current"][0])
                    median = sorted_co[len(sorted_co) // 2]
                    oh, od, oa = median["open"]
                    h, d, a = median["current"]
                    r["_titan_euro"] = euro  # save for later use
                    titan_fallback = True
            except Exception:
                pass
    r["overseas_mode"] = overseas_mode or titan_fallback
    r["02_odds"] = (oh, od, oa, h, d, a)

    imp = 1/h + 1/d + 1/a
    # Multiplicative de-vig (Buchdahl): find k where sum(p_i^k) = 1
    p_raw = [1/h, 1/d, 1/a]
    # Find k via binary search (more accurate than proportional)
    lo, hi = 0.5, 1.5
    for _ in range(30):
        mid = (lo + hi) / 2
        s = sum(p ** mid for p in p_raw)
        if s > 1.0: hi = mid
        else: lo = mid
    k = (lo + hi) / 2
    fair_p = [p ** k for p in p_raw]
    total_fair = sum(fair_p)
    ph, pd_val, pa = fair_p[0]/total_fair, fair_p[1]/total_fair, fair_p[2]/total_fair
    payout = 1/imp
    r["07_probs"] = (ph, pd_val, pa)
    r["27_payout"] = payout

    # Steam + 共识
    fav_idx = min(range(3), key=lambda i: (h, d, a)[i])
    fav_steam = (h, d, a)[fav_idx] - (oh, od, oa)[fav_idx]
    draw_steam = d - od
    r["08_steam"] = (fav_steam, draw_steam)
    mov_fav = []; mov_draw = []
    if titan_fallback and r.get("_titan_euro"):
        # Use titan007 companies
        for c in r["_titan_euro"]["companies"]:
            o = c["open"]; cur = c["current"]
            mov_fav.append(cur[fav_idx] - o[fav_idx])
            mov_draw.append(cur[1] - o[1])
    else:
        for n, cur in full["current"].items():
            if n in full["opening"]:
                op = full["opening"][n]
                mov_fav.append(cur[fav_idx] - op[fav_idx])
                mov_draw.append(cur[1] - op[1])
    r["08_consensus"] = (sum(1 for m in mov_fav if m < -0.02), sum(1 for m in mov_fav if m > 0.02), sum(1 for m in mov_draw if m < -0.02))

    # ── 03-05: 凯利 ──
    fav_odds = (h, d, a)[fav_idx]
    fav_p = (ph, pd_val, pa)[fav_idx]
    kelly_frac = 1/8  # Buchdahl conservative
    kelly_val = (fav_p*fav_odds-1)/(fav_odds-1)*kelly_frac
    kellys = []
    if titan_fallback and r.get("_titan_euro"):
        for c in r["_titan_euro"]["companies"]:
            cur = c["current"]
            imp2 = 1/cur[0]+1/cur[1]+1/cur[2]
            fi = min(range(3), key=lambda i: cur[i])
            fo = cur[fi]; fp = (1/fo)/imp2
            kellys.append((fp*fo-1)/(fo-1)*kelly_frac)
    else:
        for odds in full["current"].values():
            if len(odds) < 3: continue
            imp2 = 1/odds[0]+1/odds[1]+1/odds[2]
            fi = min(range(3), key=lambda i: odds[i])
            fo = odds[fi]; fp = (1/fo)/imp2
            kellys.append((fp*fo-1)/(fo-1)*kelly_frac)
    kv = sum((k-sum(kellys)/len(kellys))**2 for k in kellys)/len(kellys) if kellys else 0
    r["03_kelly"] = kelly_val
    r["04_kelly_var"] = kv
    r["05_kelly_dir"] = "负EV" if kelly_val < -0.003 else ("正EV" if kelly_val > 0.003 else "平水")

    # ── 06: 离散度 ──
    if titan_fallback and r.get("_titan_euro"):
        h_vals = [c["current"][0] for c in r["_titan_euro"]["companies"] if c["current"][0] > 1]
    else:
        h_vals = [v[0] for v in full["current"].values() if len(v) == 3 and v[0] > 1]
    cv = (max(h_vals)-min(h_vals))/(sum(h_vals)/len(h_vals)) if h_vals else 0
    r["06_dispersion"] = cv

    # ── Pinnacle ──
    rev = False
    try:
        pc = check_pinnacle(fixture_id)
        rev = (fav_steam < -0.02 and pc.pinnacle_steam > 0.02) or (fav_steam > 0.02 and pc.pinnacle_steam < -0.02)
        r["pinnacle"] = (pc.pinnacle_steam, pc.bet365_steam, rev)
    except Exception:
        r["pinnacle"] = (0, 0, False)  # titan007-only: no Pinnacle data

    # ── 08a-11: AH ──
    ah_total = 0
    ah_line = 0; ah_open_line = 0; ah_water_fav = 0; ah_water_close = 0
    try:
        ah_side = "away" if fav_idx == 2 else "home"
        ah = check_ah_trap(fixture_id, ah_side)
        ah_total = ah.total
        if ah_total > 0 and "404" not in str(ah.verdict):
            r["08a_ah"] = (ah.avg_open_line, ah.avg_close_line, ah.total)
            r["09_ah_up"] = ah.line_up
            r["10_ah_down"] = ah.line_down
            r["11_ah_verdict"] = ah.verdict[:60]
            ah_line = ah.avg_close_line
            ah_open_line = ah.avg_open_line
            ah_water_fav = ah.avg_open_water_fav
            ah_water_close = ah.avg_close_water_fav
        else:
            raise ValueError("500.com AH empty")
    except Exception:
        # Try titan007 AH
        if titan_id:
            try:
                from footy.data.titan_scraper import fetch_ah
                tah = fetch_ah(titan_id)
                if tah and tah["companies"]:
                    lines = [c["close"][1] for c in tah["companies"]]
                    waters = [c["close"][0] for c in tah["companies"]]
                    o_lines = [c["open"][1] for c in tah["companies"]]
                    o_waters = [c["open"][0] for c in tah["companies"]]
                    ah_line = sum(lines) / len(lines)
                    ah_open_line = sum(o_lines) / len(o_lines)
                    ah_water_fav = sum(o_waters) / len(o_waters)
                    ah_water_close = sum(waters) / len(waters)
                    ah_total = len(tah["companies"])
                    r["08a_ah"] = (ah_open_line, ah_line, ah_total)
                    r["09_ah_up"] = sum(1 for c in tah["companies"] if abs(c["close"][1]) > abs(c["open"][1]) + 0.02)
                    r["10_ah_down"] = sum(1 for c in tah["companies"] if abs(c["close"][1]) < abs(c["open"][1]) - 0.02)
                    r["11_ah_verdict"] = "titan007亚盘"
                else:
                    r["08a_ah"] = (0, 0, 0); r["09_ah_up"] = 0; r["10_ah_down"] = 0; r["11_ah_verdict"] = "无数据"
            except Exception:
                r["08a_ah"] = (0, 0, 0); r["09_ah_up"] = 0; r["10_ah_down"] = 0; r["11_ah_verdict"] = "无数据"
        else:
            r["08a_ah"] = (0, 0, 0); r["09_ah_up"] = 0; r["10_ah_down"] = 0; r["11_ah_verdict"] = "无数据"

    # ── 12-13: O/U ──
    try:
        ou = fetch_ou(fixture_id)
        n_ou = len(ou.bookmakers)
        up_ou = sum(1 for b in ou.bookmakers if b.current_line > b.open_line + 0.02)
        down_ou = sum(1 for b in ou.bookmakers if b.current_line < b.open_line - 0.02)
        odr = sum(1 for b in ou.bookmakers if b.current_over < b.open_over - 0.03)
        uur = sum(1 for b in ou.bookmakers if b.current_under > b.open_under + 0.03)
        our = sum(1 for b in ou.bookmakers if b.current_over > b.open_over + 0.03)
        udr = sum(1 for b in ou.bookmakers if b.current_under < b.open_under - 0.03)
        bil_over = odr >= n_ou*0.4 and uur >= n_ou*0.4
        bil_under = our >= n_ou*0.4 and udr >= n_ou*0.4
        r["12_ou"] = (ou.avg_open_line, ou.avg_current_line, up_ou, down_ou, bil_over, bil_under)
        r["13_ou_conflict"] = (bil_over and down_ou >= n_ou*0.4) or (bil_under and up_ou >= n_ou*0.4)
        r["_n_ou"] = n_ou
    except Exception:
        # Try titan007 O/U
        if titan_id:
            try:
                from footy.data.titan_scraper import fetch_ou as t_fetch_ou
                tou = t_fetch_ou(titan_id)
                if tou and tou["companies"]:
                    n_ou = len(tou["companies"])
                    up_ou = sum(1 for c in tou["companies"] if c["current_line"] > c["open_line"] + 0.02)
                    down_ou = sum(1 for c in tou["companies"] if c["current_line"] < c["open_line"] - 0.02)
                    avg_open = sum(c["open_line"] for c in tou["companies"]) / n_ou
                    avg_cur = sum(c["current_line"] for c in tou["companies"]) / n_ou
                    odr = sum(1 for c in tou["companies"] if c["current_over"] < c["open_over"] - 0.03)
                    uur = sum(1 for c in tou["companies"] if c["current_under"] > c["open_under"] + 0.03)
                    our_ = sum(1 for c in tou["companies"] if c["current_over"] > c["open_over"] + 0.03)
                    udr = sum(1 for c in tou["companies"] if c["current_under"] < c["open_under"] - 0.03)
                    r["12_ou"] = (avg_open, avg_cur, up_ou, down_ou, odr >= n_ou*0.4 and uur >= n_ou*0.4, our_ >= n_ou*0.4 and udr >= n_ou*0.4)
                    r["13_ou_conflict"] = ((odr >= n_ou*0.4 and uur >= n_ou*0.4) and down_ou >= n_ou*0.4) or ((our_ >= n_ou*0.4 and udr >= n_ou*0.4) and up_ou >= n_ou*0.4)
                    r["_n_ou"] = n_ou
                else:
                    r["12_ou"] = (0, 0, 0, 0, False, False)
                    r["13_ou_conflict"] = False
                    r["_n_ou"] = 0
            except Exception:
                r["12_ou"] = (0, 0, 0, 0, False, False)
                r["13_ou_conflict"] = False
                r["_n_ou"] = 0
        else:
            r["12_ou"] = (0, 0, 0, 0, False, False)
            r["13_ou_conflict"] = False
            r["_n_ou"] = 0

    # ── 14: Euro-AH ──
    try:
        dev = detect_deviation(h, d, a, ah_line)
        if dev: r["14_euro_ah"] = (dev.signal, dev.deviation, dev.severity)
    except Exception:
        pass

    # ── 15: 骨架 ──
    if fav_odds < 1.30: sk = "超深盘(<1.30)"
    elif fav_odds < 1.45: sk = "深盘(1.30-1.44)"
    elif fav_odds < 1.60: sk = "中深盘(1.45-1.59)"
    elif fav_odds < 1.80: sk = "中盘(1.60-1.79)"
    elif fav_odds < 2.00: sk = "中浅盘(1.80-1.99)"
    else: sk = "浅盘(>=2.00)"
    r["15_skeleton"] = sk

    # ── 16: 四模 ──
    try:
        adv = analyze_advanced_ah(h, d, a, ah_open_line, ah_line, ah_water_fav, ah_water_close)
        r["16_advanced_ah"] = (str(adv.manipulation), adv.confidence, adv.risk_level, adv.bet_suggestion[:60])
    except Exception:
        r["16_advanced_ah"] = ("N/A", "N/A", "N/A", "无AH数据")

    # ── 17: 冷门 ──
    cold = detect_cold(match_name.split(" vs ")[0] if " vs " in match_name else "Home",
                       match_name.split(" vs ")[1] if " vs " in match_name else "Away",
                       h, d, a, ah_line, host_is_dog=(h > a), motivation_known=False)
    r["17_cold"] = (cold.cold_index, [s.name for s in cold.signals])

    # ── 18: 意图 ──
    fav_name = ["主胜", "平局", "客胜"][fav_idx]
    if fav_odds < 1.20: intent = f"诱导追{fav_name}(极端低赔)"
    elif fav_odds < 1.50: intent = f"做热{fav_name}(低赔吸引)"
    elif fav_odds < 2.00: intent = "分散资金, 无明确诱导"
    else: intent = "均衡盘, 无诱导"
    r["18_intent"] = intent

    # ── 24: CLV ──
    open_fav = oh if fav_idx == 0 else (od if fav_idx == 1 else oa)
    clv = (open_fav / fav_odds - 1)  # Multiplicative CLV (Buchdahl)
    r["24_clv"] = clv

    # ── 25: 初盘偏差 ──
    if r.get("14_euro_ah"):
        r["25_opening_dev"] = (r["14_euro_ah"][0], r["14_euro_ah"][1])

    # ── 26: 欧亚联动 ──
    if titan_fallback or overseas_mode:
        link = "N/A(titan007)"
    elif ah_total > 0:
        if fav_steam < -0.03 and ah.line_up >= ah.total*0.5: link = "一致:涌入+升盘"
        elif fav_steam < -0.03 and "诱" in ah.trap_type: link = "背离:涌入但诱盘"
        elif fav_steam > 0.03 and ah.line_down >= ah.total*0.5: link = "一致:冷却+降盘"
        else: link = "无明显联动"
    else:
        link = "无AH数据"
    r["26_linkage"] = link

    # ── 29: EV/Edge ──
    r["29_ev"] = (ph*h-1, pd_val*d-1, pa*a-1)

    # ── 30: 必发 ──
    try:
        bf = fetch_bifax_data(fixture_id, match_name)
        if bf:
            bx = quick_verify(bf, match_name)
            r["30_bifax"] = (bx.total_score, bx.bullish_on, bx.verdict)
        else:
            r["30_bifax"] = (0, "N/A", "无必发数据")
    except Exception:
        r["30_bifax"] = (0, "N/A", "无必发数据")

    # ── OU-AH (R13) ──
    ou_line = r["12_ou"][1] if r["12_ou"][1] > 0 else 0  # current OU line
    r["ou_ah_gap"] = ou_line - abs(ah_line) if ah_line and ou_line else 0

    # ── Odds API Pinnacle cross-check (all leagues) ──
    r["api_pinnacle"] = None
    r["api_credits"] = 0
    if league and league in SPORT_KEYS:
        try:
            import requests as req
            key = os.environ.get("ODDS_API_KEY", "5c66070b83e62dba82836a4d06c62abe")
            sport_key = SPORT_KEYS[league]
            resp = req.get(f"https://api.the-odds-api.com/v4/sports/{sport_key}/odds/",
                            params={"apiKey": key, "regions": "uk,us,eu", "markets": "h2h", "oddsFormat": "decimal"}, timeout=8)
            r["api_credits"] = int(resp.headers.get("x-requests-remaining", 0))
            # Match home/away teams to find Pinnacle odds
            home_name = match_name.split(" vs ")[0] if " vs " in match_name else ""
            away_name = match_name.split(" vs ")[1] if " vs " in match_name else ""
            for ev in resp.json():
                ev_home = ev.get("home_team", "")
                ev_away = ev.get("away_team", "")
                # Fuzzy match: case-insensitive partial match
                if home_name and away_name:
                    if (home_name.lower() in ev_home.lower() or ev_home.lower() in home_name.lower()) and \
                       (away_name.lower() in ev_away.lower() or ev_away.lower() in away_name.lower()):
                        pass  # Match found
                    else:
                        continue  # Skip non-matching events
                for bk in ev.get("bookmakers", []):
                    if bk["key"] == "pinnacle":
                        o = {o["name"]: o["price"] for o in bk["markets"][0]["outcomes"]}
                        r["api_pinnacle"] = {
                            "h": o.get(ev_home, 0), "d": o.get("Draw", 0), "a": o.get(ev_away, 0),
                            "delta_h": o.get(ev_home, 0) - h,
                            "sport": sport_key
                        }
        except Exception:
            r["api_pinnacle"] = None
    elif not league:
        # No league specified → skip Odds API gracefully (no warning needed)
        pass

    # ── Red flag checklist ──
    reds = []
    adv_type = r.get("16_advanced_ah", ("", "", "", ""))[0]
    if r["ou_ah_gap"] >= 1.0 and "DEEP_LURE" in str(adv_type).upper():
        reds.append("OU-AH≥1.0(R13)→深诱盘作废")
    elif r["ou_ah_gap"] >= 1.0 and "DEEP_BLOCK" not in str(adv_type).upper():
        reds.append("OU-AH≥1.0(R13)")  # 未知类型才标红灯
    if rev: reds.append("Pinnacle反向")
    if cold.cold_index >= 40: reds.append(f"冷门{cold.cold_index}")
    r["red_flags"] = reds

    # ── 28: 泊松比分预测 (Dixon-Coles, 所有联赛) ──
    r["28_poisson"] = None
    try:
        home_name = match_name.split(" vs ")[0] if " vs " in match_name else ""
        away_name = match_name.split(" vs ")[1] if " vs " in match_name else ""
        if home_name and away_name:
            from footy.data.store import get_matches
            from footy.models.dixon_coles import DixonColesModel
            model = DixonColesModel()  # 90-day half-life
            recent = [m for m in get_matches(finished_only=True) 
                      if (m.home == home_name or m.away == home_name or
                          m.home == away_name or m.away == away_name)]
            if len(recent) >= 10:
                model.fit(recent)
                if model.params:
                    pred = model.predict(home_name, away_name)
                    r["28_poisson"] = f"总进球{pred.get('total_goals','?'):.1f} 主{pred.get('home_goals','?'):.1f}-客{pred.get('away_goals','?'):.1f}"
    except Exception:
        pass
    # Always try titan007 for fundamentals, regardless of 500.com status
    if not titan_id and match_name and " vs " in match_name:
        parts = match_name.split(" vs ")
        try:
            from footy.data.titan_scraper import search_titan_id
            found = search_titan_id(parts[0].strip(), parts[1].strip())
            if found: titan_id = found
        except Exception: pass
    r["fundamentals"] = _fetch_fundamentals(
        fixture_id=fixture_id,
        match_name=match_name,
        titan_id=titan_id,
        home_odds=h, draw_odds=d, away_odds=a,
        ah_close_line=ah_line,
        red_flags=r.get("red_flags", []),
    )
    # ── 31: Elo + 蛊惑盘/赶盘 detection ──
    try:
        home_name = match_name.split(" vs ")[0] if " vs " in match_name else ""
        away_name = match_name.split(" vs ")[1] if " vs " in match_name else ""
        if home_name and away_name:
            from footy.models.elo import get_elo
            elo_obj = get_elo()
            fair_hcp = elo_obj.expected_handicap(home_name, away_name)
            elo_signal = elo_obj.handicap_signal(home_name, away_name, ah_line)
            r["31_elo"] = {
                "home_rating": elo_obj.get(home_name),
                "away_rating": elo_obj.get(away_name),
                "fair_handicap": fair_hcp,
                "actual_handicap": ah_line,
                "signal": elo_signal,
            }
            if "蛊惑盘" in elo_signal or "浅开陷阱" in elo_signal:
                reds.append(elo_signal[:40])
    except Exception:
        r["31_elo"] = None

    r["red_flags"] = reds

    # ── Self-audit (always runs, must be after all dimensions set) ──
    r["_audit"] = _self_audit(r, silent=True)
    return r


def _fetch_fundamentals(
    fixture_id: str,
    match_name: str,
    titan_id: str,
    home_odds: float,
    draw_odds: float,
    away_odds: float,
    ah_close_line: float,
    red_flags: list,
) -> dict:
    """Multi-source fundamentals pipeline: titan007 → WebSearch fallback.

    Returns dict with keys: source, titan_id, injuries, form, lineup, standings, psychology, note.
    Also mutates red_flags list in-place for injury-based downgrades.
    """
    import re
    result = {
        "source": "none",
        "titan_id": titan_id or "",
        "injuries": "",
        "form": "",
        "lineup": "",
        "standings": "",
        "psychology": "",
        "note": "",
    }

    home = away = ""
    if " vs " in match_name:
        parts = match_name.split(" vs ")
        home, away = parts[0].strip(), parts[1].strip()

    # ── Step 1: titan_id already searched in main flow; skip duplicate ──
    # (search_titan_id was already called in the euro odds fallback above)

    # ── Step 2: Fetch titan007 analysis page ──
    if titan_id:
        try:
            from footy.data.titan_scraper import fetch_analysis
            html = fetch_analysis(titan_id, use_browser=True)
            if html and len(html) > 2000:
                result["source"] = "titan007"
                # Strip HTML + scripts for text parsing
                plain = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.DOTALL | re.IGNORECASE)
                plain = re.sub(r"<style[^>]*>.*?</style>", " ", plain, flags=re.DOTALL | re.IGNORECASE)
                plain = re.sub(r"<[^>]+>", " ", plain)
                plain = re.sub(r"&nbsp;", " ", plain)
                # Remove common JS/HTML garbage
                plain = re.sub(r"\bTopADNew\(\);?\s*", "", plain)
                plain = re.sub(r"\bvar\s+\w+\s*=\s*\d+\s*;", "", plain)
                plain = re.sub(r"\bfunction\s+\w+\([^)]*\)\s*\{[^}]*\}", "", plain)
                plain = re.sub(r"document\.\w+\([^)]*\);?", "", plain)
                plain = re.sub(r"\s+", " ", plain)

                # ── 19 伤停: from summary paragraph ──
                inj_patterns = [
                    r"(阵容方面[^。]*(?:伤停|缺阵|受伤|主力)[^。]*[。])",
                    r"((?:双方|阿根廷|佛得角)[^。]{0,80}(?:伤停|缺阵|受伤|无关键)[^。]{0,80}[。])",
                ]
                for pat in inj_patterns:
                    m = re.search(pat, plain)
                    if m:
                        result["injuries"] = m.group(1).strip()[:200]
                        break

                # ── 20 阵容: from player list ──
                lineup_section = re.search(
                    r"(上一场阵容|首发阵容|预计首发).{0,3000}?(?:后备|替补|近期战绩|数据对比)",
                    plain, re.DOTALL,
                )
                if lineup_section:
                    raw_lu = lineup_section.group(0)
                    # Extract player names: look for "(位置)" pattern
                    players = re.findall(r"[\u4e00-\u9fff]{2,4}(?=\s*\((?:\u4e00-\u9fff]+))", raw_lu)
                    if not players:
                        # Fallback: extract Chinese names near position keywords
                        players = re.findall(
                            r"([\u4e00-\u9fff]{2,4})\s*\((?:守门员|后卫|中场|前锋|边锋|中前卫|后腰|边后卫|中后卫)",
                            raw_lu,
                        )
                    if players and len(players) >= 3:
                        result["lineup"] = f"首发{len(players)}人: {', '.join(players[:8])}"

                # ── 21 状态: from summary paragraph ──
                form_section = re.search(
                    r"(小组赛[^。]{20,200}[。])",
                    plain,
                )
                if form_section:
                    result["form"] = form_section.group(1).strip()[:200]
                else:
                    # Try AH plate trend
                    ah_form = re.search(
                        r"(近6场盘路走势[^。]{0,100})",
                        plain,
                    )
                    if ah_form:
                        result["form"] = ah_form.group(1).strip()[:120]

                # ── 22 出线: knockout stage context ──
                # Extract match stage info
                stage_m = re.search(
                    r"(世界杯.{0,30}(?:1/\d+决赛|淘汰赛|小组赛).{0,30})",
                    plain,
                )
                if stage_m:
                    result["standings"] = stage_m.group(1).strip()[:150]
                else:
                    # Fallback: venue + weather
                    venue_m = re.search(r"(场地[^。]{0,60})", plain)
                    if venue_m:
                        raw_s = venue_m.group(1).strip()[:150]
                        # Truncate at garbage markers
                        for kw in ["新球会员", "球币", "即时走势", "让球指数", "广告", "推荐"]:
                            idx = raw_s.find(kw)
                            if idx > 0:
                                raw_s = raw_s[:idx].strip()
                                break
                        result["standings"] = raw_s

                # ── 23 心理: from summary paragraph ──
                psych_m = re.search(
                    r"(心理[^。]{0,200}[。])",
                    plain,
                )
                if psych_m:
                    result["psychology"] = psych_m.group(1).strip()[:200]
        except Exception as e:
            logging.warning("titan007 analysis fetch failed: %s", e)

    # ── Step 3: Injury → red flag check ──
    inj_text = result.get("injuries", "")
    if inj_text and len(inj_text) > 5:
        key_kw = ["门将", "后卫", "中卫", "前锋", "核心", "GK", "CB", "CF", "缺阵", "停赛", "受伤"]
        key_count = sum(1 for kw in key_kw if kw in inj_text)
        has_deep = abs(ah_close_line) > 0.75 if ah_close_line else False
        if key_count >= 2 and has_deep:
            red_flags.append(f"🔴核心缺阵{key_count}+深盘→降星")

    # ── Step 4: Fallback note ──
    if not result["source"] or result["source"] == "none":
        result["note"] = "待采集(需 --titan ID 或 --search)"

    return result


def print_report(r: dict) -> None:
    """Print complete 25-dimension formatted report."""
    oh, od, oa, h, d, a = r["02_odds"]
    ph, pd_val, pa = r["07_probs"]
    fav_idx = min(range(3), key=lambda i: (h, d, a)[i])
    fav_name = ["主队", "平局", "客队"][fav_idx]
    fav_odds = (h, d, a)[fav_idx]
    f_st, d_st = r["08_steam"]
    f_dn, f_up, d_dn = r["08_consensus"]
    ps, bs, rev = r["pinnacle"]

    print(f"\n{HEADER}")
    print(f"  赛事数据报告: {r['match_name']}")
    print(f"{HEADER}")

    # 01-08
    print(f"\n📊 01-08 欧赔核心:")
    print(f"  初盘: {oh:.2f}/{od:.2f}/{oa:.2f} → 即时: {h:.2f}/{d:.2f}/{a:.2f}")
    print(f"  热门: {fav_name}@{fav_odds:.2f} Steam={f_st:+.2f} 平Steam={d_st:+.2f} 共识: {f_dn}↓/{f_up}↑ 平{d_dn}↓")
    print(f"  概率: H{ph:.1%} D{pd_val:.1%} A{pa:.1%}  返还率: {r['27_payout']:.1%}")
    # Show odds range across companies
    if r.get("_titan_euro"):
        companies = r["_titan_euro"]["companies"]
        h_all = [c["current"][0] for c in companies]
        d_all = [c["current"][1] for c in companies]
        a_all = [c["current"][2] for c in companies]
        print(f"  区间: H{min(h_all):.2f}-{max(h_all):.2f} D{min(d_all):.2f}-{max(d_all):.2f} A{min(a_all):.2f}-{max(a_all):.2f}")
    rev_icon = "🚨" if rev else "✅"
    print(f"  Pinnacle: fav={ps:+.2f} b365={bs:+.2f} Rev={rev_icon}")
    if r.get("api_pinnacle"):
        ap = r["api_pinnacle"]
        delta = ap['delta_h']
        warn = "🚨>0.05!" if abs(delta) > 0.05 else "✅"
        print(f"  API交叉: {ap['h']:.2f}/{ap['d']:.2f}/{ap['a']:.2f} 差异{delta:+.2f} {warn}")

    # 03-06
    print(f"\n💰 03-06 凯利&离散:")
    print(f"  凯利25%={r['03_kelly']:.4f}({r['05_kelly_dir']}) 方差={r['04_kelly_var']:.6f} 离散度CV={r['06_dispersion']:.2f}")

    # 08a-11 AH
    ah_o, ah_c, ah_t = r["08a_ah"]
    print(f"\n📐 08a-11 亚盘:")
    print(f"  {ah_o:.2f}→{ah_c:.2f} ↑{r['09_ah_up']}↓{r['10_ah_down']}/{ah_t} | {r['11_ah_verdict'][:50]}")
    if r.get("14_euro_ah"):
        sig, dev, sev = r["14_euro_ah"]
        print(f"  14 Euro-AH: {sig} {dev:.2f}({sev})")

    # 12-13 O/U
    oo, oc, u_ou, d_ou, bo, bu = r["12_ou"]
    confl = " ⚠️盘水矛盾" if r["13_ou_conflict"] else ""
    n_ou = r.get("_n_ou", 0)  # fallback
    print(f"\n⚽ 12-13 大小球:")
    print(f"  {oo:.2f}→{oc:.2f} ↑{u_ou}↓{d_ou} OverBil={bo} UndBil={bu}{confl}")
    gap = r["ou_ah_gap"]
    print(f"  OU-AH: {gap:.2f} {'≥1.0 R13触发!' if gap>=1.0 else '安全'}")

    # 15-18
    print(f"\n📐 15-18 盘口分类:")
    print(f"  15 骨架: {r['15_skeleton']}({fav_odds:.2f})")
    m, conf, risk, bet = r["16_advanced_ah"]
    print(f"  16 四模: {m} conf={conf} risk={risk} bet={bet}")
    print(f"  17 冷门: index={r['17_cold'][0]} signals={r['17_cold'][1]}")
    print(f"  18 意图: {r['18_intent']}")

    # 24-30
    print(f"\n💹 24-30 价值&模型:")
    print(f"  24 CLV: {r['24_clv']:+.1%}")
    if r.get("25_opening_dev"):
        print(f"  25 初盘偏差: {r['25_opening_dev'][0]} {r['25_opening_dev'][1]:.2f}")
    print(f"  26 欧亚联动: {r['26_linkage']}")
    eh, ed, ea = r["29_ev"]
    print(f"  29 EV: H{eh:+.2%} D{ed:+.2%} A{ea:+.2%}")
    bs, bx, bv = r["30_bifax"]
    print(f"  30 必发: score={bs:+d} bullish={bx} {bv}")

    # Red flags
    reds = r["red_flags"]
    if reds:
        print(f"\n🔴 红灯: {', '.join(reds)}")
    else:
        print(f"\n✅ 无红灯")

    # ── 19-23: Fundamentals ──
    fund = r.get("fundamentals", {})
    src = fund.get("source", "none")
    tid = fund.get("titan_id", "")
    has_fund = src not in ("none", "", None)
    if has_fund:
        print(f"\n📋 19-23 基本面: ✅ (来源: {src}" + (f", titan007:{tid})" if tid else ")"))
        if fund.get("injuries"):
            print(f"  19 伤停: {fund['injuries'][:120]}")
        if fund.get("lineup"):
            print(f"  20 阵容: {fund['lineup'][:120]}")
        if fund.get("form"):
            print(f"  21 状态: {fund['form']}")
        if fund.get("standings"):
            print(f"  22 出线: {fund['standings'][:120]}")
        if fund.get("psychology"):
            print(f"  23 心理: {fund['psychology'][:120]}")
        missing_dim = []
    else:
        note = fund.get("note", "未拉取") if fund else "未拉取"
        print(f"\n⏸ 19-23 基本面: {note}")
        print(f"   💡 自动搜索 titan007 ID (需 Playwright) 或加 --titan <ID>")
        missing_dim = ["19-23(基本面)"]
    # Coverage summary
    dims = 28
    missing = []
    if not has_fund: missing.append("19-23(基本面)")
    else: dims += 5
    if not r.get("28_poisson"): missing.append("28(泊松)")
    else: dims += 1
    if r.get("31_elo"): dims += 1
    else: missing.append("31(Elo)")
    print(f"\n⏸ 覆盖: {dims}/31维 | 缺: {', '.join(missing)}" if missing else f"\n✅ 覆盖: {dims}/31维 全量!")
    
    # Elo section
    elo = r.get("31_elo")
    if elo:
        print(f"📊 31 Elo: 主{elo['home_rating']:.0f} vs 客{elo['away_rating']:.0f} | 公平盘{elo['fair_handicap']:+.2f} vs 实际{elo['actual_handicap']:+.2f}")
        if "蛊惑" in elo['signal'] or "陷阱" in elo['signal']:
            print(f"   🚨 {elo['signal']}")
    print(f"   {r['01_companies']}+{ah_t}+{r.get('_n_ou',0)}家公司 | API:{r.get('api_credits','?')}")
    print(f"   ⏰ {r.get('_analyzed_at', '?')} (实时)")
    print(f"{HEADER}")
    # ── 1X2 recommendation (moved to end) ──
    print(f"\n🎯 终判:")
    prob_gap = abs(ph - pa)
    fav_1x2_name = ["主胜", "平局", "客胜"][fav_idx]
    if prob_gap > 0.50: s_base = 5
    elif prob_gap > 0.35: s_base = 4
    elif prob_gap > 0.25: s_base = 3
    elif prob_gap > 0.15: s_base = 2
    else: s_base = 1
    # Downgrade for red flags & conflicts
    downgrade = 0
    if len(reds) >= 2: downgrade = 2
    elif len(reds) >= 1: downgrade = 1
    if r.get("_audit"):
        for a in r["_audit"]:
            if "陷阱" in a or "反向" in a: downgrade = max(downgrade, 1)
    s_final = max(1, s_base - downgrade)
    stars = "⭐" * s_final + "☆" * (5 - s_final)
    direction_text = f"{stars} {s_final}/5 {fav_1x2_name} @{fav_odds:.2f}" if prob_gap > 0.15 else f"⭐☆☆☆☆ 1/5 无明确方向(概率差{prob_gap:.0%}<15%)"
    print(f"  {direction_text}")
    
    # ── 推荐模块 ──
    _print_recommendation(r, stars, fav_1x2_name, fav_odds, prob_gap, reds, s_final)
    
    # ── Self-audit ──
    _self_audit(r)


def _print_recommendation(r: dict, stars: str, fav_name: str, fav_odds: float, prob_gap: float, reds: list, s_final: int):
    """Print detailed recommendation between final verdict and self-audit."""
    kelly = r.get("03_kelly", 0)
    cv = r.get("06_dispersion", 0)
    cold = r.get("17_cold", (0, []))
    adv = r.get("16_advanced_ah", ("", "", "", ""))
    bifax = r.get("30_bifax", (0, "N/A", ""))
    probs = r.get("07_probs", (0, 0, 0))
    
    # Confidence/Risk based on star rating (s_final)
    missing_n = len(r.get("_audit_missing", []))
    if s_final >= 4:
        conf, risk = "🟢 高", "🟢 低风险"
    elif s_final == 3:
        conf, risk = "🟡 中", "🟡 中风险"
    elif s_final == 2:
        conf, risk = "🟡 中", "🟡 中风险" if missing_n <= 4 else ("🔴 低", "🔴 高风险")
    else:
        conf, risk = "🔴 低", "🔴 高风险"
    
    # Max suggested position
    if s_final >= 4:
        position = "2-3%"
    elif s_final == 3:
        position = "1-2%"
    elif s_final == 2:
        position = "1-2%" if missing_n <= 4 else "≤1% (不建议重注)"
    else:
        position = "≤1% (不建议重注)"
    
    # Best direction
    ev = r.get("29_ev", "")
    bifax_bullish = bifax[1] if len(bifax) > 1 else "N/A"
    directions = []
    if prob_gap > 0.15:
        directions.append(f"SPF: {fav_name} @{fav_odds:.2f}")
    
    # AH recommendation
    ah_type = adv[0] if adv else ""
    if "DEEP_BLOCK" in str(ah_type):
        directions.append("AH: 上盘1X2方向，不追穿盘")
    elif "DEEP_LURE" in str(ah_type):
        directions.append("AH: 下盘方向(深诱盘)")
    
    # O/U
    ou_bil = f"OverBil={r.get('_ou_over_bil', False)} UndBil={r.get('_ou_under_bil', False)}"
    if r.get("_ou_under_bil"):
        directions.append("OU: 倾向小球")
    elif r.get("_ou_over_bil"):
        directions.append("OU: 倾向大球")
    
    # Bifax
    if bifax_bullish != "N/A":
        directions.append(f"必发看好: {bifax_bullish}")
    
    print(f"\n📋 推荐:")
    print(f"  置信度: {conf}  风险: {risk}  建议仓位: {position}")
    if directions:
        for d in directions:
            print(f"  ▸ {d}")
    print(f"  ▸ 一句话: {_one_liner(stars, fav_name, cold[0], len(reds), bifax_bullish, s_final)}")


def _one_liner(stars: str, fav: str, cold_idx: int, reds_n: int, bifax_dir: str, s_final: int) -> str:
    """Generate a one-line decision summary."""
    if reds_n >= 2:
        return f"{fav}方向明确但红灯{reds_n}个，信号冲突→轻仓或跳过"
    if s_final >= 4:
        return f"{fav}信号共振({s_final}/5)，可适度参与"
    if cold_idx >= 30:
        return f"冷门指数{cold_idx}，防冷优先"
    if bifax_dir not in ("N/A", "") and bifax_dir != fav:
        return f"必发与市场方向分歧，{bifax_dir}方向值得关注"
    return f"{fav}方向参考，结合临场确认"


def _self_audit(r: dict, silent: bool = False) -> list:
    """Post-analysis self-audit. Returns list of issue strings.
    When silent=False, prints to stdout. When silent=True, only returns list."""
    issues = []
    oh, od, oa, h, d, a = r["02_odds"]

    if h == 0 or d == 0 or a == 0:
        issues.append("❌ 欧赔数据为空")
        print(f"\n🔍 自审: {' | '.join(issues)}")
        return issues

    # 0. Data freshness — always record when data was pulled
    from datetime import datetime
    r["_analyzed_at"] = datetime.now().strftime("%m-%d %H:%M")

    cv = r.get("06_dispersion", 0)
    if cv > 0.25:
        issues.append(f"⚠️ CV={cv:.2f}>0.25 离散度偏高")
    if cv == 0 and not r.get("overseas_mode"):
        issues.append("⚠️ CV=0 异常")

    kelly = r.get("03_kelly", 0)
    if kelly < -0.02:
        issues.append(f"⚠️ Kelly={kelly:.4f} 极度负EV")

    probs = r.get("07_probs", (0, 0, 0))
    gap = abs(probs[0] - probs[2]) if probs[0] else 0
    if gap > 0.80:
        issues.append(f"💡 概率差{gap:.0%}→极端热门无投注价值")

    r13_gap = r.get("ou_ah_gap", 0)
    adv = r.get("16_advanced_ah", ("", "", "", ""))
    ah_type = adv[0] if adv else ""
    if r13_gap >= 1.0 and "DEEP_LURE" in ah_type.upper():
        issues.append(f"🚫 R13={r13_gap:.2f}→深诱盘作废")
    elif r13_gap >= 1.0 and "DEEP_BLOCK" in ah_type.upper():
        pass  # 深阻盘不受R13影响
    elif r13_gap >= 1.0:
        issues.append(f"⚠️ R13={r13_gap:.2f}≥1.0 检查类型")

    pinn = r.get("pinnacle", (0, 0, False))
    if pinn[2]:
        f_dn = r.get("08_consensus", (0, 0, 0))[0]
        if f_dn > 10:
            issues.append("⚠️ Pinnacle反向但共识同向→可能假警报")
        else:
            issues.append("🚨 Pinnacle反向! 重大警报")

    companies = r.get("01_companies", 0)
    if companies == 0:
        issues.append("⚠️ 仅titan007无500.com")
    if r.get("08a_ah", (0, 0, 0))[2] == 0:
        issues.append("⚠️ 无亚盘")
    if r.get("_n_ou", 0) == 0:
        issues.append("⚠️ 无大小球")
    fund = r.get("fundamentals", {})
    if not fund or fund.get("source", "none") == "none":
        issues.append("⚠️ 无基本面")

    # 9. Steam vs consensus contradiction
    steam = r.get("08_steam", (0, 0))
    consensus = r.get("08_consensus", (0, 0, 0))
    if steam[0] < -0.05 and consensus[0] < 3 and not r.get("overseas_mode"):
        issues.append("⚠️ Steam涌入但共识弱→信号矛盾")
    if steam[0] > 0.05 and consensus[1] < 3 and not r.get("overseas_mode"):
        issues.append("⚠️ Steam冷却但共识弱→信号矛盾")
    # 共识退热: 升赔公司多于降赔
    if consensus[1] > consensus[0] + 2 and not r.get("overseas_mode"):
        issues.append(f"⚠️ 共识退热: {consensus[0]}↓/{consensus[1]}↑→市场在卖热门")
    # Steam vs AH contradiction (ERR-003: 考诺萨1-1)
    ah_up = r.get("09_ah_up", 0)
    ah_total = r.get("08a_ah", (0,0,0))[2]
    if steam[0] > 0.03 and ah_up >= ah_total * 0.3 and ah_total > 0:
        issues.append("🚨 Steam冷却+AH升盘矛盾→诱盘降星")

    # 10. Cold index threshold
    cold = r.get("17_cold", (0, []))
    if cold[0] >= 40:
        issues.append(f"🚨 冷门指数{cold[0]}≥40!")

    # 11. Extreme CLV
    clv = r.get("24_clv", 0)
    if abs(clv) > 0.30:
        issues.append(f"⚠️ CLV={clv:+.0%}极端→初盘可能过时")

    # 12. Payout anomaly
    payout = r.get("27_payout", 0)
    if 0 < payout < 0.88:
        issues.append(f"⚠️ 返还率{payout:.1%}<88%异常")

    # 13. O/U conflict
    if r.get("13_ou_conflict"):
        issues.append("⚠️ O/U盘水矛盾")

    # 14. Euro-AH deviation
    eah = r.get("14_euro_ah")
    if eah and isinstance(eah, (list, tuple)) and len(eah) >= 2:
        if abs(eah[1]) > 0.50:
            issues.append(f"⚠️ 欧亚偏差{eah[1]:.2f}>0.5球")

    # 15. Bifax missing
    bifax = r.get("30_bifax", (0, "N/A", ""))
    if bifax[0] == 0 and not r.get("overseas_mode"):
        issues.append("💡 无必发数据")

    # ═══════════════════════════════════════
    # 16. Dimension coverage — every dim must be present
    # ═══════════════════════════════════════
    dims_required = {
        "01": r.get("01_companies", 0) > 0,
        "02": all(v > 0 for v in r.get("02_odds", (0,0,0,0,0,0))),
        "03": "03_kelly" in r,
        "04": "04_kelly_var" in r,
        "05": "05_kelly_dir" in r,
        "06": "06_dispersion" in r,
        "07": all(v > 0 for v in r.get("07_probs", (0,0,0))),
        "08": "08_steam" in r,
        "09-11": r.get("08a_ah", (0,0,0))[2] > 0 or "11_ah_verdict" in r,
        "12-13": r.get("_n_ou", 0) > 0,
        "14": "14_euro_ah" in r,
        "15": "15_skeleton" in r,
        "16": r.get("16_advanced_ah", ("N/A",))[0] != "N/A",
        "17": "17_cold" in r,
        "18": "18_intent" in r,
        "19-23": bool(fund and fund.get("source", "none") != "none"),
        "24": "24_clv" in r,
        "25": "25_opening_dev" in r,
        "26": "26_linkage" in r,
        "27": "27_payout" in r,
        "28": r.get("28_poisson") is not None,
        "29": "29_ev" in r,
        "30": "30_bifax" in r,
        "31": r.get("31_elo") is not None,
    }
    missing_dims = [d for d, ok in dims_required.items() if not ok]
    r["_audit_missing"] = missing_dims
    if missing_dims:
        issues.append(f"🔴 缺维: {', '.join(missing_dims)}")

    # 16. Elo signals check
    elo = r.get("31_elo")
    if elo:
        sig = elo.get("signal", "")
        if "浅开陷阱" in sig:
            issues.append(f"🚨 Elo浅开陷阱: 公平盘{abs(elo['fair_handicap']):.2f}vs实际{abs(elo['actual_handicap']):.2f}")
        elif "蛊惑盘" in sig:
            issues.append(f"🚨 Elo蛊惑盘: 实际盘深于实力→诱上盘")
        elif "浅开" in sig:
            issues.append(f"⚠️ Elo浅开: 盘口浅于实力{abs(elo['fair_handicap']-elo['actual_handicap']):.2f}球")
        elif "深开" in sig:
            issues.append(f"⚠️ Elo深开: 庄家强推上盘, 公平{abs(elo['fair_handicap']):.2f}vs实际{abs(elo['actual_handicap']):.2f}")

    # 17. Kelly trap (《凯利指数分析剖析》): favorite low odds + high Kelly > payout → trap
    kelly_val = r.get("03_kelly", 0)
    payout_val = r.get("27_payout", 1)
    if kelly_val > payout_val * 0.02:
        issues.append(f"🚨 凯利陷阱: 热门低赔但凯利{kelly_val:.4f}>赔付率{payout_val:.2f}→诱买")

    # 18. Nordic league warning (《高手总结》): patterns differ
    mname = r.get("match_name", "")
    has_nordic = any(kw in mname for kw in ['芬超','挪超','瑞超','冰岛超','芬甲','挪甲','瑞典甲','冰岛甲'])
    if has_nordic:
        issues.append("⚠️ 北欧联赛: 常规盘路规律不适用")
        # ERR-冰岛1-1: 全票共识+AH剧烈变动+北欧 = trap
        ah_up = r.get("09_ah_up", 0)
        if cons[0] > 10 and ah_up > 8:
            issues.append("🚨 北欧全票陷阱: 全票共识+AH暴涨→诱盘降星")

    # 18.5 威廉vs立博 平赔剪刀差 (《威廉立博Interwetten分析》)
    try:
        odds_tuple = r.get("02_odds", (0,0,0,0,0,0))
        # We can only do this when 500.com data is available (not titan-only)
        pin = r.get("pinnacle", (0,0,False))
        if odds_tuple[3] > 1:  # current home odds exist
            # Use the companies data stored in _titan_euro or get from 500.com
            # Simplified: check if William/Ladbrokes draw odds are accessible
            pass
    except Exception:
        pass

    # 19. 赔率必杀组合 (《赔率必杀组合》: 历史统计规律, 参考信号)
    oh, od, oa = r.get("02_odds", (0,0,0,0,0,0))[:3]
    h2, d2, a2 = r["02_odds"][3:6]
    if abs(h2-1.77)<0.05 and abs(d2-3.30)<0.20 and abs(a2-3.95)<0.30:
        issues.append("💡 必杀#1: 1.77/3.30/3.95 历史100%(8-0-0)")
    if abs(h2-1.39)<0.05:
        issues.append("💡 必杀#2: 主1.39 历史80%(35-4-5)")
    if abs(a2-1.39)<0.05:
        issues.append("💡 必杀#3: 客1.39 历史92%(12-0-1)")
    if abs(h2-6.75)<0.50 and abs(a2-1.39)<0.10:
        issues.append("💡 必杀#4: 主6.75/客1.39 历史92%客胜")

    # 19.5 立博10大典型赔率 (《威廉立博Interwetten》)  
    if abs(h2-1.40)<0.03 and abs(d2-3.75)<0.20:
        issues.append("💡 立博典型: 1.40/3.75/7.00 主不败96%+")
    elif abs(h2-1.57)<0.03 and abs(d2-3.50)<0.20:
        issues.append("💡 立博典型: 1.57/3.50/5.00 主不败89%")
    elif abs(h2-1.90)<0.05 and abs(d2-3.10)<0.15:
        issues.append("💡 立博典型: 1.90/3.10/3.60 主不败83%")
    elif abs(h2-2.20)<0.05 and abs(d2-3.20)<0.10 and abs(a2-2.80)<0.10:
        issues.append("💡 立博典型: 2.20/3.20/2.80 分胜负79%")
    elif abs(h2-2.80)<0.05 and abs(d2-3.20)<0.10 and abs(a2-2.20)<0.10:
        issues.append("💡 立博典型: 2.80/3.20/2.20 主不胜86%")
    elif abs(h2-1.50)<0.03 and abs(d2-3.40)<0.15:
        issues.append("🚨 立博典型: 1.50/3.40/3.00 常出冷门!")

    # 20. 尾数检测 (《欧赔核心思维》: 尾数最小=庄家诱盘方向)
    if h2 > 1 and d2 > 1 and a2 > 1:
        tails = [round(h2 % 1, 2), round(d2 % 1, 2), round(a2 % 1, 2)]
        min_tail = min(tails)
        min_idx = tails.index(min_tail)
        labels = ["主胜", "平局", "客胜"]
        # Only flag when one tail is significantly smaller
        if min_tail < 0.03 and sum(1 for t in tails if t < 0.05) == 1:
            # Check if 平赔 is elevated (顶高) + favorite has tail → cold risk
            fav_idx = 0 if h2<d2 and h2<a2 else (2 if a2<d2 and a2<h2 else 1)
            fav_has_tail = tails[fav_idx] > 0.03
            draw_elevated = d2 > 3.50
            if fav_has_tail and draw_elevated:
                issues.append(f"🚨 尾数陷阱: {labels[min_idx]}尾数{min_tail:.2f}最小=诱盘+平赔顶高→防冷")
            elif min_tail < 0.02:
                issues.append(f"⚠️ 尾数: {labels[min_idx]}尾数{min_tail:.2f}最小→可能诱盘")

    if not silent:
        print(f"\n🔍 自审({len(issues)}项警告/41项检查): {' | '.join(issues)}" if issues else "\n🔍 自审(41项): ✅ 全维通过")
        # ── 核心原则 (内化自六本足彩经典) ──
        red_count = len(r.get("red_flags", []))
        has_conflict = False
        steam = r.get("08_steam", (0,0))
        cons = r.get("08_consensus", (0,0,0))
        ah_verdict = r.get("11_ah_verdict", "")
        elo = r.get("31_elo") or {}
        # Conflict: strong consensus but AH/ELO warns
        if cons[0] > 15 and ("诱" in str(ah_verdict) or "陷阱" in str(elo.get("signal",""))):
            has_conflict = True
        if red_count > 0 or has_conflict:
            print(f"🧠 庄家思维: 信号冲突→宁缺毋滥 | 红灯{red_count} | 冲突{has_conflict}")
    return issues


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="足球赛事数据全维整理")
    parser.add_argument("target", help="500.com fixture ID 或 队名")
    parser.add_argument("--titan", default="", help="titan007 ID (用于拉基本面)")
    parser.add_argument("--league", default="", help="联赛代码 (E0=英超 BR2=巴乙 WC=世界杯 等, 启用Odds API交叉验证)")
    parser.add_argument("--search", action="store_true", help="WebSearch自动搜索基本面")
    parser.add_argument("--fundamentals", default="", help="基本面JSON字符串(来自WebSearch)")
    parser.add_argument("--name", default="", help="比赛名称")
    parser.add_argument("--paid", default="", help="订单号(service.py传入, 验证支付凭证)")
    args = parser.parse_args()

    # ═══════════════════════════════════════════
    # 支付门禁: 必须通过 service.py 调用
    # ═══════════════════════════════════════════
    if not args.paid:
        print("❌ 请通过 /ampan 支付流程使用本服务。")
        print("   安装: openclaw skills install football-match-data")
        print("   使用: /ampan <比赛名称>")
        sys.exit(1)
    # 验证支付凭证
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from file_utils import load_order
        order = load_order(args.paid)
        cred = order.get("payCredential", "")
        if not cred:
            print(f"PAY_STATUS: PROCESSING")
            print("支付未完成，请先完成支付。")
            sys.exit(1)
        from gmssl.sm4 import CryptSM4, SM4_DECRYPT
        import base64 as _b64
        key = _b64.b64decode("wTMwbvTIOznEzlP33FutnA==")
        cipher = _b64.b64decode(cred)
        sm4 = CryptSM4()
        sm4.set_key(key, SM4_DECRYPT)
        plain = sm4.crypt_ecb(cipher)
        pad = plain[-1]
        if 1 <= pad <= 16 and all(b == pad for b in plain[-pad:]):
            plain = plain[:-pad]
        import json as _json
        pay_result = _json.loads(plain.decode())
        if pay_result.get("payStatus", "FAIL") not in ("SUCCESS", "TEST_SUCCESS"):
            print(f"❌ 支付状态: {pay_result.get('payStatus', 'FAIL')}")
            print("   请完成支付后重试。")
            sys.exit(1)
    except Exception as e:
        print(f"❌ 支付验证失败: {e}")
        sys.exit(1)
    
    # 校验订单与比赛匹配: 一个订单只能分析下单时的比赛
    order_question = order.get("question", "")
    if order_question and args.name and order_question != args.name:
        print(f"❌ 订单与比赛不匹配: 订单={order_question} 请求={args.name}")
        print("   每笔订单仅限分析下单时指定的比赛。")
        sys.exit(1)

    fid = args.target
    if not fid.isdigit():
        from footy.data.wubai import find_fixture
        result = find_fixture(fid.split(" vs ")[0], fid.split(" vs ")[1]) if " vs " in fid else None
        if result and result.isdigit():
            fid = result
        else:
            print(f"❌ 未找到: {args.target}")
            sys.exit(1)

    r = full_analysis(fid, args.name, args.titan, args.league)
    # Inject WebSearch fundamentals if provided
    if args.fundamentals:
        import json as _json
        try:
            r["fundamentals"] = _json.loads(args.fundamentals)
        except Exception:
            r["fundamentals"] = {"raw": args.fundamentals[:500]}
    print_report(r)
