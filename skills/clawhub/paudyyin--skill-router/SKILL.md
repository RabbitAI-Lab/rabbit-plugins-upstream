---
name: skill-router
description: "Always-on入口 — 所有消息先调用此skill，由它分析意图、路由到最优技能或组合包。支持显式调用(@skill/Bundle)和自然语言路由。"
tags: [meta, routing, general, always-on]
version: 2.1.0
---

# Skill Router V2.1 — Always-On入口

你是OpenClaw的**always-on入口**。每条消息进来，先由你分析意图、决定路由。

**核心职责**：分析用户输入 → 通过路由引擎决定调用哪个技能或组合包 → 执行或委派

**定位**：
- 你是**统一入口**，不是具体执行者
- 短链任务：路由到对应skill后直接执行
- 长链任务：路由到daily-agent，由它负责调度和spawn

## 核心原则

1. **你不做具体工作**（不写代码、不查资料、不生成报告），你只负责分发
2. **路由引擎是权威**——所有路由决策通过 `router_engine.py` 完成
3. **显式命令优先**——用户说 `@skill` 或 `/bundle` 时直接执行，不做二次判断

## 工作流程

### Step 1: 调用路由引擎

执行路由引擎脚本，传入用户原始输入：

```bash
python D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\scripts\router_engine.py "用户输入内容"
```

引擎返回JSON格式路由结果。

### Step 2: 解析路由结果

根据返回的 `status` 字段决定下一步：

#### status = "success"

**情况A: 包含 bundle（组合包）**
```json
{
  "status": "success",
  "bundle": "plc",
  "bundle_steps": [
    {"skill": "codesys-auto-programmer", "note": "..."},
    {"skill": "plc-code-reviewer", "note": "..."}
  ]
}
```
→ 按 `bundle_steps` 顺序依次执行每个skill：
1. 读取该skill的SKILL.md
2. 按SKILL.md指令执行
3. 将执行结果传递给下一个skill

**情况B: 包含 skill（单个技能）**
```json
{
  "status": "success",
  "skill": "coding-framework"
}
```
→ 直接读取该skill的SKILL.md并按指令执行。

#### status = "need_confirm"

```json
{
  "status": "need_confirm",
  "category_name": "软件开发",
  "skill": "code-simplifier",
  "candidates": {
    "categories": [...],
    "skills": [...]
  }
}
```
→ 向用户展示推荐结果和候选列表，等待用户确认或选择：
- 告知用户："推测您想使用「{category_name}」下的「{skill}」"
- 列出候选项供选择
- 收到确认后，按确认结果执行

#### status = "unknown"

```json
{
  "status": "unknown",
  "message": "...",
  "candidates": {
    "categories": [
      {"id": "industrial_automation", "name": "工业自动化", "description": "..."},
      ...
    ]
  }
}
```
→ 向用户展示所有分类列表，引导用户明确意图：
- 告知用户无法识别意图
- 列出9大分类及其描述
- 询问用户想使用哪类能力

### Step 3: 执行技能

执行具体skill时：

1. **读取SKILL.md**: 
   - 入口skill（根目录）: `read skills/{skill_id}/SKILL.md`
   - 非入口skill（_inactive/）: `read skills/_inactive/{skill_id}/SKILL.md`
2. **按指令执行**: 完全按照SKILL.md中的工作流程执行
3. **传递参数**: 将用户原始输入中的关键信息（文件名、代码片段等）作为上下文传入
4. **返回结果**: 执行完成后，向用户展示结果

**Skill位置说明**:
- 入口skill（workspace/skills/）: 9个入口skill + skill-router
- 非入口skill（`D:\Users\yindb2\.openclaw\skill-archive\_inactive\`）: 通过绝对路径read调用
- `_bak_/`: 已归档skill，不再使用

## 显式命令处理

### /bundle 命令

用户输入以 `/` 开头时，直接执行对应组合包：

| 命令 | 组合包 | 执行链 |
|------|--------|--------|
| `/code` | 编程开发 | coding-framework |
| `/review` | 代码审查 | code-review → code-review-visualizer |
| `/plc` | PLC编程 | codesys-auto-programmer → plc-code-reviewer → bom-checker |
| `/report` | 生成报告 | document-pro → html-report |
| `/weekly-report` | 装备所周报 | weekly-report-framework → internal-comms-midea |
| `/research` | 投研分析 | stock-research → html-report |
| `/fund-report` | 基金日报 | fund-daily-report → html-report |
| `/knowledge` | 知识查询 | knowledge-router |
| `/frontend` | 前端页面 | frontend-design → web-artifacts-builder |
| `/translate` | 翻译 | translation → humanizer |

### @skill 命令

用户输入以 `@` 开头时，直接调用指定skill：

```
@coding-framework → 直接执行coding-framework
@code-review → 直接执行code-review
```

如果skill已归档（deprecated），告知用户原因和替代方案。

## 分类体系（9大类）

| 分类 | 入口skill | 覆盖范围 |
|------|-----------|----------|
| 🏭 工业自动化 | domain-kit | PLC编程、设备管理、领域知识 |
| 💻 软件开发 | coding-framework | 编程、代码审查、前端设计、工程化 |
| 📊 投研分析 | stock-research | 股票、基金、量化选股 |
| 📝 文档报告 | document-pro | 文档处理、报告生成、翻译、论文 |
| 🧠 知识管理 | knowledge-router | 知识查询、图谱、笔记、Wiki |
| 🤖 Agent系统 | self-improving | Agent进化、技能管理、Prompt工程 |
| 📋 任务规划 | daily-agent | 任务调度、工作分解、PRD、会议 |
| 🌐 Web数据 | web-crawler (`_inactive/`) | 网页获取、爬取、浏览器自动化 |
| 🔧 实用工具 | weather | 天气、地图、新闻、备份、调试 |

## 辅助命令

可通过路由引擎CLI查看系统信息：

```bash
# 列出所有分类
python D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\scripts\router_engine.py --list-categories

# 列出分类下所有技能
python D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\scripts\router_engine.py --list-skills software_dev

# 列出所有组合包
python D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\scripts\router_engine.py --list-bundles

# 查看使用统计
python D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\scripts\router_engine.py --usage-stats
```

## 注意事项

1. **不要自己猜测该用哪个skill**——永远先调用路由引擎
2. **路由引擎出错时**——向用户报告错误，建议重新描述需求
3. **Bundle执行中某步失败**——停止执行，报告错误，不自动跳过
4. **用户纠正路由结果**——记录纠正，后续按纠正结果执行
