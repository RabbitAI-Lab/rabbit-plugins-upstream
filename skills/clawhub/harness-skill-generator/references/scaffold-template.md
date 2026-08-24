# 脚手架模板 — Phase 3 使用

## SKILL.md 骨架模板

```markdown
---
name: <skill-name>
description: "<一句话描述做什么 + 不做什么 + 触发词>"
---

# <Skill 名称>

## 边界

### 做
- [明确列出 3-5 种任务类型]

### 不做
- [明确列出容易混淆的场景]

### 判断规则
- 如果用户要的是 [不做范围内的东西] → 停下来澄清，不进入本 Skill
- 如果用户没有提供 [必要输入] → 反问，不凭空创作

## 工作流

Phase 0  [名称]    [一句话]
   ▼
Phase 1  [名称]    [一句话]
   └ ★Checkpoint 1  确认：[清单]
   ▼
Phase 2  [名称]    [一句话]
   └ ★Checkpoint 2  确认：[清单]
   ▼
Phase 3  [名称]    [一句话]
   ▼
Phase 4  Delivery  交付

## 质检协议

| 节点 | 方式 | 产物 | 为什么 |
|---|---|---|---|
| [阶段] | [方式] | [产物] | [理由] |

## Phase 0 — [名称]
做什么（2-3行）
必读：references/xxx.md
自检：[检查项]

## Phase 1 — [名称]
做什么（2-3行）
必读：references/xxx.md
产出：[文件]

## ★Checkpoint 1 — [名称] ★硬节点
确认项：
1. [决策A] — 选项：X / Y / Z（推荐 X，因为...）
2. [决策B] — 选项：A / B（推荐 A，因为...）
铁律：每项独立确认，禁止打包

...

## 铁律
1. [最重要的约束]
2. [第二重要的约束]
3. ...
```

## manifest.json 模板

```json
{
  "name": "<skill-name>",
  "version": "0.1.0",
  "category": "<分类>",
  "description": "<一句话描述>",
  "compat": ["openclaw"]
}
```

## 项目工作区模板

```
<project>/
├── input/               输入文件（标准化后的）
├── plan/                方案文件
│   ├── human-workflow.md  人类工作流（Phase 1 产出）
│   ├── agent-workflow.md  Agent 工作流（Phase 2 产出）
│   └── plan.md            最终方案
├── output/              产出文件
├── review/              审查记录（按需）
├── scripts/             脚本（按需）
└── test-run-report.md   试运行报告（Phase 5 产出）
```
