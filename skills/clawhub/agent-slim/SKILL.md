---
name: agent-slim
slug: agent-slim
displayName: Agent 整体瘦身师
version: 0.2.0
status: released
platforms: [macos, windows, linux]
author: lis
license: MIT
description: Agent 瘦身：盘点、注入测量、发布闸门、回滚；不删原件。
---

# Agent Slim

Agent 用久了，规则、Skill、参考文档、插件、备份和旧会话会越积越多。本技能有两个入口：整体盘点后给出可回滚的减负计划；以及在 Skill 发布前测量固定注入、核对漂移、执行最后闸门。默认 dry-run，只移动、不删除。

## 何时使用

- 给这个 Agent 整体瘦身，或找出每轮常驻上下文里的冗余
- 想知道 Token 花在哪，先做只读盘点
- 新 Skill 发布或既有 Skill 改动前，需要最后瘦身闸门
- 怀疑技能目录、AGENTS、记忆或权限块发生注入漂移

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

## 发布闸门（新 Skill 或任何改动，必过）

在发布前按顺序执行；任一项 FAIL 就停在发布前，不把 `UNMEASURED` 或 `UNKNOWN` 写成 PASS。

```sh
python3 scripts/injection_state.py --check       # 先看 DRIFT / BODY_CHANGED
python3 scripts/injection_state.py --record      # 确认变更符合预期后重记基线
python3 scripts/injection_state.py --check       # 必须 overall: OK
python3 scripts/measure_prompt.py --gate 57344   # 文本七块必须 PASS
python3 scripts/self_test.py                     # 必须 ALL PASS
```

硬指标：

- `description` 单条 ≤45 字，保留触发词和“不做什么”。
- `SKILL.md` 目标 ≤8 KB；超出就外移到 `references/`，只搬不删。
- 文本块闸门 57,344 B 必须 PASS；MCP 与 App 整体仍按 `UNKNOWN` / `UNMEASURED` 如实标注。
- `check_integration`、`check_release`、包内测试全部通过，且发布包不含 `.bak.*`、个人路径和公司数据。

## 固定注入测量（Codex）

七块：记忆摘要、基础系统提示、技能目录、权限块、全局 AGENTS、MCP schema、环境上下文。`measure_prompt.py` 只读调用 `codex debug prompt-input` 并解析文本块；不读聊天正文，不写 Codex Home。

```sh
python3 scripts/measure_prompt.py --gate 57344
python3 scripts/measure_prompt.py --json --gate 57344
python3 scripts/scan_layers.py --summary          # 四层去重/冲突，只报告
python3 scripts/budget_dashboard.py --no-measure --out /tmp/budget.md
python3 scripts/mcp_probe.py --stdio --name svc -- <启动命令>
python3 scripts/token_experiment.py --help        # 首请求观测，不是账单
```

- `injection_state.py --record` 不是伪造 PASS，只是确认这批变更后更新下一次比对基准；record 前先看清单和 diff。
- 技能正文、脚本、references 改动通常记 `BODY_CHANGED`，不影响技能目录注入；`description`、技能数量、记忆/AGENTS/rules 改动才会引起 `DRIFT`。
- MCP `tools/list` 原始总量不是每请求注入；App 首请求实际注入缺实测时必须写 `UNMEASURED`。

## 整体瘦身入口

```sh
python3 scripts/agent_slim.py host --home <codex-home> --output host.json
python3 scripts/agent_slim.py audit --json --output audit.json
python3 scripts/agent_slim.py plan --audit audit.json --output plan.json
python3 scripts/agent_slim.py apply --plan plan.json              # dry-run
python3 scripts/agent_slim.py apply --plan plan.json --apply      # 显式事务
python3 scripts/agent_slim.py verify --plan plan.json --test-prompts prompts.json
python3 scripts/agent_slim.py restore --manifest <transaction>/manifest.json --apply
```

`host` 输出 `supported / unknown / unsupported` 三态，没有证据的能力不得当作可用。只执行三种移动：隔离冗余备份、归档已确认关闭的旧会话、隔离已确认低频的 Skill 文件。目标冲突即停止，不覆盖。缺少 `test-prompts` 时，触发/路由回归只能是 `PARTIAL`。

## 边界

只做跨维度盘点、排序、调度、验收和回滚；不重写被瘦身 Agent 的内容，不替其他技能做判断。注入测量只读源文件和 `tools/list` schema，不读会话、备份、日志或数据库正文。禁止删除原件、数据库 VACUUM、改密钥或 provider、上传公司数据。实际改动必须有事务清单、哈希和回滚证据。

## 按需路由

先看 `references/routing-index.md`：要执行读 `docs/usage.md`，要契约读 `docs/execution-contract.md` 和 `docs/audit-json-contract.md`；注入口径读 `docs/injection-measurement.md`、`references/budgets.md`、`references/mcp-measure.md`；与 `ponytail`、`skill-architect`、`memory-orchestrator`、发布流程的边界见 `references/integration-routing.md`。
