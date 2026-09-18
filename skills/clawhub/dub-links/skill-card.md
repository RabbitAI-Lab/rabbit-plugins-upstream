## Description:

Manage Dub short links, track conversions, and read link attribution analytics through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect agents to a Dub workspace for short-link management, conversion tracking, attribution analytics, and partner-program operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected Dub workspace access can perform sensitive account, customer, partner, bounty, commission, and deletion operations.

Mitigation: Review authorization scopes, use least-privilege credentials where available, and require explicit user approval before destructive, moderation, bounty, commission, email, cookie, or metadata actions.

Risk: The security verdict is suspicious because the skill lacks enough built-in safety guidance for high-impact operations.

Mitigation: Install only when the publisher and superagnt connection are trusted, and review the skill and connected workspace permissions before deployment.

## Reference(s):

- [superagnt Dub documentation](https://superagnt.com/r/ch-dub-links-docs)
- [ClawHub skill listing](https://clawhub.ai/jaencarrodine/skills/dub-links)
- [MCP server endpoint](https://mcp.superagnt.com/mcp)
- [MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown with JSON schemas and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and a connected Dub account.]

## Skill Version(s):

2.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
