#!/usr/bin/env python
"""足球赛事数据一键诊断 — 跑完全部能跑的数据，清楚告诉你漏了什么。

用法:
  python scripts/ampan_analyze.py 1335728                     # 只给 fixture_id
  python scripts/ampan_analyze.py 1335728 --name "德国vs美国"  # 带比赛名
  python scripts/ampan_analyze.py 1335728 --bifax             # 同时拉必发数据

输出:
  ✅ 已完成项（绿色）
  ❌ 缺失项（红色，附解决建议）
  📊 数据摘要

退出码: 0=全部通过, 1=有缺失
"""
from __future__ import annotations

import argparse
import sys
import os
from pathlib import Path

# Ensure src is on path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))


def header(text: str) -> None:
    print(f"\n{'─' * 55}")
    print(f"  {text}")
    print(f"{'─' * 55}")


def ok(text: str) -> str:
    return f"  ✅ {text}"


def fail(text: str) -> str:
    return f"  ❌ {text}"


def warn(text: str) -> str:
    return f"  ⚠️ {text}"


def info(text: str) -> str:
    return f"     {text}"


def analyze(fixture_id: str, match_name: str = "", fetch_bifax: bool = False) -> int:
    """Run full pipeline, return number of missing items."""
    from footy.analysis.orchestrator import (
        MatchData, run_full_pipeline, gate_analysis, assert_ready,
    )

    name = match_name or f"Fixture #{fixture_id}"

    header(f"赛事数据诊断: {name}")

    # ============================================================
    # Step 1: 拉取赔率数据
    # ============================================================
    print("\n📡 正在拉取数据...")

    data = MatchData(match_name=name, fixture_id=fixture_id)
    errors = []

    # --- 欧赔 ---
    print(info("欧赔 (500.com)..."), end=" ")
    try:
        from footy.data.wubai import get_odds_full
        full = get_odds_full(fixture_id)
        if full["company_count"] >= 5:
            data.odds_count = full["company_count"]
            current = full.get("current", {})
            opening = full.get("opening", {})

            if "Bet365" in current:
                data.odds_instant = current["Bet365"]
            elif current:
                data.odds_instant = next(iter(current.values()))

            if "Bet365" in opening:
                data.odds_opening = opening["Bet365"]
            elif opening:
                data.odds_opening = next(iter(opening.values()))

            data.odds_source = "500.com"
            data.odds_verified = True
            data.checklist.mark("01", f"{data.odds_count}家公司")
            data.checklist.mark("08", "初盘→即时已计算")

            # 初盘偏差
            from footy.analysis.orchestrator import verify_opening_vs_current
            steam = verify_opening_vs_current(data.odds_opening, data.odds_instant)
            data.opening_deviation = steam
            data.checklist.mark("25", f"Steam: {steam['direction']} ({steam['magnitude']})")

            print(f"✅ {data.odds_count}家")
        else:
            print(f"⚠️ 仅{full['company_count']}家")
            errors.append("欧赔公司数不足")
    except Exception as e:
        print(f"❌ {e}")
        errors.append(f"欧赔拉取失败: {e}")

    # --- O/U ---
    print(info("大小球 (500.com)..."), end=" ")
    try:
        from footy.data.ou_data import fetch_ou as _fetch_ou
        ou = _fetch_ou(fixture_id)
        if ou and ou.bookmakers:
            data.ou_verified = True
            data.ou_data = {
                "avg_open_line": ou.avg_open_line,
                "avg_current_line": ou.avg_current_line,
                "trend": ou.line_trend,
                "bias": ou.over_under_bias,
                "company_count": ou.company_count,
            }
            data.checklist.mark("12", f"{ou.company_count}家, 均线{ou.avg_current_line:.2f}")
            data.checklist.mark("13", f"趋势: {ou.line_trend}")
            print(f"✅ {ou.company_count}家, 均线{ou.avg_current_line:.2f}")
        else:
            print("⚠️ 无数据")
            errors.append("大小球数据缺失")
    except Exception as e:
        print(f"❌ {e}")
        errors.append(f"大小球拉取失败: {e}")

    # --- 必发 ---
    if fetch_bifax:
        print(info("必发 (auto-collect)..."), end=" ")
        try:
            from footy.data.bifax import fetch_bifax_data, quick_verify
            bifax_data = fetch_bifax_data(fixture_id, name)
            if bifax_data:
                result = quick_verify(bifax_data, name)
                data.bifax_data = bifax_data
                data.bifax_result = {
                    "verdict": result.verdict,
                    "score": result.total_score,
                    "recommendation": result.recommendation,
                    "bullish_on": result.bullish_on,
                }
                data.bifax_verified = result.all_passed
                data.checklist.mark("30", f"必发四步: {result.verdict} (评分{result.total_score:+d})")
                print(f"✅ {result.verdict}")
            else:
                print("⚠️ 自动采集无数据")
                data.checklist.mark("30", "待采集(需WebFetch)", status="⚠️")
        except Exception as e:
            print(f"⚠️ {e}")
            data.checklist.mark("30", f"必发采集失败: {e}", status="⚠️")
    else:
        data.checklist.mark("30", "未采集（加 --bifax 开启）", status="⚠️")

    # ============================================================
    # Step 1.5: Auto-fill all computable checklist dimensions
    # ============================================================
    print(info("自动填充清单..."), end=" ")
    try:
        from footy.analysis.auto_signals import auto_fill_checklist
        data.home = name.split(" vs ")[0].strip() if " vs " in name else ""
        data.away = name.split(" vs ")[1].strip() if " vs " in name else ""
        data.ah_verified = True
        data.auto_signals = True
        filled = auto_fill_checklist(data)
        print(f"✅ 自动填充 {filled} 项")
    except Exception as e:
        print(f"⚠️ {e}")

    # ============================================================
    # Step 2: Gate 检查
    # ============================================================
    header("📋 Checklist 状态")

    cl = data.checklist

    # 已通过
    passed_items = [(i.id, i.name, i.detail) for i in cl.items if i.status == "✅"]
    if passed_items:
        print(f"\n  已通过 ({len(passed_items)}/{len(cl.items)}):")
        for item_id, item_name, detail in passed_items:
            detail_str = f" — {detail}" if detail else ""
            print(ok(f"{item_id} {item_name}{detail_str}"))

    # 缺失
    missing_items = [(i.id, i.name) for i in cl.items if i.status == "❌"]
    if missing_items:
        print(f"\n  缺失 ({len(missing_items)}项) — 需手动或调用分析模块:")
        for item_id, item_name in missing_items:
            hint = _get_hint(item_id)
            print(fail(f"{item_id} {item_name}"))
            if hint:
                print(info(f"→ {hint}"))

    # 警告
    warned_items = [(i.id, i.name, i.detail) for i in cl.items if i.status == "⚠️"]
    if warned_items:
        print(f"\n  警告 ({len(warned_items)}项):")
        for item_id, item_name, detail in warned_items:
            print(warn(f"{item_id} {item_name} — {detail}"))

    # ============================================================
    # Step 3: 数据摘要
    # ============================================================
    header("📊 已采集数据摘要")

    if data.odds_instant:
        h, d, a = data.odds_instant
        print(info(f"即时欧赔 (Bet365): {h:.2f} / {d:.2f} / {a:.2f}"))
    if data.odds_opening:
        h, d, a = data.odds_opening
        print(info(f"初盘欧赔 (Bet365): {h:.2f} / {d:.2f} / {a:.2f}"))
    if data.opening_deviation:
        dev = data.opening_deviation
        print(info(f"Steam: {dev['direction']} ({dev['magnitude']}), {dev.get('detail', '')}"))
    if data.ou_data:
        ou = data.ou_data
        print(info(f"大小球: 均线{ou['avg_current_line']:.2f}, {ou['trend']}, 偏向{ou['bias']}"))
    if data.bifax_result:
        bf = data.bifax_result
        print(info(f"必发: {bf['verdict']}"))

    # ============================================================
    # Step 4: Gate 判决
    # ============================================================
    header("🚧 Gate 判决")

    ready, missing = data.is_ready()
    if ready:
        print(ok("全部就绪！可以输出分析结论。"))
        print(info("调用 assert_ready(data) 不会抛出异常。"))
        return 0
    else:
        print(fail(f"被拦截 — {len(missing)} 项缺失"))
        print(info(f"缺失: {', '.join(missing[:10])}{'...' if len(missing) > 10 else ''}"))
        print()
        print(info("修复方法:"))
        print(info("  1. 逐个运行对应分析模块填入数据"))
        print(info("  2. 调用 data.checklist.mark('ID', '详情') 手动标记"))
        print(info("  3. 全部填完后 assert_ready(data) 才能通过"))
        return len(missing)


