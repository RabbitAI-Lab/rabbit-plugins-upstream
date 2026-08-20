<div align="center">

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-compatible-blue.svg)](https://agentskills.io)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

# skill-auditor

检查SKILL.md有没有让AI遵守流程的防丢机制，告诉你缺什么、怎么补。

[English](README.md) · [中文](README_CN.md)

</div>

## 解决什么问题

你写了一个SKILL.md交给AI用，效果不稳定：有时严格按流程走，有时跳过步骤，有时丢失你以为写得很清楚的约束。根本原因是skill缺少迫使AI遵守的结构性模式。

## 快速开始

```bash
npx skills add Foamtor/skill-auditor
```

```bash
python3 scripts/audit_skill.py /path/to/your-skill/SKILL.md
```

输出示例：

```
类型：工作流型（检测到步骤流程）
适用维度：10/10

  ✅  反合理化守卫
  ❌  阶段门禁           — 缺失。AI会一口气跑完不停下。
  ✅  验证脚本
  ❌  陷阱清单           — 缺失。AI会重复已知错误。
  ✅  渐进式加载
  ✅  Context Engineering
  ...

评分：7 通过，0 部分，3 未通过

改进方案：
  1. [关键] 加阶段门禁 — 强制AI在关键节点停下来等确认。
     参考：ruanzhu-from-scratch 的 G0-G4 门禁表。
  2. [关键] 加陷阱清单 — 记录已知的失败模式。
     参考：ai-frontier-notes 中带日期的 "⚠️" 条目。
```

## 检查什么

10个防止AI执行漂移的模式：

| 模式 | 没有它会怎样 |
|------|------------|
| 反合理化守卫 | AI编造借口跳过步骤 |
| 阶段门禁 | AI一口气跑完不等确认 |
| 验证脚本 | AI说"做完了"但没实际检查 |
| 决策流程图 | AI在模糊指令中迷失 |
| 陷阱清单 | AI重复别人已经记录过的错误 |
| 渐进式加载 | context过载，AI忽略关键规则 |
| 三层架构 | 一个文件塞所有内容 |
| Runtime Hooks | 纯文本没有代码级强制 |
| Context Engineering | 关键规则埋在长文件中间 |
| Scoped Rules | 不相关的规则稀释AI注意力 |

不是每个skill都需要10个。脚本自动判断类型，只检查适用的：

- **工作流型**（多步骤流程）：10个全查
- **工具型**（脚本封装）：7个
- **参考型**（速查表）：4个
- **模式型**（方法论）：3个

## 给谁用

**装了第三方skill，效果不稳定。** 跑一下看缺了什么。

**自己写skill，想做得更靠谱。** 发布前检查一遍。

**团队共用skill，要推给其他人。** 当质量门禁用。

## 不做什么

- 不检查内容的事实准确性
- 不自动修skill（给建议，你来改）
- 不保证AI一定遵守（防丢机制降低漂移，不能完全消除）

## 安装

```bash
npx skills add Foamtor/skill-auditor
```

```bash
git clone https://github.com/Foamtor/skill-auditor.git ~/.agents/skills/skill-auditor
```

兼容所有支持 [Agent Skills 标准](https://agentskills.io) 的工具：Claude Code、Codex、Cursor、Gemini CLI、Hermes Agent 等。

## CI 集成

```bash
python3 scripts/audit_skill.py my-skill/SKILL.md || echo "Skill质量检查未通过"
```

退出码：0=通过，1=关键缺失，2=参数错误。

## 协议

[MIT](LICENSE)
