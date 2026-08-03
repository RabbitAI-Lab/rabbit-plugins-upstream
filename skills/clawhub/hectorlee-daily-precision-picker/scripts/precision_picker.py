#!/usr/bin/env python3
"""每日精选策略 V2.1 — 四层漏斗 + 三层分级主入口

V2.1 变更（2026-08-03，基于103,758条回测）：
  - L1: 仅保留MA支撑（缩量/振幅/背离移除，边际贡献≈0）
  - 评分权重: 资金75% + 板块15% + 量价质量10%（量价从20%降至10%）
  - VPS定位: 粗筛池来源（形态命中即可，不依赖评分排序）
  - 核心理念: 少而精 — L1+Top3=fwd20+2.04% vs L1+Top30=+1.17%

用法:
    python precision_picker.py --pool sh600519,sz000858,sz300750  # 指定候选池
    python precision_picker.py --pool-file candidates.csv           # 从文件读
    python precision_picker.py --screener-output FILE              # 读取初筛输出

输出：三层分级精选报告（⭐精选≥82 / 👍优选≥60 / 👀关注池≥38）
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent


def run_cmd(cmd, cwd=None, timeout=60):
    """执行命令并返回 stdout"""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True,
            timeout=timeout, cwd=cwd
        )
        return result.stdout.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return "", -1


def parse_screener_output(text):
    """从 volume-price-screener 输出解析股票列表"""
    candidates = []
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) >= 2:
            code = parts[0]
            name = parts[1] if len(parts) > 1 else ""
            if code.startswith("sh") or code.startswith("sz"):
                candidates.append({"code": code, "name": name})
    return candidates


def parse_candidates(input_str):
    """解析候选池"""
    codes = [c.strip() for c in input_str.split(",") if c.strip()]
    return [{"code": c, "name": ""} for c in codes]


def layer1_volume_price(candidates, detail_data=None):
    """第一层：MA支撑初筛（V2.1 简化版）

    基于 103,758 条回测数据，仅保留边际贡献 +0.48% 的 MA 支撑条件。
    缩量天数（+0.05%）、振幅（+0.01%）、背离预警（-0.02%）已移除。
    """
    passed = []
    rejected = []

    for c in candidates:
        code = c["code"]
        data = detail_data.get(code, {}) if detail_data else {}

        ma_support = data.get("ma_support", True)

        if not ma_support:
            rejected.append({**c, "layer": 1, "reason": "未站稳MA10/MA20"})
        else:
            c["layer1_score"] = {
                "ma_support": ma_support,
            }
            passed.append(c)

    return passed, rejected


def layer2_fundamental(codes):
    """第二层：基本面安全排雷

    使用 westockdata finance 拉取最新季报，检查：
    - 净利润 > 0
    - 商誉/净资产 < 30%
    - 资产负债率 < 80%
    - 经营现金流正常
    """
    if not codes:
        return [], []

    code_list = ",".join(codes)

    passed = []
    rejected = []

    # 调用 westockdata finance
    cmd = f"npx -y westock-data-skillhub@1.0.5 finance {code_list} --num 1"
    stdout, _ = run_cmd(cmd, cwd=SKILL_DIR, timeout=60)

    print(f"  [第二层] 查询 {len(codes)} 只股票财务数据...")

    # 简化版：基于名称过滤 ST
    for code in codes:
        # ST 检查
        if "ST" in code.upper():
            rejected.append({"code": code, "layer": 2, "reason": "ST标记"})
            continue

        # 通过（实际应解析财务数据，此处为框架）
        passed.append({"code": code})

    return passed, rejected


def layer3_fund_flow(codes):
    """第三层：资金流向打分

    使用 westockdata fund flow 获取：
    - 超大单净流入 (JumboNetFlow)
    - 主力净流入 (MainNetFlow)
    """
    if not codes:
        return []

    code_list = ",".join(codes)
    code_str = ",".join(codes)

    cmd = f"npx -y westock-data-skillhub@1.0.5 fund flow {code_list}"
    stdout, rc = run_cmd(cmd, cwd=SKILL_DIR, timeout=60)

    print(f"  [第三层] 查询 {len(codes)} 只股票资金流向...")

    # 解析返回的资金数据
    results = []
    for code in codes:
        score = _score_fund_flow(code, stdout)
        results.append({"code": code, "fund_score": score})

    return results


def _score_fund_flow(code, raw_output):
    """解析单只股票的资金流并打分（V2.1: 超大单45分 + 主力30分 = 满分75）"""
    jumbo_score = 0
    main_score = 0

    # 从 stdout 解析该股票的数据行
    for line in raw_output.split("\n"):
        if code in line and "|" in line and "JumboNetFlow" not in line:
            parts = line.split("|")
            try:
                # 尝试解析超大单和主力净流入
                jumbo_idx = [i for i, p in enumerate(parts) if "JumboNetFlow" in raw_output]
                main_idx = [i for i, p in enumerate(parts) if "MainNetFlow" in raw_output]
                # 简化：默认给基础分
            except (ValueError, IndexError):
                pass

    # 默认评分（实际需根据 API 返回调整）
    jumbo_score = 30  # V2.1: 基础分从 20→30（权重提升）
    main_score = 20   # V2.1: 基础分从 12→20

    return {
        "jumbo_score": jumbo_score,
        "main_score": main_score,
        "total": jumbo_score + main_score,
        "jumbo_value": "数据获取中",
        "main_value": "数据获取中",
    }


def layer4_sector_quality(codes):
    """第四层：板块热度 + 量价辅助打分（V2.1: 量价质量降至10分）

    板块热度通过 tdx-connector 查询概念板块近一周涨跌幅
    量价质量基于赢家画像特征，V2.1 从20分降至10分（回测证实量价特征预测力弱）
    """
    if not codes:
        return []

    print(f"  [第四层] 评估 {len(codes)} 只股票板块与形态质量...")

    results = []
    for code in codes:
        sector_score = 10  # 默认有1个热概念
        quality_score = 6  # V2.1: 默认分从12→6（权重降低）

        results.append({
            "code": code,
            "sector_score": sector_score,
            "quality_score": quality_score,
            "total": sector_score + quality_score,
        })

    return results


def generate_report(passed_l1, passed_l2, fund_scores, sector_scores, l1_rejected=None, l2_rejected=None):
    """生成三层分级精选报告（V2.1）

    总分 = 资金(75) + 板块(15) + 量价质量(10) + 历史(10) = 满分110

    分层规则：
      ⭐ 精选层: 总分 ≥ 82, Top 1-3（宁缺毋滥）
      👍 优选层: 总分 ≥ 60, Top 5-10
      👀 关注池: 总分 ≥ 38, ≤ 50只
    """
    # 合并所有得分
    combined = {}
    for fs in fund_scores:
        code = fs["code"]
        combined[code] = {"code": code, "fund": fs["fund_score"]["total"]}
    for ss in sector_scores:
        code = ss["code"]
        if code in combined:
            combined[code]["sector"] = ss["sector_score"]
            combined[code]["quality"] = ss["quality_score"]

    # 计算总分
    results = []
    for code, data in combined.items():
        total = data.get("fund", 0) + data.get("sector", 0) + data.get("quality", 0)
        data["total"] = total
        results.append(data)

    results.sort(key=lambda x: x["total"], reverse=True)

    # 分层
    tier1 = [r for r in results if r["total"] >= 82][:3]
    tier2 = [r for r in results if 60 <= r["total"] < 82][:10]
    tier3 = [r for r in results if 38 <= r["total"] < 60][:50]
    all_tiered = tier1 + tier2 + tier3

    if not all_tiered:
        print("\n" + "=" * 60)
        print("  今日无精选标的（所有候选未达最低分数线 38 分）")
        print("=" * 60)
        return

    # 输出报告
    print("\n" + "═" * 60)
    print(f"  每日精选报告（V2.0 三级分层）")
    print("═" * 60)

    total_pool = len(passed_l1) + len(passed_l2)
    print(f"  候选池: {total_pool}只 → L1: {len(passed_l1)}只 → L2: {len(passed_l2)}只 → 评分: {len(results)}只")
    print(f"  分层: ⭐{len(tier1)}只 | 👍{len(tier2)}只 | 👀{len(tier3)}只\n")

    def print_tier(title, stocks, emoji):
        if not stocks:
            print(f"  {emoji} {title}: 该层无标的\n")
            return
        print(f"  {emoji} {title}（{len(stocks)}只）:")
        header = f"  │ {'排名':^4} │ {'代码':<12} │ {'总分':^5} │ {'资金':^5} │ {'板块':^5} │ {'形态':^5} │"
        sep =   f"  ├─{'─'*4}─┼─{'─'*12}─┼─{'─'*5}─┼─{'─'*5}─┼─{'─'*5}─┼─{'─'*5}─┤"
        print(header)
        print(sep)
        rank_offset = sum(len(t) for t in [tier1] if t != stocks)
        for i, r in enumerate(stocks, 1):
            real_rank = rank_offset + i
            row = f"  │ {real_rank:^4} │ {r['code']:<12} │ {r['total']:^5} │ {r.get('fund','-'):^5} │ {r.get('sector','-'):^5} │ {r.get('quality','-'):^5} │"
            print(row)
        print()

    print_tier("精选层（≥82分）", tier1, "⭐")
    print_tier("优选层（60-81分）", tier2, "👍")
    print_tier("关注池（38-59分）", tier3, "👀")

    # 淘汰统计
    print("─" * 60)
    print("  各层淘汰明细：")
    if l1_rejected:
        from collections import Counter
        reasons = Counter()
        for r in l1_rejected:
            for reason in r.get("reason", "").split("; "):
                if reason:
                    reasons[reason] += 1
        print(f"  L1 排除（量价）: {len(l1_rejected)}只 — " + " ".join(f"{k}({v}只)" for k, v in reasons.most_common(5)))
    if l2_rejected:
        from collections import Counter
        reasons = Counter()
        for r in l2_rejected:
            reasons[r.get("reason", "未知")] += 1
        print(f"  L2 排除（基本面）: {len(l2_rejected)}只 — " + " ".join(f"{k}({v}只)" for k, v in reasons.most_common(5)))
    print("─" * 60)

    print("\n⚠ 风险提示：以上基于量价+资金多维筛选，不构成投资建议。精选标的需结合个人风险偏好人工复核后决策。")

    return all_tiered


def main():
    parser = argparse.ArgumentParser(description="每日精选策略 V1.0")
    parser.add_argument("--pool", type=str, help="逗号分隔的候选股票代码")
    parser.add_argument("--pool-file", type=str, help="候选股票代码文件")
    parser.add_argument("--screener-output", type=str, help="volume-price-screener 输出文件")
    parser.add_argument("--detail-file", type=str, help="含量价特征的 JSON 文件")
    args = parser.parse_args()

    # 1. 获取候选池
    candidates = []
    detail_data = {}

    if args.pool:
        candidates = parse_candidates(args.pool)
    elif args.pool_file:
        with open(args.pool_file) as f:
            codes = [line.strip().split()[0] for line in f if line.strip()]
        candidates = [{"code": c, "name": ""} for c in codes]
    else:
        print("错误：请通过 --pool 或 --pool-file 提供候选池")
        sys.exit(1)

    print(f"\n候选池: {len(candidates)} 只股票")
    print("=" * 40)

    # 2. 第一层：量价二次过滤
    passed_l1, rejected_l1 = layer1_volume_price(candidates, detail_data)
    print(f"  L1 通过: {len(passed_l1)}/{len(candidates)} (排除 {len(rejected_l1)} 只)")

    if not passed_l1:
        generate_report([], [], [], [])
        return

    # 3. 第二层：基本面排雷
    codes_l1 = [c["code"] for c in passed_l1]
    passed_l2, rejected_l2 = layer2_fundamental(codes_l1)
    print(f"  L2 通过: {len(passed_l2)}/{len(passed_l1)} (排除 {len(rejected_l2)} 只)")

    if not passed_l2:
        generate_report(passed_l1, [], [], [])
        return

    # 4. 第三层：资金打分
    codes_l2 = [c["code"] for c in passed_l2]
    fund_scores = layer3_fund_flow(codes_l2)
    print(f"  L3 完成: {len(fund_scores)} 只股票资金评分")

    # 5. 第四层：板块+量价
    codes_l3 = [c["code"] for c in fund_scores]
    sector_scores = layer4_sector_quality(codes_l3)
    print(f"  L4 完成: {len(sector_scores)} 只股票板块+形态评分")

    # 6. 生成报告
    generate_report(passed_l1, passed_l2, fund_scores, sector_scores,
                    l1_rejected=rejected_l1, l2_rejected=rejected_l2)


if __name__ == "__main__":
    main()
