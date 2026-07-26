"""标准化全维报告生成器 — 确保31维无一遗漏。

每个 match 调用 generate_report(data) 即可输出完整31维分析报告。
所有维度从 MatchData + auto_signals 结果中提取，由模板强制输出。
"""
from __future__ import annotations

import math
from typing import Optional


def generate_report(data, ah=None, cold=None, adv=None, bifax_result=None) -> str:
    """Generate a complete 31-dimension analysis report as a formatted string."""
    import os
    if not os.environ.get("AMPAN_PAID"):
        raise RuntimeError("请通过 /ampan 支付流程使用本服务")
    lines = []
    h, d, a = data.odds_instant or (0, 0, 0)
    oh, od, oa = data.odds_opening or (0, 0, 0)
    fav_idx = min(range(3), key=lambda i: (h, d, a)[i]) if h > 0 else 0
    fav_names = [data.home or "主", "平局", data.away or "客"]
    fav_name = fav_names[fav_idx]
    fav_odds = (h, d, a)[fav_idx]

    # ═══════════════════════════════════════════
    lines.append("═" * 65)
    lines.append(f"  赛事数据报告: {data.match_name}")
    lines.append("═" * 65)

    # ── SECTION 1: ODDS CORE (01-08) ──
    lines.append("")
    lines.append("── 一、欧赔核心 (01-08) ──")
    lines.append(f"  即时: {h:.2f} / {d:.2f} / {a:.2f}")
    lines.append(f"  初盘: {oh:.2f} / {od:.2f} / {oa:.2f}")
    lines.append(f"  热门: {fav_name} @ {fav_odds:.2f}")
    if h > 0:
        imp_sum = 1/h + 1/d + 1/a
        payout = 1 / imp_sum
        ph, pd_, pa = (1/h)/imp_sum, (1/d)/imp_sum, (1/a)/imp_sum
        lines.append(f"  返还率: {payout:.1%}")
        lines.append(f"  公平概率: {fav_names[0]}{ph:.1%} / {fav_names[1]}{pd_:.1%} / {fav_names[2]}{pa:.1%}")

    # Steam
    if oh > 0:
        steam_h, steam_d, steam_a = h-oh, d-od, a-oa
        lines.append(f"  Steam: 主{steam_h:+.2f} 平{steam_d:+.2f} 客{steam_a:+.2f}")
        f_steam = (steam_h, steam_d, steam_a)[fav_idx]
        if f_steam < -0.05: steam_label = "强涌入"
        elif f_steam < -0.02: steam_label = "涌入"
        elif f_steam > 0.05: steam_label = "强冷却"
        elif f_steam > 0.02: steam_label = "冷却"
        else: steam_label = "稳定"
        lines.append(f"  热门Steam: {steam_label} ({f_steam:+.2f})")

    # Company consensus
    if hasattr(data, 'odds_companies') and data.odds_companies:
        cur = data.odds_companies
        lines.append(f"  公司数: {data.odds_count}家")

    # ── SECTION 2: KELLY + DISPERSION (02-06) ──
    lines.append("")
    lines.append("── 二、凯利 & 离散度 (02-06) ──")
    if h > 0:
        # Kelly
        kelly_25 = (pa * a - 1) / (a - 1) * 0.25 if a > 1 else 0
        status = "正EV" if kelly_25 > 0.005 else ("负EV" if kelly_25 < -0.005 else "平水")
        lines.append(f"  热门凯利(25%): {kelly_25:.4f} ({status})")
        # Edge for all outcomes
        lines.append(f"  Edge: 主{ph*h-1:+.2%} 平{pd_*d-1:+.2%} 客{pa*a-1:+.2%}")

    # Kelly variance & dispersion computed externally
    kv_str = ""
    cv_str = ""
    cl = data.checklist
    for item in cl.items:
        if item.id == "04" and item.detail:
            kv_str = item.detail
        if item.id == "06" and item.detail:
            cv_str = item.detail
    if kv_str:
        lines.append(f"  凯利方差: {kv_str}")
    if cv_str:
        lines.append(f"  离散度: {cv_str}")

    # ── SECTION 3: PINNACLE (derived) ──
    lines.append("")
    lines.append("── 三、Pinnacle 检测 ──")
    try:
        from footy.analysis.auto_signals import check_pinnacle
        pc = check_pinnacle(data.fixture_id)
        if pc.alert:
            lines.append(f"  🚨 {pc.alert}")
        else:
            lines.append(f"  ✅ Pinnacle Steam: {pc.pinnacle_steam:+.2f} | Bet365: {pc.bet365_steam:+.2f} | 同向: {pc.same_direction}")
    except Exception:
        lines.append("  待检测（需500.com数据）")

    # ── SECTION 4: ASIAN HANDICAP (08a-11, 16) ──
    lines.append("")
    lines.append("── 四、亚盘分析 (08a-11, 16) ──")
    if ah and ah.total > 0:
        lines.append(f"  均线: {ah.avg_open_line:.2f} → {ah.avg_close_line:.2f}")
        lines.append(f"  水位: {ah.avg_open_water_fav:.2f} → {ah.avg_close_water_fav:.2f}")
        lines.append(f"  升盘:{ah.line_up}/{ah.total} 降盘:{ah.line_down}/{ah.total}  降水:{ah.upper_water_drops} 升水:{ah.upper_water_rises}")
        lines.append(f"  阻控诱: {ah.verdict}")
    else:
        lines.append("  无亚盘数据")

    if adv:
        manipulation_cn = {
            "SHALLOW_BLOCK": "浅阻盘", "DEEP_BLOCK": "深阻盘",
            "SHALLOW_LURE": "浅诱盘", "DEEP_LURE": "深诱盘", "NEUTRAL": "均衡盘",
        }
        man_name = manipulation_cn.get(
            adv.manipulation.name if hasattr(adv.manipulation, 'name') else str(adv.manipulation),
            str(adv.manipulation),
        )
        lines.append(f"  四模: {man_name} | 信心:{adv.confidence} 风险:{adv.risk_level}")
        lines.append(f"  信号: {adv.signal[:100]}")
        lines.append(f"  建议: {adv.bet_suggestion}")

    # Euro-AH deviation
    for item in cl.items:
        if item.id == "14" and item.detail:
            lines.append(f"  欧亚偏差: {item.detail}")

    # Euro-AH linkage
    for item in cl.items:
        if item.id == "26" and item.detail:
            lines.append(f"  欧亚联动: {item.detail}")

    # ── SECTION 5: O/U (12-13) ──
    lines.append("")
    lines.append("── 五、大小球 (12-13) ──")
    if data.ou_data:
        ou = data.ou_data
        lines.append(f"  均线: {ou.get('avg_open_line', 0):.2f} → {ou.get('avg_current_line', 0):.2f}")
        lines.append(f"  趋势: {ou.get('trend', '?')}")
        lines.append(f"  偏向: {ou.get('bias', '?')}")
    for item in cl.items:
        if item.id == "13" and item.detail:
            lines.append(f"  水位: {item.detail}")

    # ── SECTION 6: COLD DETECTION (17) ──
    lines.append("")
    lines.append("── 六、冷门检测 (17) ──")
    if cold:
        lines.append(f"  指数: {cold.cold_index} ({cold.confidence})")
        for s in cold.signals:
            lines.append(f"    ⚡ {s.name} (+{s.weight}): {s.description[:80]}")
        lines.append(f"  建议: {cold.bet_suggestion}")
    else:
        for item in cl.items:
            if item.id == "17" and item.detail:
                lines.append(f"  {item.detail}")

    # ── SECTION 7: BOOKMAKER INTENT (18) ──
    lines.append("")
    lines.append("── 七、庄家意图 (18) ──")
    for item in cl.items:
        if item.id == "18" and item.detail:
            lines.append(f"  {item.detail}")

    # ── SECTION 8: FUNDAMENTALS (19-23) ──
    lines.append("")
    lines.append("── 八、基本面 (19-23) ──")
    for item in cl.items:
        if item.id in ("19", "20", "21", "22", "23") and item.detail:
            icon = "✅" if item.status == "✅" else "⚠️"
            lines.append(f"  {icon} {item.name}: {item.detail}")

    # ── SECTION 9: VALUE & MODELS (24-29) ──
    lines.append("")
    lines.append("── 九、价值 & 模型 (24-29) ──")
    for item in cl.items:
        if item.id in ("24", "25", "27", "28", "29") and item.detail:
            lines.append(f"  {item.id} {item.name}: {item.detail}")

    # ── SECTION 10: BIFAX (30) ──
    lines.append("")
    lines.append("── 十、必发四步验证 (30) [合成数据，非真实交易所] ──")
    if bifax_result:
        lines.append(f"  评分: {bifax_result.total_score:+d}  |  {bifax_result.verdict}")
        lines.append(f"  看好: {bifax_result.bullish_on}")
        lines.append(f"  全部通过: {bifax_result.all_passed}")
        for s in bifax_result.steps:
            icon = "✅" if s.passed else "❌"
            lines.append(f"  Step{s.step} [{s.name}]: {icon} {s.signal} ({s.detail[:80]})")
        lines.append(f"  建议: {bifax_result.recommendation[:120]}")
    else:
        for item in cl.items:
            if item.id == "30" and item.detail:
                lines.append(f"  {item.detail}")

    # ── SECTION 11: ODDS SKELETON (15) ──
    lines.append("")
    lines.append("── 十一、赔率骨架 & 其他 ──")
    for item in cl.items:
        if item.id == "15" and item.detail:
            lines.append(f"  骨架: {item.detail}")

    # ── GATE ──
    lines.append("")
    lines.append("═" * 65)
    ready, missing = data.is_ready()
    all_items = cl.items
    passed = sum(1 for i in all_items if i.status == "✅")
    warned = sum(1 for i in all_items if i.status == "⚠️")
    missing_n = sum(1 for i in all_items if i.status == "❌")
    lines.append(f"  Gate: {'✅ READY' if ready else '❌ BLOCKED'}  |  "
                 f"{passed}✅ {warned}⚠️ {missing_n}❌  ({len(all_items)}维)")
    if missing:
        lines.append(f"  缺失: {', '.join(missing[:8])}")
    lines.append("═" * 65)

    return "\n".join(lines)


