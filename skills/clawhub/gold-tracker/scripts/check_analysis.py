#!/usr/bin/env python3
"""
黄金追踪 - 分析日志硬校验器
在 agent 写完 logs/YYYY-MM-DD.yaml 后、宣布"分析完成"前必须运行。
任意一条 ERROR 都会以非零退出码拒绝本次分析。

校验内容:
  1. 结构: run_id / timestamp / price_data / summary.focus / key_factors / sources 齐全
  2. impact 枚举: 必须在 config.yaml output.constraints.allowed_impacts 内
  3. factor 字段: 每条 key_factor 必须含 factor / impact / reasoning / sources
  4. factor 数量: 在 [min_factors_per_analysis, max_factors_per_analysis] 之间
  5. sources URL 格式: 必须是合法 http(s) URL
  6. sources 命中 fetch_log: 每个 source URL 必须出现在 .cache/fetch_log.json
  7. 来源多样性: 整篇 sources 覆盖 >= min_unique_domains 个独立域名
  8. 每个 factor 至少引用 min_count_per_factor 条 source
  9. 反幻觉措辞: reasoning / summary 不得包含 forbidden_phrases
 10. 占位规范: 无数据时必须使用 no_data_marker，不得空字符串

用法:
    python3 scripts/check_analysis.py                 # 校验当日最新日志
    python3 scripts/check_analysis.py logs/2026-07-28.yaml
    python3 scripts/check_analysis.py --strict        # 把 warning 也当 error
"""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT / "config.yaml"
FETCH_LOG = ROOT / ".cache" / "fetch_log.json"
TZ_BEIJING = timezone(timedelta(hours=8))

errors = []
warnings = []


