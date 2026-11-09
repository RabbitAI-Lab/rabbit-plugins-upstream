---
name: agent-slim
slug: agent-slim
displayName: Agent 整体瘦身师
version: 0.1.2
status: release-candidate
platforms: [macos, windows, linux]
author: lis
license: MIT
description: 对使用中的 Agent 做跨维度、只读优先、可逆的整体瘦身：盘点常驻与按需上下文，量化 Token 与磁盘影响，分级执行并用回归与回滚保证能力不回退；默认 dry-run。
---

# Agent Slim

Agent 用久了，规则、Skill、参考文档、插件、备份和旧会话会越积越多。本技能先盘点，再给出可回滚的减负计划：只移动、不删除，默认 dry-run。

## 何时使用

- 给这个 Agent 整体瘦身，或找出每轮常驻上下文里的冗余
- 想知道 Token 花在哪，先做只读盘点
- 把低频内容移到按需区，但要求常用任务不受影响

不适用：单个 Skill 的章节外移（`skill-architect`）、某功能是否该存在（`ponytail`）、记忆阈值与交接（`memory-orchestrator`）、改密钥或 provider。

## 三层账本

| 层 | 内容 | 收益口径 |
| --- | --- | --- |
| Hot | 每轮常驻的规则、描述、工具说明 | 缩小才可能减少每轮 Token |
| Warm | 触发才加载的正文、参考、脚本说明 | 只有实际避免加载才算 Token 收益 |
| Cold | 归档、备份、旧会话 | 只记磁盘，不算 Token |

## 流程

1. 只读盘点：识别三层内容、引用关系和加载条件。
2. 量化排序：Token 优先用实际用量，磁盘单列，估算要标置信度。
3. 风险分级：只放行 allowlist 内的三类移动动作，敏感项直接阻断。
4. 可逆执行：`apply` 默认 dry-run；`--apply` 才移动并写事务清单、SHA-256 和恢复脚本。
5. 能力回归：触发词、引用完整性、frontmatter、常用任务、失败恢复。
6. 交付或回滚：门槛不过就回滚并如实记录，不美化数字。

## 入口

```sh
python3 scripts/agent_slim.py host --home <codex-home> --output host.json
python3 scripts/agent_slim.py audit --json --output audit.json
python3 scripts/agent_slim.py plan --audit audit.json --output plan.json
python3 scripts/agent_slim.py apply --plan plan.json              # dry-run
python3 scripts/agent_slim.py apply --plan plan.json --apply      # 显式事务
python3 scripts/agent_slim.py verify --plan plan.json --test-prompts prompts.json
python3 scripts/agent_slim.py restore --manifest <transaction>/manifest.json --apply
```

`host` 输出 `supported / unknown / unsupported` 三态，没有证据的能力不得当作可用。首版只执行三种移动：隔离冗余备份、归档已确认关闭的旧会话、隔离已确认低频的 Skill 文件。目标冲突即停止，不覆盖。缺少 `test-prompts` 时，触发/路由回归只能是 `PARTIAL`。

## 边界

只做跨维度盘点、排序、调度、验收和回滚；不重写被瘦身 Agent 的内容，不替其他技能做判断。审计不读会话、备份、日志或数据库正文。禁止删除原件、数据库 VACUUM、改密钥或 provider、上传公司数据。实际改动必须有事务清单、哈希和回滚证据。

## 按需路由

先看 `references/routing-index.md`：要执行读 `docs/usage.md`，要契约读 `docs/execution-contract.md` 和 `docs/audit-json-contract.md`；与 `ponytail`、`skill-architect`、`memory-orchestrator`、发布流程的边界见 `references/integration-routing.md`。
