# -*- coding: utf-8 -*-
"""
scripts/integrations/run_pipeline.py
A 方案编排：按 config 选择数据源（mock/pgy/juguang/thirdparty），
对「关键词 × 排序」摘取并归一化为与采集器(B)同构的 CSV/MD，供 xhs-track-analysis Skill 消费。

用法:
  cd scripts/integrations
  python3 run_pipeline.py config.example.json
"""
import sys
import json
import os
import importlib

import source_base
from normalizer import save
from mock import MockAdapter
from pgy import PgyAdapter
from juguang import JuguangAdapter
from thirdparty import ThirdPartyAdapter

ADAPTERS = {
    "mock": MockAdapter,
    "pgy": PgyAdapter,
    "juguang": JuguangAdapter,
    "thirdparty": ThirdPartyAdapter,
}


def build_adapter(name, config):
    if name not in ADAPTERS:
        raise ValueError(f"未知 source：{name}。可选：{list(ADAPTERS)}")
    return ADAPTERS[name](config)


def main():
    if len(sys.argv) < 2:
        sys.exit("用法: python3 run_pipeline.py <config.json>")
    with open(sys.argv[1], encoding="utf-8") as f:
        cfg = json.load(f)

    source = cfg.get("source", "mock")
    keywords = cfg.get("keywords", [])
    sorts = cfg.get("sorts", ["综合", "最新", "最多点赞", "最多收藏", "最多评论"])
    limit = int(cfg.get("limit_per_query", 20))
    out_dir = cfg.get("output_dir", "output")

    print(f"[A方案] 数据源={source}")
    adapter = build_adapter(source, cfg)
    adapter.authenticate()

    all_records = []
    for kw in keywords:
        for s in sorts:
            try:
                recs = adapter.search_notes(kw, s, limit)
                all_records.extend(recs)
                print(f"  [{source}] {kw}/{s} → {len(recs)} 条")
            except NotImplementedError as e:
                print(f"  [骨架] {kw}/{s} 未实现：{e}")
            except Exception as e:
                print(f"  [错误] {kw}/{s}：{e}")

    if not all_records:
        print("[A方案] 无数据（骨架未实现或配置缺凭证）。可用 source=mock 跑通演示。")
        return

    csv_path, md_path = save(all_records, out_dir)
    print(f"[输出] {csv_path}\n[输出] {md_path}")


if __name__ == "__main__":
    main()
