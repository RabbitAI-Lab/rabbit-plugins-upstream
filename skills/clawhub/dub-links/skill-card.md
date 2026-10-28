## Description:

Manage Dub short links, track conversions, and read link attribution analytics through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing teams use this skill to manage short links, track lead and sale conversions, and review link attribution analytics in a connected Dub workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account can perform destructive or outbound actions, including deletions, partner bans, and reward or commission changes.

Mitigation: Use only the endpoints needed for the task and require explicit user confirmation before destructive or outbound changes.

Risk: The integration uses a Superagnt API key to access the user's connected Dub workspace.

Mitigation: Keep the key in SUPERAGNT_API_KEY and limit account permissions where available.

Risk: The documented shell examples may need correction before execution.

Mitigation: Review and correct the shell examples before running them.

## Reference(s):

- [Dub Integration documentation](https://superagnt.com/r/ch-dub-links-docs)
- [MCP server](https://mcp.superagnt.com/mcp)
- [Client installation instructions](https://www.superagnt.com/install)
- [Superagnt API key setup](https://superagnt.com/r/ch-dub-links-key)
- [Dub account connections](https://app.superagnt.com/dashboard/connections)
- [ClawHub release](https://clawhub.ai/superagnt/skills/dub-links)

## Skill Output:

**Output Type(s):** [API calls, JSON, Shell commands]

**Output Format:** [JSON API responses and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the connected Dub workspace and requested operation.]

## Skill Version(s):

2.0.10 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
