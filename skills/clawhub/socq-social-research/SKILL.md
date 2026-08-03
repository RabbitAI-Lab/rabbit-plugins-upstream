---
name: socq-social-research
description: Research public social-platform content, accounts, keywords, and SEO search data with SocQ. Use when an agent needs keyword volume, suggestions, related terms, difficulty, intent, organic results, site rankings, or social data; or needs to discover a SocQ endpoint, estimate credits, submit asynchronous jobs, poll results, paginate normalized records, and retrieve raw files through SocQ MCP or CLI.
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

# SocQ Social and SEO Research

Use SocQ to collect public social and SEO data through an asynchronous, credit-metered workflow.

## Choose the integration

1. In OpenClaw, prefer the `socq` CLI when it is installed. Otherwise run the same commands through `npx @socq/cli`.
2. Prefer the hosted MCP server at `https://api.socq.ai/mcp` when the client already has SocQ MCP configured.
3. Use a filtered MCP URL when the platforms or endpoints are known:
   - `?platforms=youtube,tiktok` for at most five platforms.
   - `?tools=youtube_comments,x_search` for at most thirty endpoint tools.
4. Run `npx @socq/mcp` when the client only supports local stdio MCP.
5. Use REST only when neither CLI nor MCP is available.
6. Attribute every execution started by this Skill:
   - pass `_request_source: "skill"` to compact or typed MCP execution tools;
   - pass `--request-source skill` to CLI execution commands;
   - send `X-Socq-Source: skill-rest` for direct REST execution.

Never place an API key in a prompt, query string, committed file, or shell command that will be retained. Read [authentication.md](references/authentication.md) before configuring credentials.

SocQ is an external, credit-metered service. A SocQ account and `SOCQ_API_KEY` are required, and research requests may consume paid credits. Check the available credits and expected endpoint cost before starting a large or cross-platform request.

## Execute research

1. Restate the requested platforms, entities, date range, and result volume.
2. Search the Capability Registry, then describe the selected endpoint before constructing input. Read [catalog.md](references/catalog.md) when tool discovery is unavailable.
3. Read the matching platform reference before choosing inputs or constructing a payload:
   [Facebook](references/platforms/facebook.md),
   [Facebook Ad Library](references/platforms/facebook-ad-library.md),
   [Facebook Marketplace](references/platforms/facebook-marketplace.md),
   [Instagram](references/platforms/instagram.md),
   [LinkedIn](references/platforms/linkedin.md),
   [Pinterest](references/platforms/pinterest.md),
   [Reddit](references/platforms/reddit.md),
   [Threads](references/platforms/threads.md),
   [TikTok](references/platforms/tiktok.md),
   [TikTok Shop](references/platforms/tiktok-shop.md),
   [X](references/platforms/x.md), or
   [YouTube](references/platforms/youtube.md).
   For keyword research, intent, organic results, or site rankings, read
   [SEO](references/platforms/seo.md).
4. Prefer direct URLs or canonical usernames over broad social search when the user supplies them. For SEO work, preserve the requested market and language; do not compare keyword metrics from different locations as if they were equivalent.
5. Check account credits before a large or cross-platform run. Read [billing.md](references/billing.md) for cost controls.
6. Submit with a reusable idempotency key when a transport retry is possible.
7. Treat `queued` and `running` as incomplete. Poll until `succeeded` or `failed`; follow [async-tasks.md](references/async-tasks.md).
8. Follow every `next_cursor` needed for the requested scope, respecting a user-provided result cap. Read [pagination.md](references/pagination.md).
9. Use task files for complete raw JSONL exports when normalized pages are insufficient.
10. Report partial coverage, failed platforms, filters, and collection time with the results.

For research spanning multiple networks, follow [cross-platform.md](references/cross-platform.md). For authentication, rate limits, provider failures, and recovery, follow [errors.md](references/errors.md).

## Guardrails

- Collect only public data supported by the selected endpoint.
- Do not retry a failed paid request blindly; inspect the normalized error first.
- Do not invent unsupported parameters. Re-read the endpoint schema after a validation error.
- Do not claim completeness when pagination stopped early, a provider failed, or the requested date filter is unsupported.
- Keep task IDs in the working notes so interrupted research can resume without resubmission.
