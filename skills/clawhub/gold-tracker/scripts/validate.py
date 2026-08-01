#!/usr/bin/env python3
"""
黄金追踪 - 项目验证器
检查数据完整性、格式一致性和常见问题。
零第三方依赖。

校验内容:
  - state.json 字段、价格范围、change_pct 类型
  - logs/*.yaml + archive/**/*.yaml: 用 YAML 子集解析器做结构校验
    * run_id / price_usd 必须存在
    * impact 必须在允许枚举内（违反则 error，不再是 warning）
    * sources 中的 URL 必须是合法 http(s) URL
    * key_factors 每条必须有 factor / impact / reasoning
  - alerts/*.json: alert_id 唯一、状态合法、字段齐全
  - archive: 文件命名、多 run 拆分
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent

errors = []
warnings = []


def err(msg):
    errors.append(msg)
    print(f"[错误] {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"[警告] {msg}")


# ---------- 配置加载 ----------
ALLOWED_IMPACTS = {"bullish", "bearish", "mixed", "neutral",
                   "slightly_bullish", "slightly_bearish"}


def load_allowed_impacts() -> set:
    """从 config.yaml 读取 output.constraints.allowed_impacts。失败回退默认。"""
    cfg = ROOT / "config.yaml"
    if not cfg.exists():
        return ALLOWED_IMPACTS
    text = cfg.read_text(encoding="utf-8")
    m = re.search(r'allowed_impacts:\s*\n((?:\s*-\s*.+\n)+)', text)
    if not m:
        return ALLOWED_IMPACTS
    out = set()
    for line in m.group(1).splitlines():
        mm = re.match(r'\s*-\s*"?([^"\n]+)"?\s*$', line)
        if mm:
            out.add(mm.group(1).strip())
    return out if out else ALLOWED_IMPACTS


# ---------- YAML 子集解析（与 check_analysis.py 一致） ----------
def _indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _parse_scalar(s: str):
    s = s.strip()
    if not s:
        return ""
    if len(s) >= 2 and s[0] in '"\'' and s[-1] == s[0]:
        return s[1:-1]
    if s == "[]":
        return []
    if s in ("null", "~", "None"):
        return None
    try:
        if "." in s:
            return float(s)
        return int(s)
    except ValueError:
        return s


def _parse_block(lines: list, indent: int) -> tuple:
    i = 0
    while i < len(lines):
        s = lines[i].lstrip(" ")
        if s and not s.startswith("#"):
            break
        i += 1
    if i >= len(lines):
        return None, len(lines)

    first = lines[i]
    first_indent = _indent_of(first)
    if first_indent < indent:
        return None, i

    first_s = first.lstrip(" ")

    # list
    if first_s.startswith("- "):
        items = []
        cur = i
        while cur < len(lines):
            ln = lines[cur]
            s = ln.lstrip(" ")
            if not s or s.startswith("#"):
                cur += 1
                continue
            ind = _indent_of(ln)
            if ind < first_indent:
                break
            if ind > first_indent:
                cur += 1
                continue
            if not s.startswith("- "):
                break
            item_text = s[2:].strip()
            item_indent = first_indent + 2
            is_quoted_scalar = (
                len(item_text) >= 2
                and item_text[0] in '"\''
                and item_text[-1] == item_text[0]
            )
            if is_quoted_scalar:
                items.append(_parse_scalar(item_text))
                cur += 1
                continue
            if item_text and ":" in item_text and not item_text.startswith(("http://", "https://")):
                ik, _, iv = item_text.partition(":")
                item_dict = {ik.strip(): _parse_scalar(iv)}
                cur += 1
                sub_lines = []
                while cur < len(lines):
                    ln2 = lines[cur]
                    s2 = ln2.lstrip(" ")
                    if not s2 or s2.startswith("#"):
                        cur += 1
                        continue
                    ind2 = _indent_of(ln2)
                    if ind2 <= first_indent:
                        break
                    sub_lines.append(ln2)
                    cur += 1
                j = 0
                while j < len(sub_lines):
                    ln2 = sub_lines[j]
                    s2 = ln2.lstrip(" ")
                    ind2 = _indent_of(ln2)
                    if not s2 or s2.startswith("#"):
                        j += 1
                        continue
                    if ind2 == item_indent and ":" in s2 and not s2.startswith("- "):
                        sk, _, sv = s2.partition(":")
                        sv = sv.strip()
                        if sv:
                            item_dict[sk.strip()] = _parse_scalar(sv)
                            j += 1
                        else:
                            j += 1
                            nested = []
                            while j < len(sub_lines):
                                ln3 = sub_lines[j]
                                s3 = ln3.lstrip(" ")
                                if not s3 or s3.startswith("#"):
                                    j += 1
                                    continue
                                if _indent_of(ln3) <= item_indent:
                                    break
                                nested.append(ln3)
                                j += 1
                            nested_val, _ = _parse_block(nested, item_indent + 1)
                            item_dict[sk.strip()] = nested_val
                    else:
                        j += 1
                items.append(item_dict)
            elif item_text:
                items.append(_parse_scalar(item_text))
                cur += 1
            else:
                cur += 1
                nested = []
                while cur < len(lines):
                    ln2 = lines[cur]
                    s2 = ln2.lstrip(" ")
                    if not s2 or s2.startswith("#"):
                        cur += 1
                        continue
                    if _indent_of(ln2) <= first_indent:
                        break
                    nested.append(ln2)
                    cur += 1
                nested_val, _ = _parse_block(nested, first_indent + 2)
                items.append(nested_val)
        return items, cur

    # dict
    if ":" in first_s:
        d = {}
        cur = i
        while cur < len(lines):
            ln = lines[cur]
            s = ln.lstrip(" ")
            if not s or s.startswith("#"):
                cur += 1
                continue
            ind = _indent_of(ln)
            if ind < first_indent:
                break
            if ind > first_indent:
                cur += 1
                continue
            if not ":" in s or s.startswith("- "):
                break
            sk, _, sv = s.partition(":")
            sv = sv.strip()
            if sv:
                d[sk.strip()] = _parse_scalar(sv)
                cur += 1
            else:
                cur += 1
                nested = []
                while cur < len(lines):
                    ln2 = lines[cur]
                    s2 = ln2.lstrip(" ")
                    if not s2 or s2.startswith("#"):
                        cur += 1
                        continue
                    if _indent_of(ln2) <= first_indent:
                        break
                    nested.append(ln2)
                    cur += 1
                nested_val, _ = _parse_block(nested, first_indent + 1)
                d[sk.strip()] = nested_val
        return d, cur

    return _parse_scalar(first_s), i + 1


def parse_yaml(text: str) -> dict:
    """解析 YAML 文本（多文档取最后一份）。"""
    text = text.lstrip("\n")
    if text.startswith("---"):
        text = text[3:]
        if text.startswith("\n"):
            text = text[1:]
    docs = [d for d in text.split("\n---") if d.strip()]
    if docs:
        text = docs[-1]
    val, _ = _parse_block(text.splitlines(), 0)
    return val if isinstance(val, dict) else {}


# ---------- 校验逻辑 ----------
def is_valid_url(u) -> bool:
    if not isinstance(u, str) or not u:
        return False
    try:
        p = urlparse(u)
        return p.scheme in ("http", "https") and bool(p.netloc)
    except Exception:
        return False


def check_state():
    f = ROOT / "state.json"
    if not f.exists():
        err("state.json 不存在")
        return
    try:
        data = json.loads(f.read_text())
    except Exception as e:
        err(f"state.json JSON 格式错误: {e}")
        return

    for field in ["date", "current_price", "last_update"]:
        if field not in data:
            err(f"state.json 缺少字段: {field}")

    price = data.get("current_price")
    if price is not None and isinstance(price, (int, float)):
        if not (1000 <= price <= 10000):
            err(f"state.json 金价超出合理范围: ${price}")
    elif price is not None:
        err(f"state.json current_price 不是数字: {type(price).__name__}")

    if isinstance(data.get("change_pct"), str):
        err("state.json change_pct 是字符串，应为数字")


def check_log_file(f: Path, allowed_impacts: set):
    """对单个 YAML 日志文件做结构校验。多文档则逐文档校验。"""
    text = f.read_text(encoding="utf-8")
    rel = f.relative_to(ROOT)

    # 多文档：切分后逐个校验
    norm = text.lstrip("\n")
    if norm.startswith("---"):
        norm = norm[3:].lstrip("\n")
    docs = [d for d in norm.split("\n---") if d.strip()]

    if not docs:
        err(f"{rel}: 空文件")
        return

    for doc_idx, doc_text in enumerate(docs):
        try:
            doc = parse_yaml(doc_text)
        except Exception as e:
            err(f"{rel} doc#{doc_idx}: YAML 解析失败: {e}")
            continue

        if not doc:
            err(f"{rel} doc#{doc_idx}: 解析结果为空")
            continue

        prefix = f"{rel} doc#{doc_idx}"

        # run_id
        if not doc.get("run_id"):
            err(f"{prefix}: 缺少 run_id")

        # price_usd — 顶层或 price_data.gold.price_usd
        price_usd = None
        if "price_data" in doc and isinstance(doc["price_data"], dict):
            gold = doc["price_data"].get("gold")
            if isinstance(gold, dict):
                price_usd = gold.get("price_usd")
        if price_usd is None and "price_usd" in doc:
            price_usd = doc["price_usd"]
        if price_usd is None:
            err(f"{prefix}: 缺少 price_usd")

        # timestamp 时区
        ts = doc.get("timestamp")
        if isinstance(ts, str):
            if "+08:00" not in ts and "Z" not in ts:
                warn(f"{prefix}: 时间戳可能缺少时区: {ts}")

        # key_factors impact 枚举校验
        factors = doc.get("key_factors")
        if isinstance(factors, list):
            for idx, fac in enumerate(factors):
                if not isinstance(fac, dict):
                    err(f"{prefix}: key_factors[{idx}] 不是 dict")
                    continue
                fp = f"{prefix}: key_factors[{idx}]"
                for field in ["factor", "impact", "reasoning"]:
                    if field not in fac:
                        err(f"{fp}: 缺少字段 {field}")
                impact = fac.get("impact")
                if impact and impact not in allowed_impacts:
                    err(f"{fp}: impact='{impact}' 不在允许枚举内")

        # sources URL 格式
        sources = doc.get("sources")
        if isinstance(sources, list):
            for s in sources:
                if not is_valid_url(s):
                    err(f"{prefix}: 非法 source URL: {s!r}")


def check_logs():
    allowed = load_allowed_impacts()
    for d_name in ["logs", "archive"]:
        d = ROOT / d_name
        if not d.exists():
            if d_name == "logs":
                warn("logs/ 目录不存在（新安装时正常）")
            continue
        files = sorted(set(d.rglob("*.yaml")) | set(d.rglob("*.yml")))
        for f in files:
            if f.name.endswith(".bak"):
                continue
            check_log_file(f, allowed)


def check_alerts():
    d = ROOT / "alerts"
    if not d.exists():
        return

    for f in sorted(d.iterdir()):
        if f.suffix not in (".md", ".json"):
            continue

        if f.suffix == ".md":
            text = f.read_text(encoding="utf-8")
            timestamps = re.findall(r'##\s*\[(\d{2}:\d{2})\]', text)
            seen = set()
            for ts in timestamps:
                if ts in seen:
                    err(f"{f.name}: 存在重复提醒 [{ts}]")
                seen.add(ts)

        if f.suffix == ".json":
            try:
                data = json.loads(f.read_text())
                if not isinstance(data, list):
                    err(f"{f.name}: JSON 格式错误，应为数组")
                    continue

                seen_ids = set()
                for alert in data:
                    alert_id = alert.get("alert_id")
                    if alert_id:
                        if alert_id in seen_ids:
                            err(f"{f.name}: 存在重复 alert_id: {alert_id}")
                        seen_ids.add(alert_id)

                    required_fields = ["alert_id", "type", "price", "change_pct",
                                       "threshold_pct", "benchmark", "message",
                                       "status", "created_at"]
                    for field in required_fields:
                        if field not in alert:
                            warn(f"{f.name}: 缺少字段: {field}")

                    status = alert.get("status")
                    if status and status not in ["pending", "sent", "acknowledged",
                                                  "resolved", "dismissed"]:
                        warn(f"{f.name}: 无效状态: {status}")

            except Exception as e:
                err(f"{f.name}: JSON 解析错误: {e}")


def check_archive():
    d = ROOT / "archive"
    if not d.exists():
        return

    for month in sorted(d.iterdir()):
        if not month.is_dir():
            continue
        for f in sorted(month.iterdir()):
            if f.suffix not in (".yaml", ".yml"):
                continue
            text = f.read_text(encoding="utf-8")
            runs = [r for r in text.split("---") if r.strip()]
            if len(runs) > 1:
                warn(f"{month.name}/{f.name}: 包含 {len(runs)} 个 run（建议拆分）")


def main():
    print("=" * 56)
    print("黄金追踪项目验证器")
    print("=" * 56)

    check_state()
    check_logs()
    check_alerts()
    check_archive()

    print()
    print("=" * 56)
    print(f"结果: {len(errors)} 个错误, {len(warnings)} 个警告")
    print("=" * 56)

    if errors:
        sys.exit(1)
    print("[通过] 所有关键检查通过")


if __name__ == "__main__":
    main()
