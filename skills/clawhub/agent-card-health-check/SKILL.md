---
name: agent-card-health-check
summary: Use this free no-storage MCP to check an authorized A2A Agent Card, its endpoint, and its authentication declaration before connecting.
---

# Agent Card Health Check

Use this skill before connecting to an A2A agent you own or are explicitly authorized to reach.

## Connect

- MCP endpoint: `https://agent-card-health-check.kadopi.workers.dev/mcp`
- MCP Service Card: `https://agent-card-health-check.kadopi.workers.dev/.well-known/agent-card.json`
- Product page: `https://aegis-sales-bot.kadopi.workers.dev/products/agent-card-health-check`
- Source: `https://github.com/kadopi/my-projects/tree/main/apps/agent-card-health-check`
- MCP Registry search: `https://registry.modelcontextprotocol.io/?q=io.github.kadopi%2Fagent-card-health-check`

## First call

Call `diagnose_agent_card` with an Agent Card and an `authorizedTargetUrl` that you own or have permission to check.

## Limits

The check is read-only and stores no Agent Card, credentials, remote response, or result. It reports connection readiness; it is not a security guarantee or vulnerability assessment.
