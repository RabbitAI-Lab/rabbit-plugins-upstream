#!/usr/bin/env python3
"""薪资数据库生成脚本 v2.0.0 — 诚实版 (honest provenance)

数据性质声明（重要）：
  records 中的薪资值是由 因子模型 生成的**参考区间估计**：
      基准区间(tier1_mid) × 层级系数 × 行业系数 × 城市系数 × [0.9, 1.1] 缓冲
  这些数值**不是**从招聘平台抓取的实时市场数据。
  scrape_samples 保留 74 条 Tavily 抓取交叉核对样本（2026-04~07，
  来自 data/scrape_samples.json）。经重新核对：32 条与模型值相同（v1 回填，
  无独立证据），29 条为真实抓取价格（28 条与模型偏差>10%，-80%~+432%），
  13 条非标准组合无法对照 —— 用于说明模型值的误差范围。

输出：data/salary_database.json
  { meta, cities, industries, levels, level_labels, unit_note,
    records: [5376 条模型估计],
    scrape_samples: [74 条交叉核对样本，含 drift_vs_modeled_pct] }

运行：python3 scripts/generate_salary_db.py [--out PATH] [--date YYYY-MM-DD]
（除 meta.generated_at 外为确定性输出）
"""
import argparse
import json
import os
from datetime import date

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_SKILL_ROOT = os.path.dirname(_SCRIPT_DIR)
SAMPLES_FILE = os.path.join(_SKILL_ROOT, "data", "scrape_samples.json")

# ── 因子模型参数（与 v1 相同算术，保证可复现）─────────────────────────────
TIER1_CITIES = ["北京", "上海", "广州", "深圳"]
TIER2_CITIES = ["杭州", "成都", "武汉", "南京", "西安", "苏州", "天津", "重庆"]
TIER3_CITIES = ["济南", "哈尔滨", "合肥", "昆明", "南昌", "贵阳", "太原", "兰州"]

INDUSTRIES = {
    "互联网/IT": 1.0, "金融/银行/保险": 1.1, "医疗/健康": 0.95, "教育培训": 0.75,
    "制造业/供应链": 0.8, "房地产/建筑": 0.85, "消费零售": 0.7,
    "文化传媒/娱乐": 0.75, "法律/咨询": 0.9, "政府/非营利": 0.7,
    "能源/化工": 0.85, "交通/物流": 0.8,
}

OCCUPATIONS = {
    "后端开发工程师": {"tier1_mid": [15000, 22000], "tier2_factor": 0.75, "tier3_factor": 0.55},
    "前端开发工程师": {"tier1_mid": [13000, 20000], "tier2_factor": 0.75, "tier3_factor": 0.55},
    "算法工程师": {"tier1_mid": [18000, 28000], "tier2_factor": 0.75, "tier3_factor": 0.55},
    "产品经理": {"tier1_mid": [14000, 22000], "tier2_factor": 0.70, "tier3_factor": 0.50},
    "UI/UX设计师": {"tier1_mid": [10000, 17000], "tier2_factor": 0.75, "tier3_factor": 0.55},
    "数据分析师": {"tier1_mid": [12000, 20000], "tier2_factor": 0.75, "tier3_factor": 0.55},
    "金融分析师": {"tier1_mid": [15000, 25000], "tier2_factor": 0.75, "tier3_factor": 0.55},
    "保险经纪人": {"tier1_mid": [8000, 18000], "tier2_factor": 0.65, "tier3_factor": 0.45},
    "医生": {"tier1_mid": [15000, 25000], "tier2_factor": 0.80, "tier3_factor": 0.60},
    "教师": {"tier1_mid": [10000, 18000], "tier2_factor": 0.75, "tier3_factor": 0.60},
    "机械工程师": {"tier1_mid": [10000, 18000], "tier2_factor": 0.75, "tier3_factor": 0.55},
    "市场营销": {"tier1_mid": [10000, 18000], "tier2_factor": 0.70, "tier3_factor": 0.50},
}

