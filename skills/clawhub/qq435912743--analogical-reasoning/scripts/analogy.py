#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analogical-reasoning —— 类比推理与迁移（结构保持）。

在源领域(对象+关系)与目标领域间找 1:1 结构保持映射，
把源已知关系(主-谓-宾)迁移到目标生成新推断。零依赖、可本地实跑。

--selftest 自带夹具，断言 映射正确 / 关系迁移正确 / 评分正确。
"""
import os, sys, argparse, json


def attr_sim(a, b):
    """属性相似度：类型相同给 1.0，否则按共有键比例。"""
    if a.get("type") and a["type"] == b.get("type"):
        return 1.0
    keys_a, keys_b = set(a.keys()), set(b.keys())
    if not keys_a or not keys_b:
        return 0.0
    return len(keys_a & keys_b) / len(keys_a | keys_b)


def best_mapping(src_objs, tgt_objs):
    """贪心 1:1 映射：每个源对象配最相似且未占用的目标对象。"""
    # 按相似度降序配对
    pairs = []
    for sn, so in src_objs.items():
        for tn, to in tgt_objs.items():
            pairs.append((attr_sim(so, to), sn, tn))
    pairs.sort(reverse=True)
    used_t, mapping = set(), {}
    for sim, sn, tn in pairs:
        if sn in mapping or tn in used_t:
            continue
        mapping[sn] = tn
        used_t.add(tn)
    return mapping


def transfer(src, tgt, mapping):
    """对每条源关系，若主宾均已映射则迁移谓词到目标。"""
    transferred, dangling = [], []
    for (s, p, o) in src["relations"]:
        if s in mapping and o in mapping:
            transferred.append((mapping[s], p, mapping[o]))
        else:
            dangling.append((s, p, o))
    return transferred, dangling


def score(src, transferred, mapping):
    total = len(src["relations"])
    supported = len(transferred)
    return round(supported / total, 3) if total else 0.0


def conclude(src, tgt):
    mapping = best_mapping(src["objects"], tgt["objects"])
    transferred, dangling = transfer(src, tgt, mapping)
    sc = score(src, transferred, mapping)
    return {
        "mapping": mapping,
        "transferred_relations": transferred,
        "dangling_relations": dangling,
        "transfer_score": sc,
    }


def selftest():
    print("🧪 selftest: 构造结构保持夹具（天体 ↔ 原子）...")
    src = {
        "objects": {
            "sun":    {"type": "celestial_body", "mass": "high"},
            "earth":  {"type": "planet", "mass": "mid"},
        },
        "relations": [("earth", "revolves_around", "sun")],
    }
    tgt = {
        "objects": {
            "nucleus": {"type": "celestial_body", "mass": "high"},
            "electron": {"type": "planet", "mass": "mid"},
        },
        "relations": [],
    }
    res = conclude(src, tgt)
    m = res["mapping"]
    # 断言1：类型保持映射 sun->nucleus, earth->electron
    assert m.get("sun") == "nucleus", f"sun 应映射到 nucleus，实际 {m}"
    assert m.get("earth") == "electron", f"earth 应映射到 electron，实际 {m}"
    # 断言2：关系迁移出 (electron, revolves_around, nucleus)
    assert ("electron", "revolves_around", "nucleus") in res["transferred_relations"], \
        f"应迁移出 electron revolves_around nucleus，实际 {res['transferred_relations']}"
    # 断言3：评分=1.0（1/1 源关系被支撑）
    assert res["transfer_score"] == 1.0, f"评分应=1.0，实际 {res['transfer_score']}"
    assert res["dangling_relations"] == [], "不应有悬空关系"
    print(f"  ✓ 映射正确（sun→nucleus, earth→electron）")
    print(f"  ✓ 关系迁移正确（electron revolves_around nucleus）")
    print(f"  ✓ 评分正确（transfer_score={res['transfer_score']}）")
    print("✅ selftest 全链路 PASS")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source")
    ap.add_argument("--target")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not (args.source and args.target):
        print("用法: --source src.json --target tgt.json [--selftest]")
        return None
    src = json.load(open(args.source, encoding="utf-8"))
    tgt = json.load(open(args.target, encoding="utf-8"))
    print(json.dumps(conclude(src, tgt), ensure_ascii=False, indent=2))
    return None


if __name__ == "__main__":
    main()
