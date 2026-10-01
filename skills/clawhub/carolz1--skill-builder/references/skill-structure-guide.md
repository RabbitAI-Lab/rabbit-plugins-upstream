# Skill 结构指南 / Skill Structure Guide

本文件说明一个 Skill 包的目录结构、渐进披露和写作风格。制作或修改 SKILL.md 时参考。

## 目录结构 / Directory layout

```
skill-name/
├── SKILL.md            # 必需，大小写精确
├── scripts/            # 可选：确定性/重复性任务的脚本
├── references/         # 可选：按需加载的领域资料
└── assets/             # 可选：模板、图标、字体等输出素材
```

- 目录名用 kebab-case，与 frontmatter 的 `name` 完全一致。
- 只创建任务真正需要的目录，不生成 README、CHANGELOG、示例脚本或占位文件。
- 确定性重复操作 → scripts；领域知识 → references；交付素材 → assets。

## frontmatter 必填字段 / Required frontmatter fields

```yaml
---
name: skill-name          # 1—64 字符，小写字母+数字+连字符
description: ...          # 20—1024 字符，四要素齐全（见触发词指南）
---
```

## 渐进披露：三层加载 / Progressive disclosure

| 层 | 内容 | 何时加载 |
|---|---|---|
| 1. 元数据 | name + description | 始终在上下文（约 100 词） |
| 2. SKILL.md 正文 | 核心流程和路由 | skill 被触发时（理想 <500 行） |
| 3. 资源 | scripts / references / assets | 按需，脚本可直接执行 |

**要点**：
- SKILL.md 控制在 500 行内，接近上限就拆到 references，并在正文里写清「何时去读哪个文件」。
- 大 reference（>300 行）加目录。
- 多领域 skill 按变体拆分 reference（如 aws.md / gcp.md / azure.md），只读相关的那份。

## 写作风格 / Writing style

- 用祈使句和编号步骤。
- 给出确定的输入、动作、产物、通过条件和失败分支。
- 输出格式给「完整模板 + 填好的真实示例」。
- 解释「为什么」优先于堆砌 ALL CAPS 的 MUST——今天的模型理解力强，讲清原因比下死命令更有效。如果发现自己写了 ALWAYS / NEVER 全大写，是个黄色信号，考虑改成解释原因。
- 正文不出现 TODO、伪代码、版本标注、修改注释或历史 log。文件读起来要像一次写成的定稿。

## 输出格式示例 / Output format example

```markdown
## Report structure
ALWAYS use this exact template:
# [Title]
## Executive summary
## Key findings
## Recommendations
```

## 输入输出示例模式 / Examples pattern

```markdown
**Example 1:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

## 安全红线 / Safety baseline

Skill 不得包含恶意代码、漏洞利用、或任何可能危害系统安全的内容。不配合制作误导性 skill、越权访问、数据外泄等。角色扮演类（roleplay）是可以的。
