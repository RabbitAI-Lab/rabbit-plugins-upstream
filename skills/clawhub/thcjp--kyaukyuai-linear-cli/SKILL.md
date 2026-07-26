---
slug: kyaukyuai-linear-cli
name: kyaukyuai-linear-cli
version: "3.2.0"
displayName: Linear CLI
summary: Use the linear-cli agent-native runtime to read and mutate Linear from Claude
  Code, Codex, or oth...
license: MIT-0
description: |-
  Use the linear-cli agent-native runtime to read and mutate Linear from
  Claude Code, Codex, or oth...

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: read, linear, runtime, kyaukyuai, native, agent, cli
tags:
- Automation
tools:
- read
- exec
---

# Linear CLI

An agent-native Linear runtime for the current `v3` execution model, with stable JSON contracts, startup discovery, dry-run previews, timeout-aware write semantics, source-adjacent intake, and git/jj workflow integration.

## Recommended Agent Loop

When using this CLI from an agent runtime, prefer this order:

1. Discover command traits with `linear capabilities`; use `--compat v1` only when an older consumer still expects the trimmed legacy shape
2. Read Linear state with default-JSON core surfaces or `--json`
3. Preview writes with `--dry-run --json` when available
4. Apply writes on the default machine-readable surface, then inspect `operation`, `receipt`, and `error.details`
5. Inspect exit codes and `error.details` instead of parsing styled terminal text

Prompt-driven human/debug flows are secondary and explicit. When a command supports prompts or editor entry, pass `--profile human-debug --interactive`; otherwise missing required inputs fail fast.

Agent-safe execution semantics are now the default runtime behavior. `--text` and `--profile human-debug` are the explicit human/debug escape hatches for maintainers, and `--profile agent-safe` remains accepted for compatibility with older automation.

When upstream tooling hands the runtime a normalized Slack, ticket, or similar source envelope, prefer `--context-file`, add `--apply-triage` if that envelope already contains deterministic team/state/label hints, and choose `--autonomy-policy` explicitly when the wrapper needs suggest-only or preview-required staging.

Recommended supporting docs:

* ../../docs/agent-first.md
* ../../docs/v2-to-v3-migration-cookbook.md
* ../../docs/json-contracts.md
* ../../docs/stdin-policy.md

## Prerequisites

The `linear` command must be available on PATH. To check:

```bash
linear --version
```

If not installed, follow the instructions at:
<https://github.com/kyaukyuai/linear-cli?tab=readme-ov-file#install>

## Best Practices for Markdown Content

When working with issue descriptions or comment bodies that contain markdown, prefer file-based flags for existing files and stdin for generated pipeline content:

* Use `--description-file` for `issue create` and `issue update` commands when the content already exists on disk
* Use `--body-file` for `comment add` and `comment update` commands when the content already exists on disk
* Pipe stdin for generated markdown, for example `cat description.md | linear issue create --title "My Issue" --team ENG`

**Why avoid large inline flags:**

* Ensures proper formatting in the Linear web UI
* Avoids shell escaping issues with newlines and special characters
* Prevents literal `\n` sequences from appearing in markdown
* Makes it easier to work with multi-line content in scripts and pipelines

**Example workflow:**

```bash
cat > /tmp/description.md <<'EOF'
## Summary

- First item
- Second item

## Details

This is a detailed description with proper formatting.
EOF

linear issue create --title "My Issue" --description-file /tmp/description.md

cat /tmp/description.md | linear issue create --title "My Issue" --team ENG

linear issue comment add ENG-123 --body-file /tmp/comment.md
```

**Only use inline flags** (`--description`, `--body`) for simple, single-line content.

## Available Commands

```text
linear auth               # Manage Linear authentication
linear issue              # Manage Linear issues
linear team               # Manage Linear teams
linear project            # Manage Linear projects
linear project-update     # Manage project status updates
linear cycle              # Manage Linear team cycles
linear milestone          # Manage Linear project milestones
linear initiative         # Manage Linear initiatives
linear initiative-update  # Manage initiative status updates (timeline posts)
linear label              # Manage Linear issue labels
linear document           # Manage Linear documents
linear notification       # Manage Linear notifications
linear webhook            # Manage Linear webhooks
linear workflow-state     # Manage Linear workflow states
linear user               # Manage Linear users
linear project-label      # Manage Linear project labels
linear config             # Interactively generate .linear.toml configuration
linear schema             # Print the GraphQL schema to stdout
linear api                # Make a raw GraphQL API request
linear capabilities       # Describe the agent-facing command surface
linear resolve            # Resolve references without mutating Linear
```