# ── Quick convenience ──

def quick_full_report(fixture_id: str, match_name: str = "") -> str:
    """One-call full report: fetch data, auto-fill, generate report.

    Requires network access to 500.com.
    """
    from footy.analysis.orchestrator import MatchData, run_full_pipeline
    from footy.analysis.auto_signals import check_ah_trap
    from footy.analysis.cold_detector import detect_cold
    from footy.analysis.advanced_ah import analyze_advanced_ah
    from footy.analysis.euro_ah import detect_deviation
    from footy.data.bifax import fetch_bifax_data, quick_verify
    import logging
    logging.basicConfig(level=logging.WARNING)

    home, away = "", ""
    if " vs " in match_name:
        parts = match_name.split(" vs ", 1)
        home, away = parts[0].strip(), parts[1].strip()

    data = MatchData(match_name=match_name, fixture_id=fixture_id, home=home, away=away)
    data = run_full_pipeline(data.match_name, data.home, data.away, fixture_id,
                             fetch_bifax=True)

    h, d, a = data.odds_instant or (0, 0, 0)
    fav_idx = min(range(3), key=lambda i: (h, d, a)[i]) if h > 0 else 0
    fav_side = "away" if fav_idx == 2 else "home"
    ah = check_ah_trap(fixture_id, fav_side)

    adv = None
    try:
        if ah.total > 0 and h > 0:
            adv = analyze_advanced_ah(h, d, a, ah.avg_open_line, ah.avg_close_line,
                                      ah.avg_open_water_fav, ah.avg_close_water_fav)
    except Exception:
        pass

    cold = None
    try:
        dev = detect_deviation(h, d, a, ah.avg_close_line) if h > 0 else None
        cold = detect_cold(home, away, h, d, a, ah.avg_close_line,
                          host_is_dog=(h > a),
                          ha_euro_deviation_signal=dev.signal if dev else "")
    except Exception:
        pass

    bf_result = None
    try:
        bf_data = data.bifax_data or fetch_bifax_data(fixture_id, match_name)
        if bf_data:
            bf_result = quick_verify(bf_data, match_name)
    except Exception:
        pass

    return generate_report(data, ah, cold, adv, bf_result)
