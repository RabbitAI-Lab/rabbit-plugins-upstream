"""
nosec.py — 误报抑制配置（.nosec.yml 全局排除 + 行内 # nosec 约定）。

借鉴 skill-security-checker (njskills, MIT) 的 .nosec.yml 思路并适配本审计器：
在 Skill 根目录放置 .nosec.yml，可按「类别 / 文件路径 / 正则模式」批量排除已知误报，
避免在审计报告中重复出现已确认的合法命中（例如安全类 Skill 自身的检测规则、文档示例）。

注意：排除仅抑制「展示与计分」，被排除的命中仍可在 --json 完整结果中查看
（result["nosec"]["suppressed"] 字段），不降低透明度。

作者：借鉴 njskills@agent.qq.com 的 global_exclude.py（MIT），由 skill-analysis 适配。
版本：2.6.3
"""

import os
import re
from pathlib import Path


class GlobalExcludeConfig:
    """解析并应用 .nosec.yml 全局排除配置（零第三方依赖，自实现轻量 YAML 解析）。"""

    def __init__(self, skill_path=None):
        self.version = 1
        self.exclude_categories = set()
        self.exclude_files = set()
        self.exclude_patterns = []
        self._loaded = False
        if skill_path:
            self.load(skill_path)

    def load(self, skill_path):
        """从 Skill 根目录加载 .nosec.yml（若存在）。"""
        skill_path = Path(skill_path)
        config_path = skill_path / ".nosec.yml"
        if not config_path.exists():
            self._loaded = False
            return
        try:
            content = config_path.read_text(encoding="utf-8-sig")
        except Exception:
            self._loaded = False
            return

        in_exclude = False
        in_section = None
        for line in content.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if stripped.startswith("version:"):
                try:
                    self.version = int(stripped.split(":", 1)[1].strip())
                except Exception:
                    self.version = 1
                continue
            if stripped == "exclude:":
                in_exclude = True
                continue
            if not in_exclude:
                continue
            if stripped.startswith("categories:"):
                in_section = "categories"
                continue
            if stripped.startswith("files:"):
                in_section = "files"
                continue
            if stripped.startswith("patterns:"):
                in_section = "patterns"
                continue
            if stripped.startswith("- "):
                val = stripped[2:].strip().strip('"').strip("'")
                if in_section == "categories":
                    self.exclude_categories.add(val)
                elif in_section == "files":
                    self.exclude_files.add(val)
                elif in_section == "patterns":
                    self.exclude_patterns.append(val)
            elif not stripped.startswith("-"):
                in_section = None
        self._loaded = True

    def is_category_excluded(self, category):
        return bool(category) and category in self.exclude_categories

    def is_file_excluded(self, filepath):
        if not filepath:
            return False
        fp = str(filepath)
        for pattern in self.exclude_files:
            if pattern in fp:
                return True
        return False

    def is_pattern_excluded(self, text):
        if not text:
            return False
        for pat in self.exclude_patterns:
            try:
                if re.search(pat, text):
                    return True
            except re.error:
                continue
        return False

    def should_skip(self, category="", filepath="", text=""):
        """是否应跳过该命中（被全局排除配置抑制）。"""
        if not self._loaded:
            return False
        if self.is_category_excluded(category):
            return True
        if self.is_file_excluded(filepath):
            return True
        if self.is_pattern_excluded(text):
            return True
        return False

    @property
    def loaded(self):
        return self._loaded


def apply_exclusions(hits, excl, file_of=None):
    """对命中列表应用全局排除，返回 (保留命中, 被抑制命中)。

    file_of: 可选 callable(hit)->相对路径，用于文件路径级排除。
    """
    kept, suppressed = [], []
    if excl is None or not excl.loaded:
        return hits, suppressed
    for h in hits:
        cat = h.get("category", "")
        fp = (file_of(h) if file_of else h.get("file", "")) or ""
        txt = f"{h.get('label', '')} {h.get('snippet', '')}"
        if excl.should_skip(cat, fp, txt):
            suppressed.append(h)
        else:
            kept.append(h)
    return kept, suppressed