## Reference Documentation

* [auth](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fauth.md&ownerHandle=kyaukyuai) - Manage Linear authentication
* [issue](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fissue.md&ownerHandle=kyaukyuai) - Manage Linear issues
* [team](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fteam.md&ownerHandle=kyaukyuai) - Manage Linear teams
* [project](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fproject.md&ownerHandle=kyaukyuai) - Manage Linear projects
* [project-update](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fproject-update.md&ownerHandle=kyaukyuai) - Manage project status updates
* [cycle](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fcycle.md&ownerHandle=kyaukyuai) - Manage Linear team cycles
* [milestone](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fmilestone.md&ownerHandle=kyaukyuai) - Manage Linear project milestones
* [initiative](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Finitiative.md&ownerHandle=kyaukyuai) - Manage Linear initiatives
* [initiative-update](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Finitiative-update.md&ownerHandle=kyaukyuai) - Manage initiative status updates (timeline posts)
* [label](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Flabel.md&ownerHandle=kyaukyuai) - Manage Linear issue labels
* [document](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fdocument.md&ownerHandle=kyaukyuai) - Manage Linear documents
* [notification](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fnotification.md&ownerHandle=kyaukyuai) - Manage Linear notifications
* [webhook](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fwebhook.md&ownerHandle=kyaukyuai) - Manage Linear webhooks
* [workflow-state](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fworkflow-state.md&ownerHandle=kyaukyuai) - Manage Linear workflow states
* [user](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fuser.md&ownerHandle=kyaukyuai) - Manage Linear users
* [project-label](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fproject-label.md&ownerHandle=kyaukyuai) - Manage Linear project labels
* [config](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fconfig.md&ownerHandle=kyaukyuai) - Interactively generate .linear.toml configuration
* [schema](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fschema.md&ownerHandle=kyaukyuai) - Print the GraphQL schema to stdout
* [api](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fapi.md&ownerHandle=kyaukyuai) - Make a raw GraphQL API request
* [capabilities](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fcapabilities.md&ownerHandle=kyaukyuai) - Describe the agent-facing command surface
* [resolve](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Fresolve.md&ownerHandle=kyaukyuai) - Resolve references without mutating Linear

For curated examples of organization features (initiatives, labels, projects, bulk operations), see [organization-features](/api/v1/skills/kyaukyuai-linear-cli/file?path=references%2Forganization-features.md&ownerHandle=kyaukyuai).

## Discovering Options

To see available subcommands and flags, run `--help` on any command:

```bash
linear --help
linear issue --help
linear issue list --help
linear issue create --help
```

Each command has detailed help output describing all available flags and options.

For machine-readable discovery, prefer:

```bash
linear capabilities
linear capabilities --compat v1
```

## Using the Linear GraphQL API Directly

**Prefer the CLI for all supported operations.** The `api` command should only be used as a fallback for queries not covered by the CLI.

### Check the schema for available types and fields

Write the schema to a tempfile, then search it:

```bash
linear schema -o "${TMPDIR:-/tmp}/linear-schema.graphql"
grep -i "cycle" "${TMPDIR:-/tmp}/linear-schema.graphql"
grep -A 30 "^type Issue " "${TMPDIR:-/tmp}/linear-schema.graphql"
```

### Make a GraphQL request

**Important:** GraphQL queries containing non-null type markers (e.g. `String` followed by an exclamation mark) must be passed via heredoc stdin to avoid escaping issues. Simple queries without those markers can be passed inline.

```bash
linear api '{ viewer { id name email } }'

linear api --variable teamId=abc123 <<'GRAPHQL'
query($teamId: String!) { team(id: $teamId) { name } }
GRAPHQL

linear api --variable term=onboarding <<'GRAPHQL'
query($term: String!) { searchIssues(term: $term, first: 20) { nodes { identifier title state { name } } } }
GRAPHQL

linear api --variable first=5 <<'GRAPHQL'
query($first: Int!) { issues(first: $first) { nodes { title } } }
GRAPHQL

linear api --variables-json '{"filter": {"state": {"name": {"eq": "In Progress"}}}}' <<'GRAPHQL'
query($filter: IssueFilter!) { issues(filter: $filter) { nodes { title } } }
GRAPHQL

linear api '{ issues(first: 5) { nodes { identifier title } } }' | jq '.data.issues.nodes[].title'
```

### Advanced: Using curl directly

For cases where you need full HTTP control, use `linear auth token`:

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: $(linear auth token)" \
  -d '{"query": "{ viewer { id } }"}'
```

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
