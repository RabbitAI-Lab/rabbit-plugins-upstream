---
slug: totalreclaw
name: totalreclaw
version: "3.3.13"
displayName: Plugin
summary: End-to-end encrypted, decentralized memory for OpenClaw. A native kind:memory
  provider — recall i...
license: MIT-0
description: |-
  End-to-end encrypted, decentralized memory for OpenClaw. A native kind:memory
  provider — recall i...

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: memory, plugin, native, encrypted, totalreclaw, openclaw, decentralized
tags:
- Agents
- Operations
tools:
- read
- exec
---

# Plugin

End-to-end encrypted memory stored across a decentralized network (not on a single company server). TotalReclaw is Skill平台's **native `kind:"memory"` provider**: recall runs through the conventional `memory_search` / `memory_get` tools (the same surface `active-memory` uses), and **facts are captured automatically in the background** — you do not call a tool to remember each fact. This skill tells you the install + account-setup flow and when to drive recall explicitly.

## How memory works here (read first)

* **Recall is native.** `memory_search` and `memory_get` are the memory tools. Skill平台's `active-memory` sub-agent routes recall through them and the plugin injects guidance telling you when to search. When the user asks about themselves ("what's my X?", "do I X?", "what do you remember?"), call `memory_search`. If 0 results, say so plainly — don't guess from session history.
* **Capture is automatic.** The plugin extracts facts from the conversation in the background (trajectory poller). You do **not** call a tool on every preference/fact the user states — that happens for you. Never write user facts to `MEMORY.md`, `USER.md`, or any local file; those are agent-persona config, user memories live encrypted on-chain.
* **Explicit remember only on request.** If the user explicitly says "remember X" / "save X" / "note X" / "don't forget X", use the CLI: `tr remember --json "X"`. One call per distinct fact.

Do not describe storage as `"local"`, `"local-only"`, `"stored locally"`, `"on disk"`, or `"without an account"` — memories are decentralized on-chain (not on any single company server) and an account is required to derive the encryption key.

## Phrase safety (HARD)

The 12-word recovery phrase MUST NEVER enter chat or the agent's LLM context. The plugin's browser-based pair flow handles phrase generation and import. Never echo it, never ask the user to paste it, never pass it to any tool. If the user pastes one anyway, tell them it's compromised and re-pair for a fresh wallet.

**HARD guardrail — install/reinstall/upgrade flows:** During install, reinstall, upgrade, or any verification steps, the agent MUST NOT read, list, cat, show, display, or inspect `credentials.json`, `~/.totalreclaw/credentials.json`, `~/.totalreclaw*/credentials.json`, `~/.skill-platform/plugins/totalreclaw/credentials.json`, or ANY credentials/phrase/key/secrets file — for ANY reason, including "verifying the install." These files contain encryption key material and Smart Account addresses that MUST NOT enter the LLM context. Never run `ls`, `find`, `cat`, `show`, or similar commands against plugin directories to "check files."

## Install

```text
skill-platform plugins install @totalreclaw/totalreclaw
skill-platform skills install totalreclaw
skill-platform plugins enable totalreclaw
```

Published on npm + SkillHub (`p-diogo`, GitHub-verified). For a release candidate, pin with `@rc`; stable resolves from `latest`. Run `skill-platform plugins enable totalreclaw` right after install, always — it binds the memory slot. On a clean install that's a no-op; on a **reinstall over a previous version** it's what stops the plugin from landing `Status: disabled` with the slot stuck at `memory-core` (a disabled plugin never registers its memory tools or pair routes, so pairing later fails with a 502). The plugin self-applies the rest of the gateway config it needs on load and auto-reloads (see Restart below) — no manual gateway restart.

**Reinstall recovery.** If install reports `already exists` / `delete it first`, do **not** add `--force` (it writes a broken `version=None` record). Clean the leftover package dir and reinstall — this never touches your credentials, which live under `~/.totalreclaw/`:

