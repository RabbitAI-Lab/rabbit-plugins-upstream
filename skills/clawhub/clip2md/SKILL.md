---
name: clip2md
description: Use clip2md to configure an access token, save web pages or article URLs as Markdown clipping tasks, check remaining daily/permanent quota, query task status, and wait for clipping completion or failure. Use when the user mentions clip2md, 剪藏, clip, 保存网页为 Markdown, 查询额度, 提交链接, 查询任务, 等待剪藏完成, or wants an Agent to operate the clip2md product tool.
metadata:
  openclaw:
    requires:
      bins:
        - node
    emoji: "✂️"
---

# clip2md Agent Tool

Use the bundled CLI. Run commands from this skill folder unless the caller provides another path.

```bash
node scripts/clip2md.js <command>
```

## Agent Workflow

- Before clipping, querying quota, or checking a task, rely on the CLI to detect whether `~/.clip2md/config.json` contains a token.
- If the CLI says the token is missing, expired, or invalid, ask the user for a fresh clip2md token from the web profile page.
- Never print, quote, summarize, or echo the token in user-facing output.
- Summarize command results: task id, status, quota, title/error, and whether Markdown is ready. Do not paste full Markdown content unless the user explicitly asks for it.
- Use `clip` only to submit a URL. Use `wait` only when the user asks to wait for completion or when completion is necessary for the request.

## Commands

Configure token:

```bash
node scripts/clip2md.js config <token>
```

Check quota:

```bash
node scripts/clip2md.js quota
```

Submit a URL:

```bash
node scripts/clip2md.js clip "https://example.com/article"
```

Query one task:

```bash
node scripts/clip2md.js status <task_id>
```

Wait for one task:

```bash
node scripts/clip2md.js wait <task_id> [--timeout <seconds>] [--interval <seconds>]
```

Defaults: timeout 120 seconds, interval 5 seconds.

## Status Semantics

- `SUCCESS`: completed; Markdown is ready when the summary says `Markdown: 已生成`.
- `PENDING`, `PROCESSING`, `WAITING_SERVICE`: still waiting; use `wait` if the user asked for completion.
- `FAILED`, `FAILED_AUTH_EXPIRED`, `FAILED_SERVICE_UNAVAILABLE`, `MANUAL_REVIEW`: not completed; explain the error message/category if present and suggest retrying later or refreshing credentials based on the CLI message.

## Errors

- `401`: token expired or invalid; ask the user for a new token and run `config`.
- `403`: quota or permission problem; report quota/permission failure without retry loops.
- `409`: duplicate link or task conflict; report the conflict and task context.
- `429` or `503`: rate limit or temporary service outage; respect the CLI retry hint when present.

## 配置

Token 存储在 `~/.clip2md/config.json`。
API 默认地址为 `https://clip2.md/api/v1`。Set `CLIP2MD_API_BASE` only for tests or private deployments.
