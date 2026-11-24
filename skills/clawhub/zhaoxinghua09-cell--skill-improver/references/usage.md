#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用法模板：三种典型场景各怎么做。

场景一：拿到一份评测报告，只想看能修什么
    python scripts/improve.py scan path/to/skill

场景二：确认要改，一次做到
    python scripts/improve.py apply path/to/skill --siblings a,b,c

场景三：有阻断项「声明了未实现的参数」，且你决定先撤掉示例
    python scripts/improve.py apply path/to/skill --fix-doc-drift
"""

SCENE_1 = """\
$ python scripts/improve.py scan ./my-skill
基线：结构制 46/100 BLOCK
整改项 9 条

可自动补（4）：
  - licensing:no-license            无独立许可文件（仅 frontmatter 声明）
  - discoverable:no-ai-index        未提供 ai-index.json
  - discoverable:no-tags            标签 0 个，建议 ≥3
  - discoverable:no-triggers        缺触发词段（AI 检索主要靠它）
必须人工（5）：
  - block:declared_command_missing  SKILL.md:18 声明了未实现的参数
  - reproducible:no-golden          无测试用例文件
  - reproducible:no-runner          无测试执行器
  - hygiene:no-boundary             未声明安全边界
  - discoverable:no-links           缺互链段

（当前是 scan，未改动任何文件；执行改造请用 apply）
"""

SCENE_2 = """\
$ python scripts/improve.py apply ./my-skill --siblings lgd-skill-review
执行改造：
  ✓ 写入 LICENSE（MIT，作者取自 frontmatter 的 author）
  ✓ 生成 ai-index.json（8 条 intents，已标注待校订）
  ✓ 补 tags（my-skill, review, remediation）
  ✓ 追加 Triggers 段（5 条，取自 description）
  ✓ 追加 Related skills 段（1 个，含「同系列」标识）

复测：结构制 46/100 BLOCK  →  67/100 WARN   (+21)

仍必须人工的 4 项未动——自动改造只补元信息，不伪造能力。
"""

if __name__ == "__main__":
    print(SCENE_1)
    print(SCENE_2)
