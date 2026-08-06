---
name: socq-x-research
description: Research public X content, accounts, keywords, and performance data with SocQ. Use when an agent needs X-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.
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

# SocQ X Research

Use SocQ to collect public X data through an asynchronous, credit-metered workflow.

## Choose the integration

1. In OpenClaw, prefer the `socq` CLI when installed; otherwise use `npx @socq/cli`.
2. Use the hosted MCP server at `https://api.socq.ai/mcp?platforms=x` when SocQ MCP is already configured.
3. Use REST only when neither CLI nor MCP is available.
4. Attribute executions with `--request-source skill`, `_request_source: "skill"`, or `X-Socq-Source: skill-rest` for CLI, MCP, or REST respectively.

Never place an API key in a prompt, query string, committed file, or retained shell command. Read [authentication.md](references/authentication.md) before configuring credentials.

SocQ is an external, credit-metered service. A SocQ account and `SOCQ_API_KEY` are required, and requests may consume paid credits.

## Plan X research

Choose the endpoint from the shape of the question instead of treating every X request as generic search:

- Use `x/search` for topic, phrase, hashtag, or time-bounded conversation discovery. Preserve the user's query operators and requested ordering.
- Use `x/trends` for currently trending topics. Report the collection time and requested region because trends are time- and market-sensitive.
- Use `x/profiles` to resolve account identity before collecting an account's posts or network.
- Use `x/user-posts` for a known account's timeline and `x/posts` when the user supplies specific post URLs or IDs.
- Use `x/post-replies`, `x/post-quotes`, or `x/post-retweeters` for distinct engagement behaviors. Do not combine them into one engagement metric without labeling each source.
- Use `x/followers-list` and `x/following-list` for network questions. Treat the returned relationship snapshot as point-in-time data, not proof of historical following.

For conversation analysis, collect seed posts first, retain their IDs, and expand only the requested reply, quote, or repost branches. Distinguish original posts, replies, quotes, and reposts in the final report. When comparing accounts, use the same date window and collection method for each account. X search and trend results can change quickly, so state when the data was collected and avoid claiming exhaustive coverage when pagination or search visibility limits the result.


## Execute research

1. Restate the requested X entities, date range, filters, and result volume.
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