LEVEL_FACTORS = {"entry": 1.0, "mid": 1.6, "senior": 2.5, "expert": 4.0}
LEVEL_LABELS = {
    "entry": "入门级（0-2年经验）", "mid": "中级（3-5年经验）",
    "senior": "资深（6-10年经验）", "expert": "专家级（10年以上）",
}
CITY_TIERS = {}
for _c in TIER1_CITIES:
    CITY_TIERS[_c] = "tier1"
for _c in TIER2_CITIES:
    CITY_TIERS[_c] = "tier2"
for _c in TIER3_CITIES:
    CITY_TIERS[_c] = "tier3"

# 2026 年公开数据校准锚点（用于对照模型值，不是数据来源）
CALIBRATION_ANCHORS = [
    {"point": "航空航天行业 人工智能工程师 平均招聘月薪", "value_rmb_month": 22787,
     "source": "智联招聘《2026年人工智能产业人才发展报告》(2026-07-21 发布, H1 2026 数据)",
     "closest_model": "算法工程师 tier1 mid: 25920-49280",
     "note": "模型区间中值显著高于平台平均招聘月薪，模型值应视为方向性参考"},
    {"point": "新能源行业 人工智能工程师 平均招聘月薪", "value_rmb_month": 22594,
     "source": "同上",
     "closest_model": "算法工程师 tier1 mid: 25920-49280", "note": "同上"},
    {"point": "算法工程师 平均招聘月薪（2025-02）", "value_rmb_month": 23510,
     "source": "智联招聘数据，新华社'新华视点'报道 (2025-03-26)",
     "closest_model": "算法工程师 tier1 mid: 25920-49280",
     "note": "平台月均值甚至低于模型区间下限"},
]


def modeled_range(city, industry, occupation, level):
    occ = OCCUPATIONS[occupation]
    tf = {"tier1": 1.0, "tier2": occ["tier2_factor"], "tier3": occ["tier3_factor"]}[CITY_TIERS[city]]
    lf = LEVEL_FACTORS[level]
    lo = int(occ["tier1_mid"][0] * lf * INDUSTRIES[industry] * tf * 0.9)
    hi = int(occ["tier1_mid"][1] * lf * INDUSTRIES[industry] * tf * 1.1)
    return lo, hi


def _rec(city, industry, occupation, level, lo, hi):
    return {
        "city_tier": CITY_TIERS[city], "city": city, "industry": industry,
        "occupation": occupation, "level": level,
        "salary_min": lo, "salary_max": hi, "salary_unit": "月薪",
        "data_source": "因子模型估计（非抓取市场数据）",
    }


def generate_salary_records():
    records = []
    for occupation in OCCUPATIONS:
        for city in TIER1_CITIES:
            for industry in INDUSTRIES:
                for level in LEVEL_FACTORS:
                    lo, hi = modeled_range(city, industry, occupation, level)
                    records.append(_rec(city, industry, occupation, level, lo, hi))
        main_industries = ["互联网/IT", "金融/银行/保险", "医疗/健康", "教育培训", "制造业/供应链"]
        for city in TIER2_CITIES:
            for industry in main_industries:
                for level in LEVEL_FACTORS:
                    lo, hi = modeled_range(city, industry, occupation, level)
                    records.append(_rec(city, industry, occupation, level, lo, hi))
        tiny_industries = ["互联网/IT", "金融/银行/保险", "制造业/供应链"]
        for city in TIER3_CITIES:
            for industry in tiny_industries:
                for level in LEVEL_FACTORS:
                    lo, hi = modeled_range(city, industry, occupation, level)
                    records.append(_rec(city, industry, occupation, level, lo, hi))
    return records


