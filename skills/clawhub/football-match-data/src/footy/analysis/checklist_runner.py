"""赛事数据自动化检查器 — 30维必须全过才能输出结论。

Every match analysis must pass this checklist before results are shown.
Missing dimensions are flagged and must be filled.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CheckItem:
    """One analysis step that must be completed."""

    id: str
    name: str
    status: str = "❌"  # ✅ / ❌ / ⚠️
    detail: str = ""


@dataclass
class MatchChecklist:
    """Full 30-dimension checklist for a single match."""

    match: str = ""
    items: list[CheckItem] = field(default_factory=list)

    @property
    def passed(self) -> int:
        return sum(1 for i in self.items if i.status == "✅")

    @property
    def missing(self) -> int:
        return sum(1 for i in self.items if i.status == "❌")

    @property
    def warned(self) -> int:
        return sum(1 for i in self.items if i.status == "⚠️")

    def is_ready(self) -> bool:
        return self.missing == 0

    def missing_items(self) -> list[str]:
        return [f"{i.id} {i.name}" for i in self.items if i.status == "❌"]

    def mark(self, item_id: str, detail: str = "", status: str = "✅") -> None:
        """Mark a checklist item as complete with optional detail."""
        for item in self.items:
            if item.id == item_id:
                item.status = status
                if detail:
                    item.detail = detail
                return
        # Item not found — could be a new item added after creation
        # Try flexible matching (e.g. "08a" matches "08")
        for item in self.items:
            if item.id == item_id or item.id.startswith(item_id):
                item.status = status
                if detail:
                    item.detail = detail
                return

    def mark_list(self, items: list[tuple[str, str]]) -> None:
        """Batch mark multiple items. Each tuple: (item_id, detail)."""
        for item_id, detail in items:
            self.mark(item_id, detail)


def create_checklist(match_name: str) -> MatchChecklist:
    """Create a fresh 30-dimension checklist for a match."""
    items = [
        # ---- Core odds (01-08a) ----
        CheckItem("01", "欧赔数据(≥5家)"),
        CheckItem("02", "去水(de-vig)"),
        CheckItem("03", "凯利指数"),
        CheckItem("04", "凯利方差"),
        CheckItem("05", "凯利方向"),
        CheckItem("06", "离散度"),
        CheckItem("07", "隐含概率"),
        CheckItem("08", "Steam(初盘→即时)"),
        CheckItem("08a", "亚盘数据(初盘+即时+水位)"),

        # ---- Asian handicap (09-11) ----
        CheckItem("09", "升盘降水分析"),
        CheckItem("10", "退盘升水分析"),
        CheckItem("11", "阻控诱判定"),

        # ---- O/U handicap (12-13) ----
        CheckItem("12", "大小球盘口线"),
        CheckItem("13", "大小球水位变化"),

        # ---- Cross-analysis (14-18) ----
        CheckItem("14", "欧亚偏差"),
        CheckItem("15", "赔率骨架"),
        CheckItem("16", "高级亚盘(四模)"),
        CheckItem("17", "冷门检测(9信号)"),
        CheckItem("18", "庄家意图"),

        # ---- Fundamentals (19-23) ----
        CheckItem("19", "伤停信息"),
        CheckItem("20", "阵容/首发"),
        CheckItem("21", "近期状态"),
        CheckItem("22", "出线形势"),
        CheckItem("23", "心理惯性"),

        # ---- Value & models (24-29) ----
        CheckItem("24", "CLV(收盘线价值)"),
        CheckItem("25", "初盘偏差(浅开/深开)"),
        CheckItem("26", "欧亚联动分析"),
        CheckItem("27", "返还率异常检测"),
        CheckItem("28", "泊松比分预测"),
        CheckItem("29", "EV/Edge计算"),

        # ---- Betfair (30) ----
        CheckItem("30", "必发四步验证(成交量/背离/盈亏/凯利)"),
    ]
    return MatchChecklist(match=match_name, items=items)


def print_checklist(checklist: MatchChecklist) -> None:
    """Display checklist status."""
    print(f"\n{'='*60}")
    print(f"  {checklist.match}")
    print(f"  Passed: {checklist.passed} | Missing: {checklist.missing} | Warn: {checklist.warned}")
    print(f"  READY: {'✅ YES' if checklist.is_ready() else '❌ NO — fill missing first'}")
    print(f"{'='*60}")
    if not checklist.is_ready():
        print("  MISSING:")
        for item in checklist.missing_items():
            print(f"    ❌ {item}")
    else:
        print("  ALL 30 DIMENSIONS PASSED ✅")
    print()
