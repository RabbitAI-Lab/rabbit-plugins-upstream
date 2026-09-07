# -*- coding: utf-8 -*-
"""
数据质量校验模块（从 build_house_dashboard.py 下沉，独立复用）
用法：
    from validate import validate_houses, validate_permits
    report = validate_houses(houses)   # houses: list[dict]
    print(report)

校验维度（与看板一致，统一为可机读 dict）：
    - 重复房源（楼栋|单元|楼层|房号 复合键去重）
    - 字段空值率（面积/套内/分摊/总价/单价/状态）
    - 面积异常（偏离中位数 >2x 或 <0.5x）
    - 单价异常（z-score > 3）
    - 总价/单价一致性（偏差 >1%）
以及 permits 级：
    - 证级重复（certificateNo 去重）
    - 批准套数/面积为空
"""
import math
import json


# 房源行标准字段（缺字段时按 None 处理，计入空值率）
HOUSE_FIELDS = ["楼栋", "单元", "楼层", "房号", "面积", "套内", "分摊", "总价", "单价", "状态"]


def _key(h):
    return "|".join(str(h.get(k, "")) for k in ["楼栋", "单元", "楼层", "房号"])


def validate_houses(houses):
    """返回 dict 质量报告（全 ASCII key，便于机读/JSON）。"""
    q = {}
    n = len(houses)
    q["房源总数"] = n

    # 1. 重复房源
    keys = [_key(h) for h in houses]
    dups = n - len(set(keys))
    q["重复房源"] = f"{dups} 套"

    # 2. 字段空值率
    null_rates = {}
    for f in ["面积", "套内", "分摊", "总价", "单价", "状态"]:
        miss = sum(1 for h in houses if h.get(f) in (None, "", 0))
        null_rates[f] = f"{miss}/{n} ({miss / n * 100:.1f}%)" if n else "0/0"
    q["空值率"] = null_rates

    # 3. 面积异常（中位数 0.5x~2x 之外）
    areas = [h["面积"] for h in houses if h.get("面积")]
    med = sorted(areas)[len(areas) // 2] if areas else 0
    area_abn = [h for h in houses if h.get("面积") and (h["面积"] > med * 2 or h["面积"] < med * 0.5)]
    q["面积异常"] = f"{len(area_abn)} 套 (中位数 {med:.1f}㎡)" if med else "N/A(无面积)"

    # 4. 单价 z-score
    priced = [h for h in houses if h.get("单价") and h["单价"] > 0]
    if priced:
        vals = [h["单价"] for h in priced]
        mu = sum(vals) / len(vals)
        sd = math.sqrt(sum((v - mu) ** 2 for v in vals) / len(vals)) or 1
        abn = [h for h in priced if abs(h["单价"] - mu) > 3 * sd]
        q["单价异常(z>3)"] = f"{len(abn)} 套 / 可售{len(priced)}套"
        q["可售均价"] = f"{mu:.0f} 元/㎡ (σ={sd:.0f})"
    else:
        q["单价异常(z>3)"] = "N/A(无单价)"

    # 5. 总价/单价一致性
    mismatch = [
        h for h in priced
        if h.get("面积") and h.get("总价")
        and abs(h["总价"] - h["单价"] * h["面积"]) / (h["单价"] * h["面积"]) > 0.01
    ]
    q["总价单价一致性"] = f"{len(mismatch)} 套偏差>1%"

    return q


def validate_permits(permits):
    """permits: list[dict]，至少含 certificateNo / project / approvedUnits / approvedArea。"""
    q = {}
    n = len(permits)
    q["证级总数"] = n
    nos = [p.get("certificateNo", "") for p in permits]
    q["重复证号"] = f"{n - len(set(nos))} 本"
    miss_u = sum(1 for p in permits if not p.get("approvedUnits"))
    miss_a = sum(1 for p in permits if not p.get("approvedArea"))
    q["批准套数缺失"] = f"{miss_u}/{n}"
    q["批准面积缺失"] = f"{miss_a}/{n}"
    return q


if __name__ == "__main__":
    # 自测：造 3 条含 1 重复 + 1 面积异常
    sample = [
        {"楼栋": "1", "单元": "1", "楼层": 1, "房号": "01", "面积": 100, "套内": 80, "分摊": 20, "总价": 500, "单价": 5, "状态": "可售"},
        {"楼栋": "1", "单元": "1", "楼层": 1, "房号": "01", "面积": 100, "套内": 80, "分摊": 20, "总价": 500, "单价": 5, "状态": "可售"},
        {"楼栋": "2", "单元": "1", "楼层": 2, "房号": "02", "面积": 9999, "套内": 80, "分摊": 20, "总价": 500, "单价": 5, "状态": "已售"},
    ]
    print(json.dumps(validate_houses(sample), ensure_ascii=False, indent=1))
    print(json.dumps(validate_permits([
        {"certificateNo": "A", "approvedUnits": 10, "approvedArea": 1000},
        {"certificateNo": "A", "approvedUnits": 0, "approvedArea": 0},
    ]), ensure_ascii=False, indent=1))
