#!/usr/bin/env python3
"""Skill 包结构与入口链接的轻量回归测试。"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


class SkillPackageTests(unittest.TestCase):
    def test_required_metadata_is_present(self) -> None:
        content = SKILL.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\n"))
        frontmatter = content.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name:\s*project-engineering\s*$")
        self.assertRegex(frontmatter, r"(?m)^description:\s*\S.+$")
        self.assertRegex(frontmatter, r"(?m)^license:\s*MIT-0\s*$")

    def test_skill_reference_links_resolve(self) -> None:
        content = SKILL.read_text(encoding="utf-8")
        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", content)
        relative_links = [link for link in links if "://" not in link and not link.startswith("#")]
        self.assertTrue(relative_links)
        for link in relative_links:
            with self.subTest(link=link):
                self.assertTrue((ROOT / link).is_file(), f"缺少引用文件：{link}")


if __name__ == "__main__":
    unittest.main()
