## Description:

Helps agents claim and manage public hostnames for websites, APIs, and webhooks using AgentDomains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tashfeenahmed](https://clawhub.ai/user/tashfeenahmed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create public hostnames and manage DNS records, HTTPS setup, redirects, reverse proxies, and nameserver delegation for sites, APIs, and callbacks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public DNS names and proxies can expose private or unauthenticated services.

Mitigation: Confirm the intended public exposure; do not point or proxy private, administrative, or local-only services without authorization.

Risk: An exposed API key could allow unauthorized domain management.

Mitigation: Protect the AgentDomains API key and avoid logging or committing it.

Risk: Unpinned CLI or MCP installations can change unexpectedly.

Mitigation: Pin CLI or MCP package versions in controlled environments.

## Reference(s):

- [AgentDomains documentation](https://docs.agentdomains.co)
- [AgentDomains API documentation](https://docs.agentdomains.co#api)
- [AgentDomains MCP documentation](https://docs.agentdomains.co/#mcp)
- [AgentDomains ClawHub release](https://clawhub.ai/tashfeenahmed/skills/agentdomains)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown and shell commands; CLI responses can be JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can provide claimed hostnames, DNS changes, and setup or account-management steps.]

## Skill Version(s):

0.6.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
