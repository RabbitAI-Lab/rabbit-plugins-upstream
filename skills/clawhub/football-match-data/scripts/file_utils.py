"""ClawTip 订单文件读写工具 — Phase 1/3 共用."""
import json
import os
import hashlib
from pathlib import Path

SKILL_SLUG = "football-match-data"
INDICATOR = hashlib.md5(SKILL_SLUG.encode("utf-8")).hexdigest()

def order_dir() -> Path:
    """订单文件存储目录"""
    home = Path.home()
    return home / "openclaw" / "skills" / "orders" / INDICATOR

def save_order(data: dict) -> Path:
    """保存订单JSON，返回文件路径"""
    d = order_dir()
    d.mkdir(parents=True, exist_ok=True)
    order_no = data["order_no"]
    path = d / f"{order_no}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path

def load_order(order_no: str) -> dict:
    """读取订单JSON"""
    path = order_dir() / f"{order_no}.json"
    if not path.exists():
        raise FileNotFoundError(f"订单文件不存在: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def update_order(order_no: str, key: str, value) -> None:
    """更新订单JSON中的某个字段"""
    data = load_order(order_no)
    data[key] = value
    save_order(data)
