#!/usr/bin/env python3
"""
pdd-check-restock：补货/清仓巡检。读取 pdd-sync-shop 落的数据（SQLite 零部署 /
企业模式 PDD_CH_URL），输出分级行动清单。纯读，不碰店铺后台。

计算逻辑（全部阈值可按商家自己的补货思路定制，见 ~/.pdd-data/restock_policy.json）：
  日均销量 = 近30天销量 / 30
  可售天数 = 当前库存 / 日均销量
  断货     = 库存 0 且近30天有销量
  即将断货 = 可售天数 < 采购周期(lead_days)，建议补至覆盖 采购周期+安全销量期(cover_days)
  积压     = 可售天数 > overstock_days
  滞销     = 近30天 0 销且有库存

用法: python3 check_restock.py [--mall <id>] [--lead-days 14] [--format text|json]
（--lead-days 临时覆盖本次采购周期；长期定制改 policy 文件）
"""
import sys, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import store  # noqa: E402

POLICY_PATH = os.path.expanduser(os.environ.get("PDD_RESTOCK_POLICY",
                                                "~/.pdd-data/restock_policy.json"))
DEFAULT_POLICY = {
    "_doc": "补货巡检参数。按贵司补货思路修改数值即可原地生效（无需改代码）。",
    "lead_days": 14,        # 采购周期（下单到入库天数）。可售天数低于它 → 即将断货
    "cover_days": 30,       # 安全销量期。补货建议 = 日均销 ×（采购周期+安全期）- 现库存
    "overstock_days": 90,   # 可售天数超过它 → 积压
    "slow_days": 30,        # 滞销判定窗口：近 N 天零销量且有库存 → 滞销（当前取数口径固定30天）
    "customized": False,     # 商家确认过自己的参数后请改为 true（关闭首次引导提示）
}


def load_policy():
    """(policy, first_run)。首次运行自动写默认值文件——文件本身就是可编辑的配置界面。"""
    if os.path.exists(POLICY_PATH):
        try:
            p = {**DEFAULT_POLICY, **json.load(open(POLICY_PATH))}
            return p, False
        except Exception:
            return dict(DEFAULT_POLICY), False
    try:
        os.makedirs(os.path.dirname(POLICY_PATH), exist_ok=True)
        with open(POLICY_PATH, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_POLICY, f, ensure_ascii=False, indent=1)
    except OSError:
        pass  # 沙箱只读也不阻塞巡检
    return dict(DEFAULT_POLICY), True


def methodology(pol):
    """把本次用的计算口径说清楚（给 agent 转述给用户/放进报表）。"""
    return {
        "daily_sales": "近30天销量 ÷ 30",
        "days_of_stock": "当前库存 ÷ 日均销量",
        "断货": "库存=0 且 近30天有销量",
        "即将断货": f"可售天数 < 采购周期 {pol['lead_days']} 天（有销量的商品）",
        "补货建议量": f"日均销量 × (采购周期{pol['lead_days']}天 + 安全销量期{pol['cover_days']}天) − 现库存",
        "积压": f"可售天数 > {pol['overstock_days']} 天",
        "滞销": "近30天 0 销量 且 有库存",
        "policy_file": POLICY_PATH,
        "policy_customized": bool(pol.get("customized")),
    }


def main():
    a = sys.argv
    def arg(k, d=None): return a[a.index(k) + 1] if k in a else d
    mall = arg("--mall")
    pol, first_run = load_policy()
    lead = int(arg("--lead-days", pol["lead_days"]))
    cover = int(pol["cover_days"])
    over = int(pol["overstock_days"])
    fmt = arg("--format", "text")

    try:
        store.ensure_schema()
        rows = [g for g in store.latest_goods(mall) if g.get("is_onsale")]
    except Exception as e:
        print(json.dumps({"ok": False, "reason": "store_unreachable", "detail": str(e)[:150],
                          "action": {"type": "notify_user",
                                     "message": "数据不可用：请先运行一次 pdd-sync-shop 同步店铺数据"}},
                         ensure_ascii=False)); sys.exit(2)
    if not rows:
        print(json.dumps({"ok": False, "reason": "no_data",
                          "action": {"type": "notify_user",
                                     "message": "暂无店铺数据：请先运行一次 pdd-sync-shop"}},
                         ensure_ascii=False)); sys.exit(2)

    acts = {"断货": [], "即将断货": [], "积压": [], "滞销": []}
    for r in rows:
        dos, daily = r["days_of_stock"], r["daily_sales_30d"]
        if r["quantity"] == 0 and r["sold_quantity_30d"] > 0:
            acts["断货"].append({**r, "advice": f"尽快补货，建议 {max(1, round(daily*(lead+cover)))} 件"})
        elif dos is not None and dos < lead and r["sold_quantity_30d"] > 0:
            need = max(1, round(daily * (lead + cover) - r["quantity"]))
            acts["即将断货"].append({**r, "advice": f"剩 {dos} 天可售，建议补 {need} 件（覆盖采购周期{lead}天+{cover}天销量）"})
        elif dos is not None and dos > over:
            acts["积压"].append({**r, "advice": f"库存 {r['quantity']}、可售约 {dos} 天，建议促销或暂停补货"})
        elif r["sold_quantity_30d"] == 0 and r["quantity"] > 0:
            acts["滞销"].append({**r, "advice": f"近30天无销量、库存 {r['quantity']}，建议调价或参加活动"})

    n = sum(len(v) for v in acts.values())
    as_of = max(r["collected_at"] for r in rows)
    meta = methodology(pol)
    invite = None
    if first_run or not pol.get("customized"):
        invite = {"type": "notify_user",
                  "message": ("本次巡检用的是通用默认口径（采购周期14天、积压线90天等，"
                              "完整算法已随结果给出）。每家公司的补货思路不同——"
                              "欢迎把贵司的采购周期、安全库存天数、清仓标准告诉我，"
                              "我会把巡检口径原地改成您认可的算法，之后一直按它执行。")}
    if fmt == "json":
        out = {"ok": True, "as_of": as_of, "scanned": len(rows),
               "total_actions": n, "actions": acts,
               "methodology": meta, "first_run": first_run}
        if invite:
            out["action"] = invite
        print(json.dumps(out, ensure_ascii=False)); return

    lines = [f"补货/清仓巡检　在售 {len(rows)} 款，{n} 项需处理　数据截至 {as_of} (UTC)"]
    for k in ("断货", "即将断货", "积压", "滞销"):
        if acts[k]:
            lines.append(f"\n[{k}] {len(acts[k])} 款")
            for it in acts[k]:
                lines.append(f"  - {it['goods_name'][:20]}（¥{it['price_min_yuan']}，30天销 {it['sold_quantity_30d']}）：{it['advice']}")
    if n == 0:
        lines.append("全部商品库存状态正常。")
    lines.append("\n—— 判定口径 ——")
    for k in ("断货", "即将断货", "补货建议量", "积压", "滞销"):
        lines.append(f"  {k}：{meta[k]}")
    lines.append(f"  （参数文件：{POLICY_PATH}，可按贵司补货思路修改）")
    if invite:
        lines.append("\n" + invite["message"])
    print("\n".join(lines))


if __name__ == "__main__":
    main()
