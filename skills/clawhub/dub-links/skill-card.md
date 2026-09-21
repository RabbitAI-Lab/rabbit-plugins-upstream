## Description:

Manage Dub short links, track conversions, and read link attribution analytics through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect agents to a Dub workspace through Superagnt, manage short links and related resources, track lead and sale conversions, and retrieve attribution analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or delete live marketing, customer, partner, and commission data in a connected Dub workspace.

Mitigation: Require the agent to restate the exact resources and obtain explicit approval before delete, bulk update, partner moderation, bounty, commission, or customer-data actions.

Risk: Conversion tracking and customer workflows may expose customer emails or metadata.

Mitigation: Minimize customer emails and metadata sent through tracking calls and review payloads before execution.

Risk: Using the skill grants agent access through the user's Superagnt API key and connected Dub credentials.

Mitigation: Install only when agent access to a live Dub workspace is intended, and keep SUPERAGNT_API_KEY scoped and protected.

## Reference(s):

- [Superagnt Dub documentation](https://superagnt.com/r/ch-dub-links-docs)
- [Superagnt MCP endpoint](https://mcp.superagnt.com/mcp)
- [Superagnt agent setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub listing](https://clawhub.ai/jaencarrodine/skills/dub-links)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with inline bash commands and JSON API schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and a connected Dub account.]

## Skill Version(s):

2.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
