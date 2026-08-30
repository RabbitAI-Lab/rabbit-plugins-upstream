---
name: jd-drama
description: Install and use the public beta jd-drama CLI to operate JianDan short-drama projects, scripts, uploaded imports, assets, storyboards, videos, brands, and task diagnostics from Codex, Code, OpenClaw, or other agents.
metadata:
  openclaw:
    requires:
      bins:
        - jd-drama
---

# JianDan Short-Drama CLI

## Install And Start

1. Check `command -v jd-drama` and `jd-drama --version`.
2. If missing or older than `1.0.0-beta.3`, install or update with `npm install -g @flyengine/jd-drama-cli@beta`.
3. Run `jd-drama --json doctor`. The public beta defaults to `https://jiandan.flyengine.cn/api`, the JianDan production environment.
4. If `auth.browserAuthorization.authorized` is false, run `jd-drama auth login` and let the user approve it in the JianDan browser page.
5. Run `jd-drama --json release-check` before live work and proceed only when `data.ok` is true.

Never ask for a JianDan password or Token. The CLI supports browser authorization only. Use `--json` for agent calls. Do not override the production API unless the user explicitly requests a local or test environment.

```bash
npm install -g @flyengine/jd-drama-cli@beta
jd-drama --version
jd-drama --json skill doctor --target codex
jd-drama auth login
jd-drama --json release-check
```

## Discover And Read

```bash
jd-drama --json projects list --limit 10
jd-drama --json projects get <projectId>
jd-drama --json brands list --keyword "品牌名"
jd-drama --json assets summary <projectId>
jd-drama --json storyboard episodes <projectId>
jd-drama --json tasks recovery-plan <projectId>
```

Use named commands first. `raw get` is only for missing read wrappers under `/user/ai-drama` or `/user/brands`; full URLs are forbidden.

## Create

Preview every write with `--dry-run`. Execute only after the user approves the exact action, using the same command with `--confirm`.

```bash
jd-drama --json ai-script create --idea "品牌短剧创意" --episode-count 10 --name "项目名" --generate --dry-run
jd-drama --json imports create-from-file ./script.md --name "项目名" --parse-assets --dry-run
```

To associate a brand, resolve its ID and pass `--brand-id` plus `--brand-placement-depth auto|light|medium|heavy` during initial project creation. Do not change an existing project's brand.

## Storyboard And Video

```bash
jd-drama --json storyboard optimize-segment <projectId> --episode-id <episodeId> --segment-id <segmentId> --dry-run
jd-drama --json storyboard update-segment <projectId> --episode-id <episodeId> --segment-id <segmentId> --duration-seconds 8 --text "完整分镜" --dry-run
jd-drama --json video generate <projectId> --episode-id <episodeId> --segment-ids <segmentId> --model-code <modelCode> --resolution 720p --dry-run
```

Segment optimization returns a candidate but does not save it. Review the candidate, then preview and confirm `storyboard update-segment` separately.

## Boundaries

- Treat the current npm package as a public beta connected to production user data and real quotas.
- Do not expose credentials or config file contents.
- Do not bypass `--dry-run` and `--confirm` with direct API calls.
- Do not run Agent chat, task retry, generic asset generation, or raw non-GET requests as live writes.
- Diagnose failures with `tasks errors` or `tasks recovery-plan` before retrying work.
