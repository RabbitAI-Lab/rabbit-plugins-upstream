## Description:

apipay helps agents use prepaid web search, markdown URL fetching, and weather APIs without asking for vendor API keys, with optional BYOK access for other catalog APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamalanlui](https://clawhub.ai/user/iamalanlui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use apipay to run web search, fetch web pages as markdown, check weather, manage prepaid API credits, and configure MCP access without requesting separate vendor API keys for the no-key catalog paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, fetched URLs, weather coordinates, signup email, payment or top-up activity, and BYOK keys may be sent to a third-party service.

Mitigation: Avoid sending sensitive data unless third-party processing fits the user's risk tolerance, and confirm trust in apipay and the apipay-mcp package before installation.

Risk: Bearer tokens and BYOK credentials could be exposed through chat, URLs, or logs.

Mitigation: Keep tokens in environment variables or the vault flow, never place bearer tokens in URLs or chat, and log only slug, cost, latency, and status.

Risk: Payment-required responses or catalog misses could lead an agent to invent payment paths or request unnecessary vendor keys.

Mitigation: Use only the returned topup_url for HTTP 402 handling, retry after payment, and request vendor keys only when the user explicitly selects a BYOK slug.

Risk: Weather output can omit required Open-Meteo attribution.

Mitigation: Keep Open-Meteo CC BY 4.0 attribution next to displayed weather results.

## Reference(s):

- [apipay homepage](https://apipay.fly.dev)
- [apipay signup API](https://apipay.fly.dev/v1/signup)
- [apipay hosted MCP endpoint](https://apipay.fly.dev/mcp)
- [ClawHub apipay skill page](https://clawhub.ai/iamalanlui/skills/apipay)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline API calls, JSON configuration, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include service slugs, costs, authentication guidance, 402 handling steps, and attribution reminders.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
