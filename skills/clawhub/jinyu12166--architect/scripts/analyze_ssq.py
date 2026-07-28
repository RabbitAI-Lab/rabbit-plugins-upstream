#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
双色球智能分析生成器
基于 SQLite 数据库中的累计历史数据，做冷热统计、
特征分布分析和规则过滤。推荐号码通过 clawtip 支付验证后由 service.py 调用生成。
"""
import argparse
import os
import random
import sqlite3
import sys
from collections import Counter
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ssq_data.db")
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "最新分析结果.md")

# ============================================================
# 1. 数据库读取
# ============================================================

def get_recent_draws(conn, n=20):
    """获取最近 n 期开奖数据"""
    c = conn.cursor()
    c.execute("""
        SELECT code, red1, red2, red3, red4, red5, red6, blue, draw_date
        FROM draws ORDER BY code DESC LIMIT ?
    """, (n,))
    rows = c.fetchall()
    result = []
    for row in rows:
        result.append({
            "code": row[0],
            "reds": sorted([row[1], row[2], row[3], row[4], row[5], row[6]]),
            "blue": row[7],
            "date": row[8],
        })
    return list(reversed(result))


def get_all_draws(conn):
    """获取所有历史数据"""
    c = conn.cursor()
    c.execute("SELECT code, red1, red2, red3, red4, red5, red6, blue, draw_date FROM draws ORDER BY code")
    rows = c.fetchall()
    result = []
    for row in rows:
        result.append({
            "code": row[0],
            "reds": sorted([row[1], row[2], row[3], row[4], row[5], row[6]]),
            "blue": row[7],
            "date": row[8],
        })
    return result


def get_db_info(conn):
    """获取数据库统计信息"""
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM draws")
    total = c.fetchone()[0]
    c.execute("SELECT MIN(code) FROM draws")
    min_code = c.fetchone()[0]
    c.execute("SELECT MAX(code) FROM draws")
    max_code = c.fetchone()[0]
    return {"total": total, "min_code": min_code, "max_code": max_code}


# ============================================================
# 2. 统计模块
# ============================================================

def compute_hot_cold(all_draws, n=20):
    """计算红球冷热属性"""
    recent_reds = [r for draw in all_draws[-n:] for r in draw["reds"]]
    counter = Counter(recent_reds)

    stats = []
    for num in range(1, 34):
        count = counter.get(num, 0)
        if count >= 6:
            attr = "HOT"
        elif count >= 3:
            attr = "WARM"
        else:
            attr = "COLD"

        miss_count = 0
        for draw in reversed(all_draws[-n:]):
            if num in draw["reds"]:
                break
            miss_count += 1

        bar_len = min(count, 10)
        bar = "#" * bar_len + "-" * (10 - bar_len)

        stats.append({
            "number": num, "count": count, "miss": miss_count,
            "freq": round(count / (n * 6) * 100, 1),
            "attr": attr, "bar": bar,
        })

    return stats


def compute_blue_stats(all_draws, n=20):
    """计算蓝球统计"""
    recent_blues = [draw["blue"] for draw in all_draws[-n:]]
    counter = Counter(recent_blues)
    stats = []
    for num in range(1, 17):
        count = counter.get(num, 0)
        miss_count = 0
        for draw in reversed(all_draws[-n:]):
            if draw["blue"] == num:
                break
            miss_count += 1
        if count >= 3:
            attr = "HOT"
        elif count >= 1:
            attr = "WARM"
        else:
            attr = "COLD"
        stats.append({"number": num, "count": count, "miss": miss_count, "attr": attr})
    return stats


def compute_odd_even_ratio(reds_list):
    """统计奇偶比"""
    ratios = Counter()
    for draw in reds_list:
        odd = sum(1 for r in draw["reds"] if r % 2 == 1)
        ratios[f"{odd}:{6-odd}"] += 1
    return ratios


def compute_ac_value(reds):
    """计算一组红球的 AC 值"""
    diffs = set()
    for i in range(len(reds)):
        for j in range(i + 1, len(reds)):
            diffs.add(abs(reds[i] - reds[j]))
    return len(diffs) - 5


def compute_ac_distribution(reds_list):
    """统计 AC 值分布"""
    acs = Counter()
    for draw in reds_list:
        ac = compute_ac_value(draw["reds"])
        acs[ac] += 1
    return acs


def compute_zone_distribution(reds_list):
    """统计三区分布"""
    zones = Counter()
    for draw in reds_list:
        z1 = sum(1 for r in draw["reds"] if 1 <= r <= 11)
        z2 = sum(1 for r in draw["reds"] if 12 <= r <= 22)
        z3 = sum(1 for r in draw["reds"] if 23 <= r <= 33)
        zones[f"{z1}:{z2}:{z3}"] += 1
    return zones


# ============================================================
# 3. 筛选引擎
# ============================================================

def get_zone(reds):
    """获取三区分布"""
    z1 = sum(1 for r in reds if 1 <= r <= 11)
    z2 = sum(1 for r in reds if 12 <= r <= 22)
    z3 = sum(1 for r in reds if 23 <= r <= 33)
    return [z1, z2, z3]


def has_triple_consecutive(reds):
    """检查是否有三连号"""
    for i in range(len(reds) - 2):
        if reds[i + 2] - reds[i + 1] == 1 and reds[i + 1] - reds[i] == 1:
            return True
    return False


def count_consecutive_pairs(reds):
    """统计二连号数量"""
    count = 0
    for i in range(len(reds) - 1):
        if reds[i + 1] - reds[i] == 1:
            count += 1
    return count


def passes_filters(reds, stats_data):
    """
    过滤规则检查，返回 (True, details_list) 或 (False, fail_reason)
    """
    checks = []

    # 奇偶比
    odd = sum(1 for r in reds if r % 2 == 1)
    even = 6 - odd
    oe = f"{odd}:{even}"
    if oe in ("3:3", "4:2", "2:4"):
        checks.append(("odd_even", oe, "OK"))
    else:
        return False, f"奇偶比 {oe} 不符合要求"

    # AC值
    ac = compute_ac_value(reds)
    if 7 <= ac <= 10:
        checks.append(("ac", str(ac), "OK"))
    else:
        return False, f"AC值 {ac} 不在7-10范围内"

    # 三区分布
    z1, z2, z3 = get_zone(reds)
    zone_str = f"{z1}:{z2}:{z3}"
    ok_zones = ["2:2:2", "3:2:1", "2:3:1", "3:1:2", "1:3:2", "2:1:3", "1:2:3"]
    if zone_str in ok_zones:
        checks.append(("zone", zone_str, "OK"))
    else:
        return False, f"三区分布 {zone_str} 过于偏态"

    # 和值
    s = sum(reds)
    if 80 <= s <= 150:
        checks.append(("sum", str(s), "OK"))
    else:
        return False, f"和值 {s} 不在80-150范围内"

    # 三连号
    if has_triple_consecutive(reds):
        return False, "含有三连号，已禁止"

    # 二连号
    pairs = count_consecutive_pairs(reds)
    if pairs <= 1:
        checks.append(("pairs", str(pairs), "OK"))
    else:
        return False, f"含有{pairs}组二连号，超过限制"

    # 冷热配比
    hot = sum(1 for r in reds if any(s["number"] == r and s["attr"] == "HOT" for s in stats_data))
    warm = sum(1 for r in reds if any(s["number"] == r and s["attr"] == "WARM" for s in stats_data))
    cold = sum(1 for r in reds if any(s["number"] == r and s["attr"] == "COLD" for s in stats_data))
    if hot <= 3 and cold <= 3 and warm >= 2:
        checks.append(("hot_cold", f"{hot}H+{warm}W+{cold}C", "OK"))
    else:
        return False, f"冷热配比 {hot}热+{warm}温+{cold}冷 不合理"

    return True, checks


def generate_blue_candidates(blue_stats):
    """生成4枚备选蓝球"""
    candidates = sorted(blue_stats, key=lambda x: (-x["miss"], x["count"]))
    selected = []
    for b in candidates:
        if b["number"] not in [s["number"] for s in selected]:
            selected.append(b)
        if len(selected) >= 4:
            break
    return selected[:4]


def try_pick_sets(stats_data, blue_candidates, max_attempts=50000):
    """尝试生成符合过滤条件的号码组合"""
    hot_set = set(s["number"] for s in stats_data if s["attr"] == "HOT")
    warm_set = set(s["number"] for s in stats_data if s["attr"] == "WARM")
    cold_set = set(s["number"] for s in stats_data if s["attr"] == "COLD")
    all_nums = list(range(1, 34))

    valid_sets = []
    attempted = 0
    count_per_blue = max_attempts // 4 if blue_candidates else max_attempts

    for bc in blue_candidates[:4]:
        blue_ball = bc["number"]
        local_attempts = 0

        while local_attempts < count_per_blue and len(valid_sets) < 5:
            local_attempts += 1
            attempted += 1

            # 构建候选池：优先温号，再热号，再冷号
            pool = list(warm_set) + list(hot_set) + list(cold_set)
            if not pool:
                pool = all_nums

            random.shuffle(pool)
            reds = sorted(pool[:6])

            # 检查重复
            too_similar = False
            for vs in valid_sets:
                if len(set(reds) & set(vs["reds"])) >= 4:
                    too_similar = True
                    break
            if too_similar:
                continue

            result = passes_filters(reds, stats_data)
            if result[0]:
                checks = result[1]
                valid_sets.append({
                    "reds": reds,
                    "blue": blue_ball,
                    "odd_even": f"{sum(1 for r in reds if r%2==1)}:{sum(1 for r in reds if r%2==0)}",
                    "ac": compute_ac_value(reds),
                    "zone": f"{get_zone(reds)[0]}:{get_zone(reds)[1]}:{get_zone(reds)[2]}",
                    "sum_val": sum(reds),
                    "pairs": count_consecutive_pairs(reds),
                    "hot_count": sum(1 for r in reds if r in hot_set),
                    "warm_count": sum(1 for r in reds if r in warm_set),
                    "cold_count": sum(1 for r in reds if r in cold_set),
                    "checks": checks,
                })

            if len(valid_sets) >= 5:
                break

    return valid_sets, attempted


# ============================================================
# 4. 报告生成
# ============================================================

def _attr_label(attr):
    return {"HOT": "[热]", "WARM": "[温]", "COLD": "[冷]"}.get(attr, attr)


def generate_report(conn, recommend=False):
    """生成完整的分析报告"""
    db_info = get_db_info(conn)
    recent = get_recent_draws(conn, 20)
    all_draws = get_all_draws(conn)

    if not recent:
        print("[ERROR] 数据库为空，请先运行 fetch_ssq.py 抓取数据")
        return None

    red_stats = compute_hot_cold(all_draws, 20)
    blue_stats = compute_blue_stats(all_draws, 20)
    odd_even_dist = compute_odd_even_ratio(recent)
    ac_dist = compute_ac_distribution(recent)
    zone_dist = compute_zone_distribution(recent)
    sum_list = [sum(d["reds"]) for d in recent]
    sum_avg = round(sum(sum_list) / len(sum_list)) if sum_list else 0

    blue_candidates = generate_blue_candidates(blue_stats)
    valid_sets, attempts = try_pick_sets(red_stats, blue_candidates)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = []

    lines.append("# 双色球智能分析报告")
    lines.append("")
    lines.append(f"> 生成时间：{now}")
    lines.append(f"> 数据基准：近20期（{db_info.get('min_code', 'N/A')} ~ {db_info.get('max_code', 'N/A')}）")
    lines.append(f"> 数据库总计：{db_info.get('total', 0)} 期历史数据")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ---- 近20期原始数据 ----
    lines.append("## 一、近20期开奖原始数据")
    lines.append("")
    lines.append("| 期号 | 红球 | 蓝球 | 日期 |")
    lines.append("|------|------|------|------|")
    for draw in recent:
        red_str = " ".join(f"{r:02d}" for r in draw["reds"])
        lines.append(f"| {draw['code']} | {red_str} | {draw['blue']:02d} | {draw['date']} |")
    lines.append("")

    # ---- 红球冷热统计 ----
    lines.append("## 二、红球冷热属性统计（近20期）")
    lines.append("")
    lines.append("| 球号 | 出现次数 | 遗漏 | 频率 | 属性 | 热力图 |")
    lines.append("|------|---------|------|------|------|--------|")
    for s in red_stats:
        lines.append(f"| {s['number']:02d} | {s['count']} | {s['miss']} | {s['freq']}% | {_attr_label(s['attr'])} | {s['bar']} |")
    lines.append("")

    # ---- 蓝球统计 ----
    lines.append("## 三、蓝球统计（近20期）")
    lines.append("")
    lines.append("| 球号 | 出现次数 | 遗漏 | 属性 |")
    lines.append("|------|---------|------|------|")
    for s in blue_stats:
        lines.append(f"| {s['number']:02d} | {s['count']} | {s['miss']} | {_attr_label(s['attr'])} |")
    lines.append("")

    # ---- 特征分布 ----
    lines.append("## 四、特征分布统计")
    lines.append("")

    lines.append("### 奇偶比分布")
    lines.append("")
    lines.append("| 比例 | 出现次数 | 频率 |")
    lines.append("|------|---------|------|")
    for ratio in sorted(odd_even_dist.keys()):
        c = odd_even_dist[ratio]
        lines.append(f"| {ratio} | {c} | {round(c/len(recent)*100, 1)}% |")
    lines.append("")

    lines.append("### AC值分布")
    lines.append("")
    lines.append("| AC值 | 出现次数 | 频率 |")
    lines.append("|------|---------|------|")
    for ac_val in sorted(ac_dist.keys()):
        c = ac_dist[ac_val]
        lines.append(f"| {ac_val} | {c} | {round(c/len(recent)*100, 1)}% |")
    lines.append("")

    lines.append("### 三区分布")
    lines.append("")
    lines.append("| 分布 | 出现次数 | 频率 |")
    lines.append("|------|---------|------|")
    for zone, c in sorted(zone_dist.items(), key=lambda x: -x[1]):
        lines.append(f"| {zone} | {c} | {round(c/len(recent)*100, 1)}% |")
    lines.append("")

    lines.append("### 和值统计")
    lines.append("")
    lines.append(f"- 平均和值：**{sum_avg}**")
    lines.append(f"- 最小和值：{min(sum_list)}")
    lines.append(f"- 最大和值：{max(sum_list)}")
    lines.append("")

    # ---- 备选蓝球 ----
    if recommend:
        lines.append("## 五、备选蓝球推荐（4枚）")
        lines.append("")
        reasons = ["遗漏最深，冷号反弹首选", "次冷补位，奇偶搭配", "遗漏适中，多策略覆盖", "偶数码补充，组合多样化"]
        lines.append("| 序号 | 蓝球 | 次数 | 遗漏 | 属性 | 推荐理由 |")
        lines.append("|------|------|------|------|------|---------|")
        for i, c in enumerate(blue_candidates[:4]):
            lines.append(f"| {i+1} | {c['number']:02d} | {c['count']} | {c['miss']} | {_attr_label(c['attr'])} | {reasons[i]} |")
        lines.append("")
    
        # ---- 最终号码 ----
        lines.append("## 六、最终推荐号码（5组）")
        lines.append("")
        lines.append(f"> 经 {attempts} 次尝试筛选，以下组合全部通过过滤规则校验")
        lines.append("")
    
        # 交叉检查
        lines.append("### 组间重复检查")
        lines.append("")
        lines.append("| 对比 | 重复红球数 | 判定 |")
        lines.append("|------|-----------|------|")
        for i in range(len(valid_sets)):
            for j in range(i + 1, len(valid_sets)):
                overlap = len(set(valid_sets[i]["reds"]) & set(valid_sets[j]["reds"]))
                tag = "OK" if overlap <= 2 else "WARN"
                lines.append(f"| 第{i+1}组 vs 第{j+1}组 | {overlap} | {tag} |")
        lines.append("")
    
        for idx, vs in enumerate(valid_sets):
            red_str = "  ".join(f"{r:02d}" for r in vs["reds"])
            lines.append(f"### 第{idx+1}组")
            lines.append("")
            lines.append(f"- **红球**：{red_str}")
            lines.append(f"- **蓝球**：{vs['blue']:02d}")
            lines.append("")
            lines.append("| 维度 | 数值 | 状态 |")
            lines.append("|------|------|------|")
            lines.append(f"| 奇偶比 | {vs['odd_even']} | OK |")
            lines.append(f"| AC值 | {vs['ac']} | OK |")
            lines.append(f"| 三区分布 | {vs['zone']} | OK |")
            lines.append(f"| 和值 | {vs['sum_val']} | OK |")
            lines.append(f"| 连号 | {vs['pairs']}组 | OK |")
            lines.append(f"| 冷热配比 | {vs['hot_count']}H+{vs['warm_count']}W+{vs['cold_count']}C | OK |")
            lines.append("")
            notes_parts = []
            if vs["cold_count"] >= 2:
                notes_parts.append(f"追冷策略({vs['cold_count']}枚冷号)")
            if vs["odd_even"] == "3:3":
                notes_parts.append("奇偶均衡配置")
            elif vs["odd_even"] == "4:2":
                notes_parts.append("奇数略偏倚")
            else:
                notes_parts.append("偶数略偏倚")
            if vs["zone"] == "2:2:2":
                notes_parts.append("三区均衡布局")
            notes_parts.append(f"AC值{vs['ac']}高概率区间")
            lines.append("**选号备注**：" + "；".join(notes_parts))
            lines.append("")
    
    
    # ---- 免责声明 ----
    lines.append("---")
    lines.append("")
    lines.append("> **风险提示**：本报告基于历史数据统计分析生成，彩票开奖为随机独立事件，")
    lines.append("> 任何分析方法均不能保证中奖。请理性购彩，量力而行。")
    lines.append("")

    return "\n".join(lines)


def main(recommend=False):
    if recommend:
        print("NOTICE: --recommend flag requires prior payment verification via clawtip service.")
        print("        Paid recommendations should only be generated after service.py confirms payment.")
        print()
    print("=" * 50)
    print("  双色球智能分析生成器")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    if not os.path.exists(DB_PATH):
        print(f"\n[ERROR] 数据库不存在: {DB_PATH}")
        print("   请先运行 fetch_ssq.py 抓取数据")
        return 1

    conn = sqlite3.connect(DB_PATH)
    try:
        report = generate_report(conn, recommend=recommend)
        if report:
            with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"\n[DONE] 分析报告已生成：{OUTPUT_PATH}")
            print(f"       报告大小：{len(report)} 字符")
            return 0
        else:
            return 1
    finally:
        conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SSQ analysis report generator")
    parser.add_argument("--recommend", action="store_true",
                        help="Include paid recommendation numbers (use only after clawtip payment verification)")
    args = parser.parse_args()
    sys.exit(main(recommend=args.recommend))