def _get_hint(item_id: str) -> str:
    """Return a hint for how to fill a missing checklist item."""
    hints = {
        "02": "调用 footy.analysis.value 的 devig 函数",
        "03": "调用 footy.analysis.value 计算凯利指数",
        "04": "需多家公司赔率计算方差",
        "05": "凯利方向判定（>1看好, <1不看好）",
        "06": "赔率离散度分析",
        "07": "隐含概率 = 1/赔率 归一化",
        "08a": "调用 footy.data.nowscore 或 500.com 亚盘页",
        "09": "亚盘升盘降水 → 看好信号",
        "10": "亚盘退盘升水 → 不看好信号",
        "11": "阻控诱判定（四模分析）",
        "14": "欧赔→理论亚盘 vs 实际亚盘对比",
        "15": "赔率骨架分类（1.30/1.44/1.57...）",
        "16": "调用 footy.analysis.advanced_ah 四模分析",
        "17": "调用 footy.analysis.cold_detector 9信号检测",
        "18": "调用 footy.analysis.bookmaker_mind 庄家意图",
        "19": "手动采集伤停信息",
        "20": "手动采集阵容/首发",
        "21": "手动或自动采集近期状态",
        "22": "赛事出线形势分析",
        "23": "心理惯性分析",
        "24": "CLV = (收盘赔率-初盘赔率)/初盘赔率",
        "26": "欧赔变动 vs 亚盘变动联动分析",
        "27": "返还率 = 1/(1/H+1/D+1/A), 异常<88%或>98%",
        "28": "调用 footy.models.poisson 泊松模型",
        "29": "EV = (公允概率*赔率-1), Edge判定",
        "30": "调用 footy.data.bifax.quick_verify() 四步验证",
    }
    return hints.get(item_id, "")


