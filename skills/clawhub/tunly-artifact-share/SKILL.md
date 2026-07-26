---
name: "tunly-artifact-share"
description: "Publish agent-generated artifacts to durable Tunly links with explicit privacy and immutable versions."
license: MIT-0
user-invocable: true
metadata:
  openclaw:
    skillKey: "tunly-artifact-share"
---

# Tunly Artifact Share

Use this Skill when the user asks to share a generated report, review page,
dashboard, prototype, evidence bundle, static site, or other browser-readable
artifact as a durable link.

## Official OpenClaw path

Use the official Tunly CLI. It is the only supported executable integration.

On first use, run `tunly login`, give the user the displayed browser URL and
code, and wait for approval. The user signs in or creates a Tunly account and
approves the connection. Do not ask the user to copy an API key.

When connected, publish with `tunly agent publish`. The default access mode is
`account`; use `public` only after the user confirms the artifact is safe for
the open web. Report the latest URL, immutable version URL/revision, access
mode, and verification result.

```bash
curl -fsSL https://tunly.io/install.sh | sh
tunly login
tunly auth status
tunly agent publish ./dist --json --account
```

`tunly login` starts browser/device authorization. For CI, use
`TUNLY_API_KEY` or `tunly login <key>`. Do not refer to `TUNLY_API_TOKEN` or
`tunly whoami`; neither is a supported authentication path.

## First publish in one command

After the user has explicitly asked to share an existing artifact, mark only
that first OpenClaw publication for aggregate, privacy-safe conversion
evidence. Use the requested artifact path; do not create or publish a demo
artifact just to produce a metric.

```bash
TUNLY_SOURCE=openclaw TUNLY_FIRST_PUBLISH=1 TUNLY_AGENT_NAME=openclaw \
  tunly agent publish ./dist --json --account
```

This emits only the bounded integration source and lifecycle outcome. It never
sends an API key, device code, email address, workspace path, or artifact bytes
to the funnel telemetry. Do not set `TUNLY_FIRST_PUBLISH` for retries or later
publications.

## Safety and verification

- Never publish secrets, credentials, private keys, `.env` files, dependency
  directories, or unrelated local data.
- Default customer, project, operational, personal, and unreleased content to
  account-only access.
- Verify that Tunly returns a ready latest URL and immutable version URL before
  saying the artifact is published.
- Do not substitute a local file, localhost URL, temporary tunnel, or chat
  attachment when the user asked for a durable Tunly link.

## Final response

```text
Published: <latest_url>
Version: <version_url_or_revision_id>
Access: <access_mode>
Verified: <latest/version fetch or exact remaining gap>
```