def load_scrape_samples():
    try:
        with open(SAMPLES_FILE, "r", encoding="utf-8") as f:
            return json.load(f).get("samples", [])
    except (OSError, json.JSONDecodeError) as exc:
        print(f"warning: scrape samples unavailable ({exc}); continuing without")
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=os.path.join(_SKILL_ROOT, "data", "salary_database.json"))
    parser.add_argument("--date", default=str(date.today()))
    args = parser.parse_args()

    records = generate_salary_records()
    drifts = []
    samples = []
    for s in load_scrape_samples():
        try:
            lo, hi = modeled_range(s["city"], s["industry"], s["occupation"], s["level"])
        except (KeyError, ValueError):
            s["drift_vs_modeled_pct"] = None
            s["note"] = "非标准组合（城市/职业不在因子模型内），无法对照"
        else:
            mid_s = (s.get("salary_min", 0) + s.get("salary_max", 0)) / 2
            mid_m = (lo + hi) / 2
            s["modeled_min"], s["modeled_max"] = lo, hi
            s["drift_vs_modeled_pct"] = round((mid_s - mid_m) / mid_m * 100, 1)
            if s["drift_vs_modeled_pct"] is not None:
                drifts.append(abs(s["drift_vs_modeled_pct"]))
        s.pop("verification_status", None)
        s.pop("verified_by", None)
        s.pop("verification_source", None)
        s.pop("drift_correction_by", None)
        s["cross_check"] = "Tavily抓取样本（非模型值，供误差对照）"
        samples.append(s)
    n_off = sum(1 for d in drifts if d > 10)
    n_identical = sum(1 for s in samples if s.get("modeled_min") == s.get("salary_min")
                      and s.get("modeled_max") == s.get("salary_max"))
    n_comparable = len(drifts)
    n_nonmodelable = len(samples) - n_comparable
    n_genuine = n_comparable - n_identical
    drifts_signed = [s["drift_vs_modeled_pct"] for s in samples
                     if s.get("drift_vs_modeled_pct") is not None
                     and not (s.get("modeled_min") == s.get("salary_min")
                              and s.get("modeled_max") == s.get("salary_max"))]

    db = {
        "meta": {
            "version": "2.0.0",
            "generated_at": args.date,
            "method": "因子模型：tier1基准区间 × 层级系数(entry1.0/mid1.6/senior2.5/expert4.0) × 行业系数(0.7~1.1) × 城市系数(tier1 1.0/tier2 0.75/tier3 0.55) × [0.9,1.1]缓冲",
            "provenance_statement": "records 为因子模型生成的参考区间估计，不是招聘平台抓取数据，不代表实时市场薪资；具体薪资以实时平台数据为准",
            "calibration_anchors": CALIBRATION_ANCHORS,
            "scrape_sample_summary": {
                "count": len(samples),
                "period": "2026-04-25 ~ 2026-07-26",
                "identical_to_model": n_identical,
                "genuine_scrapes_comparable": n_genuine,
                "genuine_over_10pct_from_model": n_off,
                "nonmodelable": n_nonmodelable,
                "genuine_drift_range_pct": [min(drifts_signed), max(drifts_signed)] if drifts_signed else None,
                "note": (
                    f"{n_identical}/{len(samples)} 条与因子模型值完全相同（系 v1 '验证'时由模型回填，无独立证据价值）；"
                    f"{n_genuine} 条为真实抓取价格，其中 {n_off} 条与模型偏差>10%（范围 "
                    f"{min(drifts_signed)}% ~ {max(drifts_signed)}%，极端值疑似抓取错误）；"
                    f"{n_nonmodelable} 条为非标准组合无法对照。结论：模型值应视为方向性参考，不可当作市场数据引用"
                ),
            },
            "total_records": len(records),
            "description": "中国各城市、各行业、各职业层级的薪资参考区间（模型估计），供职业规划参考使用",
        },
        "cities": {"tier1": TIER1_CITIES, "tier2": TIER2_CITIES,
                   "tier3": TIER3_CITIES, "tier4": ["其余地级市及县城"]},
        "industries": list(INDUSTRIES.keys()),
        "levels": list(LEVEL_FACTORS.keys()),
        "level_labels": LEVEL_LABELS,
        "unit_note": "薪资单位：人民币/月",
        "records": records,
        "scrape_samples": samples,
    }
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    print(f"command=salary-db status=ok records={len(records)} "
          f"scrape_samples={len(samples)} out={args.out} exit=0")


if __name__ == "__main__":
    main()
