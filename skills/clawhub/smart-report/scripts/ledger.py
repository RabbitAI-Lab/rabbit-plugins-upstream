"""事实台账公共模块。

供以下消费者共享同一份 ledger.json 加载/校验/格式化逻辑：
- report_assembler 的 HTML 组装（--ledger-mode scan|placeholder）
- docx_export 的 Word 组装
- pptx_export 的幻灯片组装
- HTML 报告附录中的"关键数据溯源"表

设计要点：
- 单一格式化函数：值 → 字符串，供占位符替换与附录表格共用，避免报告内
  外数字口径分叉。
- 占位符语法 {{id}} / {{id:fmt}>>，fmt 是合法 Python format spec（',.0f' / '.1f' / ',.1f' 等）。
- 替换器报错统一抛 LedgerError，由调用方按 5004 / 5005 错误码输出。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path


_PLACEHOLDER_RE = re.compile(
    r"\{\{\s*(?P<id>[A-Za-z_][A-Za-z0-9_]*)\s*(?::\s*(?P<fmt>[^{}]*?)\s*)?\}\}"
)

# 数字识别（Level 1 修订版）：
#   必须溯源 —— 任何小数、>=100 的整数、紧跟%/个百分点/倍 的数字
#   豁免    —— 日期（图 1）、图号（图 2）、章节引用（§1）、纯小整数（"59 名学生"）
_DATE_PATTERNS = [
    re.compile(r"\d{4}-\d{2}(-\d{2})?"),                             # 2025-01 / 2025-06-30
    re.compile(r"(?:从|至|截至|于|在|自|到|至)\s*(?:19|20)\d{2}"),       # 从 2025 / 至 2026
    re.compile(r"(?:19|20)\d{2}\s*(?:年|年度|全年|上半年|下半年|期间|以来|至今|Q[1-4])"),  # 2025 年 / 2025 全年
    re.compile(r"\d{1,2}\s*月(?![度内例])"),                             # 6 月
    re.compile(r"Q[1-4]|第?[1-4一二三四]季度"),
    re.compile(r"图\s*\d+"),
    re.compile(r"§\w+"),
]
# %/个百分点/倍 必须溯源（无论整数小数，堵漏 37%）
# 关键：分窗口检查，避免把"远处有 倍/%"误判为 %-like
#   单字符形态（%/％/倍）看紧邻 ≤ 2 字符；
#   多字符"个百分点"需 ≤ 6 字符。
_PERCENT_LIKE_TIGHT_RE = re.compile(r"[%％]|倍")          # 紧邻 2 字符
_PERCENT_LIKE_LOOSE_RE = re.compile(r"个百分点")          # 紧邻 6 字符
_NUM_RE = re.compile(r"-?\d{1,3}(?:,\d{3})+(?:\.\d+)?|-?\d+\.\d+|-?\d+")


class LedgerError(Exception):
    def __init__(self, message: str, code: int = 5004, details: dict | None = None):
        super().__init__(message)
        self.code = code
        self.code_name = "LEDGER_MISMATCH" if code == 5004 else "RAW_NUMBER_IN_PLACEHOLDER_MODE"
        self.message = message
        self.details = details or {}


@dataclass
class LedgerEntry:
    id: str
    metric: str
    value: float
    unit: str = ""
    source: str = ""
    sections: list[str] = field(default_factory=list)


@dataclass
class LedgerResolver:
    ledger_path: Path
    entries: list[LedgerEntry]
    by_id: dict[str, LedgerEntry]
    citations: dict[str, list[str]] = field(default_factory=dict)

    @classmethod
    def load(cls, path: str | Path) -> "LedgerResolver":
        p = Path(path).expanduser()
        if not p.is_file():
            raise LedgerError(
                f"ledger 文件不存在: {path}",
                code=5004,
                details={"given": str(path), "suggestion": "Step 4 应把台账落盘为 ledger.json"},
            )
        try:
            raw = json.loads(p.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            raise LedgerError(
                f"ledger 不是合法 JSON: {e}",
                code=5004,
                details={"given": str(p), "suggestion": "用 json.dumps(..., ensure_ascii=False) 生成"},
            )
        if not isinstance(raw, list) or not raw:
            raise LedgerError(
                "ledger 须为非空数组",
                code=5004,
                details={"given": str(p), "suggestion": "参考 REPORT.md 台账 schema：每项含 metric/value/source"},
            )
        entries: list[LedgerEntry] = []
        by_id: dict[str, LedgerEntry] = {}
        for i, item in enumerate(raw):
            if not isinstance(item, dict) or "value" not in item or "id" not in item:
                raise LedgerError(
                    f"ledger 第 {i} 项缺少 id/value 或不是对象",
                    code=5004,
                    details={"given": str(p)},
                )
            try:
                value = float(item["value"])
            except (TypeError, ValueError):
                raise LedgerError(
                    f"ledger 第 {i} 项 value 无法转为数字: {item['value']!r}",
                    code=5004,
                    details={"given": str(p)},
                )
            if not str(item["id"]).strip():
                raise LedgerError(f"ledger 第 {i} 项 id 为空", code=5004, details={"given": str(p)})
            eid = str(item["id"])
            if eid in by_id:
                raise LedgerError(f"ledger 存在重复 id: {eid!r}", code=5004, details={"given": str(p)})
            entry = LedgerEntry(
                id=eid,
                metric=str(item.get("metric", eid)),
                value=value,
                unit=str(item.get("unit", "")),
                source=str(item.get("source", "")),
                sections=list(item.get("sections") or []),
            )
            entries.append(entry)
            by_id[eid] = entry
        return cls(ledger_path=p, entries=entries, by_id=by_id)

    def _decimals(self, value: float) -> int:
        """源 value 的有效小数位数（基于 str 解析；整数视为 0）。"""
        s = repr(value) if isinstance(value, float) else str(value)
        if "." in s:
            return len(s.split(".")[1].rstrip("0"))
        return 0

    def _format_value(self, entry: LedgerEntry, fmt: str | None) -> str:
        val = entry.value
        if fmt is None or fmt.strip() == "":
            if isinstance(val, float) and val.is_integer():
                return str(int(val))
            return str(val)
        try:
            return format(val, fmt)
        except (ValueError, TypeError) as e:
            raise LedgerError(
                f"占位符格式说明非法: id={entry.id!r} fmt={fmt!r} → {e}",
                code=5004,
                details={"id": entry.id, "fmt": fmt, "suggestion": "fmt 是 Python format spec，如 ',.0f' / '.1f' / ',.1f'"},
            )

    def _verify_format_precision(self, entry: LedgerEntry, rendered: str, where: str) -> None:
        """format spec 不能把 value 粗化到精度以下（98.56 → .0f → 99 视为失真）。"""
        src_decimals = self._decimals(entry.value)
        cleaned = rendered.replace(",", "").replace("%", "").strip()
        try: numeric = float(cleaned)
        except ValueError:
            return  # 非纯数字占位符（如 "约 100"）放过
        rendered_decimals = 0 if "." not in cleaned else len(cleaned.split(".")[1].rstrip("0"))
        if rendered_decimals < src_decimals:
            raise LedgerError(
                f"占位符 fmt 把 {entry.id}={entry.value} 粗化为 {rendered!r}（精度下降）",
                code=5004,
                details={
                    "id": entry.id,
                    "source_decimals": src_decimals,
                    "rendered": rendered,
                    "where": where,
                    "suggestion": f"fmt 至少保留 {src_decimals} 位小数（value={entry.value}）；或更新 ledger 让 value 更粗",
                },
            )

    def resolve_text(self, text: str, where: str) -> str:
        """解析文本中的 {{id}} / {{id:fmt}} 占位符并替换；citation 入账。"""
        if not text:
            return text

        def _rep(m: re.Match) -> str:
            eid = m.group("id")
            fmt = m.group("fmt")
            if eid not in self.by_id:
                raise LedgerError(
                    f"未注册占位符: {eid!r}",
                    code=5004,
                    details={
                        "where": where,
                        "id": eid,
                        "available_ids": sorted(self.by_id),
                        "suggestion": f"把 {eid} 写入 ledger.json 或在文本中改用已注册 id",
                    },
                )
            entry = self.by_id[eid]
            try:
                rendered = self._format_value(entry, fmt)
            except LedgerError:
                raise
            self._verify_format_precision(entry, rendered, where)
            self.citations.setdefault(eid, []).append(where)
            return rendered

        return _PLACEHOLDER_RE.sub(_rep, text)

    # ---------- 占位符模式专用：发现占位符 id 与裸数字 ----------

    def placeholder_ids_in(self, text: str) -> set[str]:
        return set(m.group("id") for m in _PLACEHOLDER_RE.finditer(text or ""))

    def unresolved_placeholders(self, text: str) -> list[tuple[str, int]]:
        """返回未匹配到 ledger 的占位符列表 [(id, span_start)]，空表示全部注册。"""
        return [(m.group("id"), m.start()) for m in _PLACEHOLDER_RE.finditer(text or "")
                if m.group("id") not in self.by_id]

    # ---------- 数字扫描共用（Level 1 修订：%/个百分点/倍强制） ----------

    @staticmethod
    def strip_placeholders(text: str) -> str:
        """把 {{...}} 替换为空白占位符，便于对残留文本扫描数字。"""
        return _PLACEHOLDER_RE.sub(" ", text or "")

    @staticmethod
    def required_numbers(text: str) -> list[tuple[str, float, str]]:
        """找出必须溯源台账的数字：(display, value, context)。

        context 为前后各 ~20 字符（日期豁免后；占位符已剥离）。
        规则：任何小数 / >=100 整数 / 紧跟 %/个百分点/倍 的数字（无论大小）。
        """
        cleaned = LedgerResolver.strip_placeholders(text)
        for pat in _DATE_PATTERNS:
            cleaned = pat.sub(" ", cleaned)
        out = []
        for m in _NUM_RE.finditer(cleaned):
            display = m.group(0)
            try:
                value = float(display.replace(",", ""))
            except ValueError:
                continue
            has_decimal = "." in display
            # 紧邻窗口：单字符形态 ≤2 字符，"个百分点" ≤6 字符；避免远处命中误带
            tight_window = cleaned[m.end():m.end() + 2]
            loose_window = cleaned[m.end():m.end() + 6]
            is_percent_like = bool(_PERCENT_LIKE_TIGHT_RE.search(tight_window)) or \
                              bool(_PERCENT_LIKE_LOOSE_RE.search(loose_window))
            if not has_decimal and value < 100 and not is_percent_like:
                continue  # 裸小整数（"3 个类别" / "Top 5"）：计数语境，放行
            ctx = cleaned[max(0, m.start() - 20):m.end() + 25].replace("\n", " ").strip()
            out.append((display, value, ctx))
        return out

    # ---------- 兼容旧 API：供 scan 模式沿用 ----------

    def values_for_matching(self) -> list[float]:
        """所有 entry 的可匹配数值（兼容字符串 value "98.6%"）。"""
        vals: list[float] = []
        for e in self.entries:
            s = str(e.value)
            try:
                vals.append(float(s.replace(",", "").replace("%", "").strip()))
            except ValueError:
                pass
        return vals


def matches_any(value: float, ledger_vals: list[float]) -> bool:
    """容差匹配：用于 scan 模式兜底。"""
    decimals = len(str(value).split(".")[1]) if "." in str(value) else 0
    tol = 0.5 * (10 ** -decimals) + 1e-9
    for v in ledger_vals:
        if abs(v - value) <= tol:
            return True
        if round(v, decimals) == round(value, decimals):
            return True
    return False