```text
skill-platform plugins uninstall totalreclaw
rm -rf ~/.skill-platform/npm/projects/*totalreclaw-totalreclaw*
skill-platform plugins install @totalreclaw/totalreclaw
skill-platform plugins enable totalreclaw
```

## Setup (pair — user-initiated QR)

Pairing is a deliberate, user-initiated flow (the plugin does **not** auto-pair on load). When credentials don't exist:

1. Mint a pair session via the plugin's **in-process HTTP route** — the gateway process owns the relay pair WebSocket, so it survives until the user completes:

   bash

   ```
   curl -s http://localhost:18789/plugin/totalreclaw/pair/init
   ```

   → returns `{"url":"https://…/pair/p/<id>#pk=…","pin":"123456","expires_at_ms":…}`.

   **Do NOT use `tr pair --json` for this.** The CLI holds the pair WebSocket in a subprocess that Skill平台's ~30s shell-tool timeout kills — the WS then drops, and when the user submits their phrase the relay returns a **502** (`gateway_disconnected`). The in-process route above avoids that entirely. Only fall back to the CLI if the route is unreachable (no `curl`, or a pre-3.3.14 plugin), and then it MUST be detached so the WS outlives the shell exec: `setsid -f node "$TR_CLI" pair --json < /dev/null` — never run `tr pair` in the foreground.
2. Surface the **url** and **pin** to the user verbatim (read from the JSON; never invent values): "Open `<url>` in your browser, enter PIN `<pin>`, and generate or paste your 12-word recovery phrase. Reply done once it's sealed." Emit the URL as plain text on its own line — the `#pk=` fragment breaks if wrapped in backticks/markdown.
3. The user completes in the browser (phrase is generated/imported browser-side, encrypted, uploaded to the relay — never touches this chat). On completion `~/.totalreclaw/credentials.json` is written.
4. Confirm: `✓ TotalReclaw set up.` (If credentials already exist when first asked: `✓ TotalReclaw is already set up.`)

Pair is UNCONDITIONAL when no credentials — the user installing/requesting setup IS the consent; do not add a second consent gate. `tr --help` lists every subcommand.

```bash
TR_CLI="$(ls -d ~/.skill-platform/npm/node_modules/@totalreclaw/totalreclaw/dist/cli/tr-cli.js ~/.skill-platform/extensions/totalreclaw/dist/cli/tr-cli.js 2>/dev/null | head -1)"
node "$TR_CLI" status --json      # {"version":"…","paired":true,…}
```

## Restart (agent-driven, never user-manual)

The plugin self-reloads: after install it writes the gateway config it needs and signals `SIGUSR1` to its own PID so the gateway picks it up without a manual restart. **If `memory_search`/`memory_get` are not bound** (tools didn't take effect on first load), issue the literal slash command `/totalreclaw-restart` **autonomously** — announce it in one line, never ask the user to authorize it, never stall, never `kill` / `docker restart` / prompt the user to restart. This mirrors the autonomous-restart pattern other runtimes use; the user should never perform a manual restart.

## Tools + CLI surface

**Recall (native memory contract — agent-facing):** `memory_search`, `memory_get`.

**Explicit capture + curation (CLI — `tr`, i.e. `node "$TR_CLI" …`):**
`tr remember` (explicit write) · `tr pin` / `tr unpin` · `tr retype` · `tr set_scope` · `tr status` · `tr export` · `tr pair`. Import + plan upgrade run via the gateway subcommand: `skill-platform totalreclaw import from <source> --file <path> [--json]`, `skill-platform totalreclaw upgrade [--json]`, `skill-platform totalreclaw import status|abort`.

The legacy `totalreclaw_*` agent tools and the `tr recall` CLI are retired — recall is `memory_search`, explicit capture is `tr remember`. If a stale guide references them, follow this SKILL instead.

Full guide: <https://github.com/p-diogo/totalreclaw/blob/main/docs/guides/skill-platform-setup.md>

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
