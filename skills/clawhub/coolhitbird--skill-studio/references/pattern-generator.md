# Pattern: Generator（生成器）

> 控制的不确定性：**输出不确定**——每次输出结构都不一样。

## 何时用

当输出每次都需要遵循固定结构时：**一致性比创造力更重要**。

典型场景：
- 技术报告（执行摘要/方法论/发现/建议，无论主题如何始终同顺序）
- API 文档（每个端点：描述/参数/请求响应示例/错误码）
- 提交消息（Conventional Commits：feat:/fix:/docs:）
- 周报、方案文档

## 目录结构

```
skill-name/
├── SKILL.md                    # 编排流程
├── references/
│   └── style-guide.md          # 控制语气、格式、质量规则
└── assets/
    └── template.md             # 控制输出结构
```

**三分角色**（拆分让 Skill 好维护）：

| 文件 | 作用 | 改它=改什么 |
|---|---|---|
| SKILL.md | 编排流程 | 改流程 |
| references/style-guide.md | 语气/格式/质量 | 改文风 |
| assets/template.md | 输出结构 | 改输出格式 |

## 核心要素：6 步输出契约

Generator 的核心不是"生成"，而是**输出契约**。成熟 Generator 不说"请生成一份报告"，而明确要求：

1. **加载风格指南**（`references/style-guide.md`）
2. **加载输出模板**（`assets/template.md`）
3. **检查缺失字段**
4. **向用户补问必要信息**
5. **填充模板的每个部分**（模板中每个部分都必须出现）
6. **返回完整文档**

## 最小 SKILL.md 骨架

```markdown
---
name: report-generator
description: 生成 Markdown 格式的结构化技术报告。当用户要求编写、起草或分析报告时使用。
agent_created: true
---

你是技术报告生成器。严格遵循以下步骤：

步骤1：加载 `references/style-guide.md` 获取语气和格式规则。

步骤2：加载 `assets/report-template.md` 获取所需的输出结构。

步骤3：询问用户填充模板所需的任何缺失信息：
- 主题或课题
- 关键发现或数据点
- 目标受众（技术、高管、通用）

步骤4：按照风格指南规则填充模板。模板中的每个部分都必须出现在输出中。

步骤5：将完成的报告作为单个 Markdown 文档返回。
```

## assets/template.md 示例

```markdown
# {Report Title}

**Date:** {YYYY-MM-DD}
**Audience:** {Technical | Executive | General}

## Executive Summary
{150 words max. Key findings and recommendation.}

## Background
{Context: why this report exists}

## Findings
{Description with supporting evidence.}

## Recommendations
1. {Actionable recommendation with rationale}

## Next Steps
- [ ] {Concrete action item with owner/timeline}
```

## 常见坑

| 坑 | 后果 | 修正 |
|---|---|---|
| 只说"生成报告"不定义步骤 | 每次结构漂移 | 用 6 步输出契约 |
| 风格和结构混在一个文件 | 改文风连结构也动 | 风格→references/，结构→assets/ |
| 模板部分允许省略 | 输出不完整 | "模板中每个部分都必须出现" |
