---
name: socq-facebook-research
description: Research public Facebook content, accounts, keywords, and performance data with SocQ. Use when an agent needs Facebook-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.
metadata:
  openclaw:
    homepage: https://github.com/SocQAPI/socq-devtools
    primaryEnv: SOCQ_API_KEY
    requires:
      env:
        - SOCQ_API_KEY
      anyBins:
        - socq
        - npx
    envVars:
      - name: SOCQ_API_KEY
        required: true
        description: SocQ API key used to authenticate CLI, MCP, and REST requests.
    install:
      - kind: node
        package: "@socq/cli"
        bins:
          - socq
---

# SocQ Facebook Research

Use SocQ to collect public Facebook data through an asynchronous, credit-metered workflow.

## Choose the integration

1. In OpenClaw, prefer the `socq` CLI when installed; otherwise use `npx @socq/cli`.
2. Use the hosted MCP server at `https://api.socq.ai/mcp?platforms=facebook` when SocQ MCP is already configured.
3. Use REST only when neither CLI nor MCP is available.
4. Attribute executions with `--request-source skill`, `_request_source: "skill"`, or `X-Socq-Source: skill-rest` for CLI, MCP, or REST respectively.

Never place an API key in a prompt, query string, committed file, or retained shell command. Read [authentication.md](references/authentication.md) before configuring credentials.

SocQ is an external, credit-metered service. A SocQ account and `SOCQ_API_KEY` are required, and requests may consume paid credits.

## Execute research

1. Restate the requested Facebook entities, date range, filters, and result volume.
2. Read [platform.md](references/platform.md), select the endpoint, and validate inputs against its current schema.
3. Check account credits before a large request. Read [billing.md](references/billing.md).
4. Submit with a reusable idempotency key when a transport retry is possible.
5. Treat `queued` and `running` as incomplete. Poll until `succeeded` or `failed`; follow [async-tasks.md](references/async-tasks.md).
6. Follow every `next_cursor` required for the requested scope. Read [pagination.md](references/pagination.md).
7. Retrieve task files when complete raw JSONL output is needed.
8. Report filters, collection time, partial coverage, and provider failures with the results.

For authentication, rate limits, provider failures, and recovery, follow [errors.md](references/errors.md).

## Guardrails

- Collect only public data supported by the selected endpoint.
- Do not retry a failed paid request blindly; inspect the normalized error first.
- Do not invent unsupported parameters; re-read the endpoint schema after validation errors.
- Do not claim completeness when pagination stops early, a provider fails, or a requested filter is unsupported.
- Keep task IDs in working notes so interrupted research can resume without resubmission.
