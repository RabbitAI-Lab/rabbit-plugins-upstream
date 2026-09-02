## Description:

Get and manage a free public domain (yourname.makes.fyi or yourname.agentdomains.co) for an AI agent or app using the AgentDomains CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tashfeenahmed](https://clawhub.ai/user/tashfeenahmed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when they need a public hostname for a website, API, webhook, callback, reverse proxy, redirect, DNS record, ACME challenge, or nameserver delegation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to create or store an AgentDomains API key.

Mitigation: Use an existing AGENTDOMAINS_API_KEY when possible and treat stored API keys as credentials.

Risk: DNS, forwarding, proxy, delete, and account closure commands can change public hostnames or remove access.

Mitigation: Review the intended hostname, record, forwarding, proxy, deletion, and account commands before execution.

Risk: Provisional accounts and names can be deleted if the required email confirmation is not completed within 30 days.

Mitigation: Confirm the account email link within the documented 30-day window for names that should remain permanent.

## Reference(s):

- [AgentDomains Documentation](https://docs.agentdomains.co)
- [AgentDomains API Documentation](https://docs.agentdomains.co#api)
- [AgentDomains MCP Documentation](https://docs.agentdomains.co/#mcp)
- [AgentDomains Service](https://agentdomains.co)
- [AgentDomains CLI Releases](https://github.com/tashfeenahmed/AgentDomains/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON-oriented CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include DNS, forwarding, proxy, account, MCP, and API-key environment variable instructions.]

## Skill Version(s):

0.5.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
