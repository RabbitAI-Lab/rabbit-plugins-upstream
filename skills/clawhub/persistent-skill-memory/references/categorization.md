# categorization.md — 域分类关键词表（供参考）

规则：取技能 `name` 与 `description` 拼接后**小写**；按优先级序（下表从上到下）扫描 10 域，域内任一关键词**子串**命中即归该域——**first-match-wins，不允许多标签**。全不命中 → `general`。

优先级序是有意保守的：跨域技能（如 "security research"）归先列域——确定性、无歧义、可预期。

| 优先级 | 域 | 关键词（小写子串） |
| --- | --- | --- |
| 1 | agents-orchestration | agent, orchestration, swarm, router, playbook, mcp, tool-calling |
| 2 | research-grounding | research, grounding, evidence, citation, literature, survey, benchmark, fact-check |
| 3 | data-parsing | parse, parser, dicom, pdf, csv, json, xml, extract, convert, deid, nifti, imaging |
| 4 | security-redteam | security, redteam, red-team, vuln, vulnerability, pentest, threat, exploit, attack, defense, harden, audit |
| 5 | build-engineering | build, compile, debug, refactor, deploy, infra, ci/cd, test, code |
| 6 | content-writing | write, draft, article, copywriting, marketing, seo, content, blog, newsletter |
| 7 | media-generation | image, audio, speech, video, tts, render, music, illustration |
| 8 | ops-sandbox | sandbox, snapshot, docker, kubernetes, server, monitoring, cron, async, stall, wipe, restore, deploy |
| 9 | education-learning | learn, teach, explain, tutorial, course, quiz, study, education |
| 10 | productivity-personal | todo, plan, calendar, email, notes, memory, organize, habit, goal |
| 兜底 | general | （无关键词） |

## 已知碰撞（first-match-wins 的确定性结果）
- `deploy` 同时属 5（build-engineering）与 8（ops-sandbox）→ 归 **5**。
- `test` → 5（不归 9）。
- "agent memory" 技能：`agent` 先命中 → **1**；仅 "memory" → 10。
- "audit"（安全审计）→ 4；"code audit" → 仍 4（`audit` 在 4 先于 `code` 在 5）。

## 工作示例（务必按优先级扫描，勿按"最强关联"猜）
- `y-tool` / "parses DICOM evidence" → **research-grounding**：扫描序域 2 先命中 `evidence`，
  早于域 3 的 `parse`/`dicom`——相关度不参与判定。
- `x-tool` / "agent router playbook" → **agents-orchestration**：域 1 命中 `agent` 即止。
- 判定只看"优先级序中首个命中的域"，与命中词个数/相关度无关。

## 维护纪律
- 加新域：追加到表**尾**（不改既有优先级），同步更新 `scripts/skill_memory.py` 顶部 `DOMAINS` 与 `scripts/selftest.py` G4 的域清单断言，重跑 selftest。
- 关键词必须 ASCII 小写（确定性 + 可排序）；多词词组用连字符（`red-team`、`tool-calling`）。
- 任何调整必须重跑：`selftest` → `inject`（幂等替换）→ `verify`（rc0）。