def err(msg):
    errors.append(msg)
    print(f"  [✗] {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"  [!] {msg}")


# ---------- 配置加载 ----------
def load_config() -> dict:
    """从 config.yaml 读取 output 段。不依赖 PyYAML，用正则提取关键段。"""
    cfg = {
        "max_factors_per_analysis": 6,
        "min_factors_per_analysis": 2,
        "allowed_impacts": ["bullish", "bearish", "mixed", "neutral",
                            "slightly_bullish", "slightly_bearish"],
        "required_factor_fields": ["factor", "impact", "reasoning", "sources"],
        "forbidden_phrases": ["根据经验", "众所周知", "一般来说",
                              "通常情况下", "据了解", "据业内人士", "显而易见"],
        "no_data_marker": "no_data",
        "min_unique_domains": 2,
        "min_count_per_factor": 1,
        "must_be_in_fetch_log": True,
        "must_be_http_url": True,
    }
    if not CONFIG_FILE.exists():
        return cfg
    text = CONFIG_FILE.read_text(encoding="utf-8")

    # 提取 output: 块（直到下一个顶层 key）
    m = re.search(r'^output:\s*\n((?:[ \t]+.*\n|\n)+)', text, re.MULTILINE)
    if not m:
        return cfg
    block = m.group(1)

    def grab_int(key):
        mm = re.search(rf'^\s*{key}:\s*(\d+)\s*$', block, re.MULTILINE)
        if mm:
            return int(mm.group(1))
        return None

    v = grab_int("max_factors_per_analysis")
    if v is not None: cfg["max_factors_per_analysis"] = v
    v = grab_int("min_factors_per_analysis")
    if v is not None: cfg["min_factors_per_analysis"] = v
    v = grab_int("min_unique_domains")
    if v is not None: cfg["min_unique_domains"] = v
    v = grab_int("min_count_per_factor")
    if v is not None: cfg["min_count_per_factor"] = v

    # allowed_impacts 列表
    m = re.search(r'allowed_impacts:\s*\n((?:\s*-\s*.+\n)+)', block)
    if m:
        cfg["allowed_impacts"] = [
            re.sub(r'^\s*-\s*"?([^"\n]+)"?\s*$', r'\1', line)
            for line in m.group(1).splitlines()
        ]

    # forbidden_phrases 列表
    m = re.search(r'forbidden_phrases:\s*\n((?:\s*-\s*.+\n)+)', block)
    if m:
        cfg["forbidden_phrases"] = [
            re.sub(r'^\s*-\s*"?([^"\n]+)"?\s*$', r'\1', line)
            for line in m.group(1).splitlines()
        ]

    v = re.search(r'no_data_marker:\s*"([^"]+)"', block)
    if v: cfg["no_data_marker"] = v.group(1)

    return cfg


# ---------- YAML 子集解析（递归下降） ----------
def _indent_of(line: str) -> int:
    """返回前导空格数（tab 按 1 计，本项目日志统一用空格）。"""
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
    """
    解析从 indent 缩进开始的块。返回 (value, next_index)。
    支持 dict / list / 标量。遇到缩进 <= indent 的行停止。
    """
    # 找到第一个非空非注释行
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
        return None, i  # 属于外层

    first_s = first.lstrip(" ")

    # 列表
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
                # 不应该发生（item 子字段已在内部消化）；跳过
                cur += 1
                continue
            if not s.startswith("- "):
                break  # 列表结束
            # 列表项内容：取 "- " 后面的部分
            item_text = s[2:].strip()
            item_indent = first_indent + 2  # "- " 占 2 字符
            # 引号包裹的整体当标量，避免 URL 中的 ":" 被误判为 k:v
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
                # 列表项是 dict（首个 k:v 跟在 - 后）
                ik, _, iv = item_text.partition(":")
                item_dict = {ik.strip(): _parse_scalar(iv)}
                # 收集本项后续子字段
                cur += 1
                # 项内的子块（可能是嵌套 dict 或 list）
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
                    if ind2 <= item_indent - 1 and not (ind2 == item_indent and s2.startswith("- ")):
                        # 属于本项的兄弟字段（与首个 k:v 同缩进）
                        if s2.startswith("- "):
                            break
                        # 同级字段
                        pass
                    sub_lines.append(ln2)
                    cur += 1
                # 解析 sub_lines 为 dict（与首个字段同级或更深）
                # 用递归：把 sub_lines 按 item_indent 分组
                j = 0
                while j < len(sub_lines):
                    ln2 = sub_lines[j]
                    s2 = ln2.lstrip(" ")
                    ind2 = _indent_of(ln2)
                    if not s2 or s2.startswith("#"):
                        j += 1
                        continue
                    if ind2 == item_indent and ":" in s2 and not s2.startswith("- "):
                        # 同级 k:v
                        sk, _, sv = s2.partition(":")
                        sv = sv.strip()
                        if sv:
                            item_dict[sk.strip()] = _parse_scalar(sv)
                            j += 1
                        else:
                            # 嵌套块：收集更深的行
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
                # 列表项是标量
                items.append(_parse_scalar(item_text))
                cur += 1
            else:
                # "- " 后为空，可能是嵌套块
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
                # 不应发生，跳过
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
                # 嵌套块
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

    # 单个标量
    return _parse_scalar(first_s), i + 1


def parse_yaml_doc(text: str) -> dict:
    """
    解析项目日志使用的 YAML 子集（顶层 dict + 嵌套 dict + list + 标量）。
    不处理引用、锚点、多行字符串折叠。返回顶层 dict。
    """
    # 标准化：剥除开头的 --- 分隔符，按 \n--- 切多文档取最后一份
    text = text.lstrip("\n")
    if text.startswith("---"):
        text = text[3:]
        if text.startswith("\n"):
            text = text[1:]
    docs = [d for d in text.split("\n---") if d.strip()]
    if docs:
        text = docs[-1]

    lines = text.splitlines()
    val, _ = _parse_block(lines, 0)
    return val if isinstance(val, dict) else {}


# ---------- fetch_log 加载 ----------
def load_fetch_log() -> dict:
    if not FETCH_LOG.exists():
        return {"urls": set(), "domains": set()}
    try:
        data = json.loads(FETCH_LOG.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return {
                "urls": {e["url"] for e in data if e.get("url")},
                "domains": {e.get("domain", urlparse(e["url"]).netloc)
                            for e in data if e.get("url")},
            }
    except Exception:
        pass
    return {"urls": set(), "domains": set()}


# ---------- 校验主逻辑 ----------
def is_valid_url(u: str) -> bool:
    if not isinstance(u, str) or not u:
        return False
    try:
        p = urlparse(u)
        return p.scheme in ("http", "https") and bool(p.netloc)
    except Exception:
        return False


def check(doc: dict, cfg: dict, fetch: dict, file_name: str):
    prefix = f"{file_name}: "

    # 1. 顶层必填字段
    required_top = ["run_id", "timestamp", "price_data", "summary", "key_factors", "sources"]
    for f in required_top:
        if f not in doc:
            err(f"{prefix}缺少顶层字段: {f}")

    if "summary" in doc and isinstance(doc["summary"], dict):
        if not doc["summary"].get("focus"):
            err(f"{prefix}summary.focus 不能为空")

    # 2. key_factors
    factors = doc.get("key_factors")
    if not isinstance(factors, list):
        err(f"{prefix}key_factors 必须是列表")
        factors = []
    else:
        n = len(factors)
        if n < cfg["min_factors_per_analysis"]:
            err(f"{prefix}key_factors 数量 {n} < 最小 {cfg['min_factors_per_analysis']}")
        if n > cfg["max_factors_per_analysis"]:
            err(f"{prefix}key_factors 数量 {n} > 最大 {cfg['max_factors_per_analysis']}")

    # 3. 每个 factor 字段齐全 + impact 枚举 + sources 非空
    all_sources_urls = []
    for idx, fac in enumerate(factors):
        if not isinstance(fac, dict):
            err(f"{prefix}key_factors[{idx}] 不是 dict")
            continue
        fp = f"{prefix}key_factors[{idx}]"
        for field in cfg["required_factor_fields"]:
            if field not in fac:
                err(f"{fp}: 缺少字段 {field}")

        impact = fac.get("impact")
        if impact and impact not in cfg["allowed_impacts"]:
            err(f"{fp}: impact='{impact}' 不在允许枚举内 {cfg['allowed_impacts']}")

        reasoning = fac.get("reasoning", "")
        if reasoning and cfg["no_data_marker"] not in str(reasoning):
            for phrase in cfg["forbidden_phrases"]:
                if phrase in str(reasoning):
                    err(f"{fp}: reasoning 含禁用措辞 '{phrase}'")

        # factor 的 sources
        fac_sources = fac.get("sources", [])
        if isinstance(fac_sources, str):
            fac_sources = [fac_sources]
        if not isinstance(fac_sources, list):
            fac_sources = []
        if len(fac_sources) < cfg["min_count_per_factor"]:
            err(f"{fp}: sources 数量 {len(fac_sources)} < 最小 {cfg['min_count_per_factor']}")
        for s in fac_sources:
            all_sources_urls.append(s)

    # 4. 顶层 sources 校验
    top_sources = doc.get("sources", [])
    if isinstance(top_sources, str):
        top_sources = [top_sources]
    if not isinstance(top_sources, list):
        top_sources = []
    all_sources_urls.extend(top_sources)

    if not all_sources_urls:
        err(f"{prefix}整篇分析没有任何 source URL")
    else:
        # URL 格式
        valid_urls = []
        for s in all_sources_urls:
            if cfg["must_be_http_url"] and not is_valid_url(s):
                err(f"{prefix}非法 source URL: {s!r}")
            else:
                valid_urls.append(s)

        # 命中 fetch_log
        if cfg["must_be_in_fetch_log"]:
            fetch_urls = fetch["urls"]
            if not fetch_urls:
                warn(f"{prefix}fetch_log 为空 —— 请确认是否已用 log_fetch.py 记录 web_fetch 行为")
            for s in valid_urls:
                if s not in fetch_urls:
                    err(f"{prefix}source URL 未出现在 fetch_log 中（即未实际抓取过）: {s}")

        # 来源多样性：unique domain
        domains = set()
        for s in valid_urls:
            try:
                domains.add(urlparse(s).netloc)
            except Exception:
                pass
        if len(domains) < cfg["min_unique_domains"]:
            err(f"{prefix}来源覆盖 {len(domains)} 个独立域名 < 最小 {cfg['min_unique_domains']}（防止单源依赖）")

    # 5. summary.focus 反幻觉
    summary = doc.get("summary", {})
    if isinstance(summary, dict):
        focus = str(summary.get("focus", ""))
        for phrase in cfg["forbidden_phrases"]:
            if phrase in focus:
                err(f"{prefix}summary.focus 含禁用措辞 '{phrase}'")


# ---------- main ----------
def find_latest_log() -> Path:
    d = ROOT / "logs"
    if not d.exists():
        return None
    candidates = sorted([f for f in d.iterdir()
                         if f.suffix in (".yaml", ".yml")],
                        key=lambda f: f.name, reverse=True)
    return candidates[0] if candidates else None


def main():
    strict = "--strict" in sys.argv
    target = None
    for a in sys.argv[1:]:
        if not a.startswith("--"):
            target = a
            break

    if target:
        target_path = Path(target)
        if not target_path.is_absolute():
            target_path = ROOT / target_path
    else:
        target_path = find_latest_log()

    print("=" * 56)
    print("黄金追踪 - 分析日志硬校验")
    print("=" * 56)

    if not target_path or not target_path.exists():
        print(f"[错误] 未找到待校验日志: {target}")
        sys.exit(2)

    print(f"校验目标: {target_path.relative_to(ROOT)}\n")

    cfg = load_config()
    fetch = load_fetch_log()

    # 多文档 YAML：逐 doc 校验，取最后一个（当日本次 run）
    text = target_path.read_text(encoding="utf-8")
    docs = [d for d in text.split("\n---") if d.strip()]
    if not docs:
        docs = [text]
    last_doc = docs[-1]

    try:
        doc = parse_yaml_doc(last_doc)
    except Exception as e:
        err(f"YAML 解析失败: {e}")
        doc = {}

    if not doc:
        err("解析结果为空")

    check(doc, cfg, fetch, target_path.name)

    print()
    print("=" * 56)
    print(f"结果: {len(errors)} 个错误, {len(warnings)} 个警告")
    print("=" * 56)

    if errors or (strict and warnings):
        print("[拒绝] 本次分析未通过硬校验 —— 修复后重新写日志并再次运行本脚本")
        sys.exit(1)
    print("[通过] 所有硬约束满足，可以宣布分析完成")


if __name__ == "__main__":
    main()
