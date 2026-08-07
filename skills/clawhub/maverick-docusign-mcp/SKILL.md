---
name: maverick-docusign-mcp
description: Read DocuSign account, envelope, recipient, template, and signing-status data through DocuSign's official developer MCP server. Use when the user asks to inspect DocuSign signing workflows without changing them.
metadata:
  openclaw:
    emoji: '✍️'
    homepage: https://developers.docusign.com/tools/mcp-server/
    requires:
      bins:
        - mcporter
      env:
        - MAVERICK_DOCUSIGN_MCP_ACCESS_TOKEN
        - MAVERICK_DOCUSIGN_MCP_REFRESH_TOKEN
        - MAVERICK_DOCUSIGN_MCP_CLIENT_ID
        - MAVERICK_DOCUSIGN_MCP_CLIENT_SECRET
    primaryEnv: MAVERICK_DOCUSIGN_MCP_REFRESH_TOKEN
    setup:
      script: scripts/setup.sh
    install:
      - id: node
        kind: node
        package: mcporter@0.12.3
        bins:
          - mcporter
        label: Install mcporter (node)
---

# DocuSign

## How to use this skill

This skill is a thin pass-through to DocuSign's official developer MCP server at `https://mcp-d.docusign.com/mcp`. The bundle exposes only the six approved read tools. The live server remains the source of truth for their current schemas and server-published instructions.

Discover the live tool schemas before calling a tool:

```sh
mcporter --config {baseDir}/mcporter.json list maverick-docusign --schema
```

Call a discovered read tool with structured output:

```sh
mcporter --config {baseDir}/mcporter.json call --output json maverick-docusign.<tool> key=value
```

The allowed tools are exactly:

- `getUserInfo`
- `getAccount`
- `getEnvelopes`
- `getEnvelope`
- `listRecipients`
- `getTemplates`

## Read-only boundary

This first release cannot create, send, void, update, remind, pause, resume, or otherwise change DocuSign data. The `allowedTools` list in `mcporter.json` enforces that boundary at the tool layer. Do not try to bypass it with direct DocuSign API calls or a different MCP configuration.

Agreement Manager tools are also excluded because this release requests only the `signature` OAuth scope. It does not request `adm_store_unified_repo_read`.

## Authentication

Credentials are provisioned at setup time by `scripts/setup.sh` (a thin delegator to `scripts/init-mcporter-oauth.sh`) and stored in mcporter's local vault. The setup hook requires these credential env vars:

- `MAVERICK_DOCUSIGN_MCP_REFRESH_TOKEN`
- `MAVERICK_DOCUSIGN_MCP_CLIENT_ID`
- `MAVERICK_DOCUSIGN_MCP_CLIENT_SECRET`
- `MAVERICK_DOCUSIGN_MCP_ACCESS_TOKEN`

For refresh-aware seeding, setup also reads optional expiry metadata env vars when the provisioner supplies them:

- `MAVERICK_DOCUSIGN_MCP_EXPIRES_AT`
- `MAVERICK_DOCUSIGN_MCP_EXPIRES_IN`
- `MAVERICK_DOCUSIGN_MCP_REFRESH_TOKEN_EXPIRES_AT`

mcporter sends the refreshed bearer token to DocuSign's hosted MCP server and refreshes expired access tokens through DocuSign's demo token endpoint. If calls keep returning authentication errors after retry, the OAuth grant has likely been revoked or expired; reconnect the integration.

## Data flow

Tool arguments and results travel over HTTPS to DocuSign's hosted developer MCP server. DocuSign sees the account, envelope, recipient, template, and signing-status data referenced by each call. Use this skill only with a DocuSign developer/demo account and do not pass unrelated sensitive content through these tools. Production endpoint promotion is outside this bundle's scope.

## Dependencies

- **`mcporter`** ([github.com/openclaw/mcporter](https://github.com/openclaw/mcporter)) — MCP CLI used to discover and call the hosted MCP server. If it is missing from `PATH`, the frontmatter installs the exact `mcporter@0.12.3` package with npm install scripts disabled.

## References

- DocuSign MCP overview: <https://developers.docusign.com/tools/mcp-server/>
- DocuSign developer MCP endpoint: <https://mcp-d.docusign.com/mcp>
