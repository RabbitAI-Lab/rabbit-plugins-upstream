---
name: agent-card-health-check
summary: Use this free no-storage MCP to assess an authorized A2A Agent Card's connection readiness before connecting. It is not a security audit.
---

# Agent Card Health Check

Use this skill before connecting to an A2A agent that you own or are explicitly authorized to reach. It is useful when an Agent Card, its declared endpoint, or its authentication declaration has changed, or when a connection fails before a task can start.

Do not use it to scan unknown agents, assess behavior or cybersecurity, or decide whether an agent is trustworthy.

## Connect

- MCP endpoint: `https://agent-card-health-check.kadopi.workers.dev/mcp`
- MCP Service Card: `https://agent-card-health-check.kadopi.workers.dev/.well-known/agent-card.json`
- Product page: `https://aegis-sales-bot.kadopi.workers.dev/products/agent-card-health-check`
- Source: `https://github.com/kadopi/my-projects/tree/main/apps/agent-card-health-check`
- MCP Registry search: `https://registry.modelcontextprotocol.io/?q=io.github.kadopi%2Fagent-card-health-check`

## Diagnose

Call `diagnose_agent_card` with:

- `agentCard`: the exact Agent Card to be checked;
- `authorizedTargetUrl`: an HTTPS A2A endpoint that you own or are explicitly authorized to reach;
- `authorization`: only when the target requires Bearer authentication and the credential is available through the authorized runtime.

Do not copy credentials into logs, tickets, or the result. Do not guess a target URL or authorization scheme.

## Interpret the result

| Result | Next action |
| --- | --- |
| `connectable` | The declared Card and the read-only endpoint response are consistent enough to proceed with the authorized connection. |
| `auth_required` | Obtain the correct authorized authentication configuration; do not bypass it. |
| `configuration_mismatch` | Correct the Agent Card or endpoint configuration, then diagnose again. |
| `unreachable` | Confirm the endpoint is available to the authorized caller before retrying. |

Return the result, the mismatch or missing configuration, and the smallest owner action. Do not label the target safe or unsafe.

## Limits

The check is read-only and stores no Agent Card, credentials, remote response, or result. It reports connection readiness; it is not a security guarantee or vulnerability assessment.