if __name__ == "__main__":
    print("❌ 请通过 /ampan 支付流程使用本服务。")
    print("   安装: openclaw skills install football-match-data")
    print("   使用: /ampan <比赛名称>")
    sys.exit(1)
    
    parser = argparse.ArgumentParser(description="赛事数据一键诊断")
    parser.add_argument("fixture_id", nargs="?", help="500.com fixture ID 或 球队名(如 '土耳其 vs 美国')")
    parser.add_argument("--name", "-n", default="", help="比赛名称（可选）")
    parser.add_argument("--bifax", action="store_true", help="尝试拉取必发数据")
    parser.add_argument("--full", action="store_true", help="输出标准化全维报告")
    args = parser.parse_args()

    fid = args.fixture_id
    if fid and not fid.isdigit():
        # User passed team names, try to find fixture ID
        if " vs " in fid.lower():
            parts = fid.split(" vs ", 1)
        elif "VS" in fid:
            parts = fid.split("VS", 1)
        elif "vs" in fid:
            parts = fid.split("vs", 1)
        else:
            print(f"❌ 无法解析: {fid}")
            print(f"   格式: '球队A vs 球队B' 或 fixture_id")
            sys.exit(1)
        team_a, team_b = parts[0].strip(), parts[1].strip()
        print(f"🔍 搜索: {team_a} vs {team_b} ...")
        from footy.data.wubai import find_fixture
        found = find_fixture(team_a, team_b)
        if not found:
            found = find_fixture(team_b, team_a)
        if found:
            print(f"   ✅ 找到 fixture_id: {found}")
            fid = found
            if not args.name:
                args.name = f"{team_a} vs {team_b}"
        else:
            print(f"   ❌ 未找到，请去 https://odds.500.com 查找 fixture_id")
            sys.exit(1)
    
    if not fid:
        parser.print_help()
        sys.exit(1)

    missing = analyze(fid, args.name, args.bifax)

    # --full: output standardized 31-dim report
    if args.full:
        try:
            from footy.analysis.report import quick_full_report
            print(quick_full_report(fid, args.name))
        except Exception as e:
            print(f"⚠️ 全维报告生成失败: {e}")

    sys.exit(0 if missing == 0 else 1)
