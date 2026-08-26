---
name: story-engine-for-creator
slug: story-engine-for-creator
version: 2.1.0
displayName: 创作者故事因果引擎
description: 决定论剧情架构工具，内置第二视角因果推理、逻辑漏洞检测、世界观自动生成、叙事呈现层审计
required_commands:
  - python3
metadata:
  openclaw:
    required_binaries:
      - python3
    emoji: "✍️"
    homepage: "https://github.com/nohn3043-arch/story-engine"
---
# 创作者故事因果引擎
基于决定论因果推理的专业剧情创作工具，为史诗级小说、游戏剧本、影视脚本提供从大纲到完稿的全流程逻辑校验与生成支持。
## 触发场景
当用户询问以下内容时自动触发：
- 小说/剧本/游戏剧情架构设计
- 世界观设定生成与一致性校验
- 剧情逻辑漏洞检测与修复
- 角色行为一致性校验
- 多线叙事时间线对齐
- 剧情节奏优化与细节补全
## 核心能力
### 🧠 第二视角因果推理内核
- 自然语言大纲自动转可审计因果链
- 剧情逻辑漏洞自动检测与修复建议
- 角色行为一致性全链路校验
- 多线叙事时间线自动对齐
### 🌍 世界观生成与校验
- 基于规则的架空世界观自动生成
- 设定冲突自动审计
- 力量体系平衡性校验
- 历史时间线自洽性验证
### ✍️ 剧情生成与渲染
- 多语言剧情桥接与本地化
- 场景细节自动补全
- 对话风格一致性保持
- 剧情节奏自动优化
### 🎭 叙事呈现层审计（v2.1 新增）
- 史官旁观 / 禁全知：三档叙事立场校验（chronicler / limited / omniscient）
- 台词时代穿越检测：自动识别现代词穿越，支持题材豁免（都市/科幻/现代等）
- 台词认知边界审计：角色只说己知之事，禁知识泄漏
- 文体风格自动识别：题材/人称/视角/语言/节奏五维画像
### 🔒 引擎隔离防护（v2.1 新增）
- Creator 引擎与 Business 引擎命名空间隔离，防止同名数据类混用导致崩溃
- 自动检测多引擎并发加载并告警
## 使用方法
```python
# 初始化引擎
from scripts.story_engine import UltimateCausalNovelEngine, GlobalState
state = GlobalState()
engine = UltimateCausalNovelEngine("你的小说标题", state)
# 加载世界观设定
engine.conceive_world("世界观大纲文本")
# 从自然语言大纲创建章节
chapter = engine.create_chapter_from_outline(1, "章节标题", "自然语言大纲文本")
# 执行逻辑审计
audit_result = engine.audit_text("章节正文", "consistency")
print(audit_result)
# 生成章节内容
content = engine.render_chapter(chapter)
```
## v2.0 升级能力（P0-P2）

### 🔗 角色-叙事互链（P0）
与 AI 绘画构图模板共享同一 `character_id`：视觉身份（绘画模板）→ 行为身份（本引擎）→ 情绪状态（拟人引擎），三源一真。每章跑连续性清单（不可变事实逐字保留、气质一致行为、道具连续性、情绪弧线、台词风格）。见 `references/CharacterToNarrativeLink.md`。
### 🌍 世界观版本化（P0）
世界观像代码一样管理：core_rules（不可变）/derived_rules（可演化）/canon（叙事事实）三层 + 语义化版本号（major=核心规则变更 / minor=衍生规则 / patch=canon 追加）。每章生成 diff，违例规则即拒绝或显式改版。见 `references/WorldviewVersioning.md`。
### 🪟 长篇叙事窗口管理（P1）
章节门/弧门/卷门三级检查点 + 滚动摘要窗口 + 伏笔台账（承诺→兑现跟踪，>10 章未兑现告警）。第 20 章不再背叛第 1 章。见 `references/LongNarrativeWindow.md`。
### 🕵️ 逻辑漏洞检测联动（P2）
漏洞检测直接复用 NOMOS 决策中枢的五算子链做剧情因果审计——同一套决定论引擎，从决策域迁移到叙事域。

## v2.1 升级要点

- **引擎核心全面重构**：840 行 → 2800+ 行，新增第二视角因果引擎、叙事呈现层审计、文体风格识别、可视化审计报告
- **叙事呈现层审计**：史官旁观 / 禁全知、台词时代穿越、台词认知边界三大检测器
- **引擎隔离机制**：Creator / Business 双引擎命名空间隔离，混用自动告警
- **构造器变更**：`UltimateCausalNovelEngine(novel_title, initial_global_state, output_language="zh")`
- **新增 API**：`recognize_style()`、`audit_text()`、`simulate_chapter()`、`repair_presentation_issues()`

## 文件
- `references/CharacterToNarrativeLink.md`（P0 角色-叙事互链）
- `references/WorldviewVersioning.md`（P0 世界观版本化）
- `references/LongNarrativeWindow.md`（P1 长篇窗口管理）
- `scripts/`（引擎核心）

## 典型场景
1. **史诗小说创作**：百万字级长篇小说的世界观校验、剧情推演、逻辑审计
2. **游戏剧本开发**：多分支剧情的一致性校验、结局合理性推演
3. **影视脚本创作**：剧情节奏优化、人物行为逻辑校验
4. **IP衍生创作**：确保衍生内容与原作世界观、人物设定的一致性
## 技术特性
- 无概率黑盒：所有生成与校验结果均支持完整因果溯源
- 审计链上链：所有修改与决策均留痕可审计
- 纯本地运行：无需联网，所有数据仅存储在本地
- 零学习成本：支持纯自然语言输入，无需掌握专业标记语言
## 授权说明
仅允许个人非商业研究使用，商业使用需获得书面授权。
