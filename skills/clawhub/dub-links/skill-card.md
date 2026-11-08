## Description:

Manage Dub short links, track conversions, and read link attribution analytics through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing or affiliate operators use the skill to manage Dub links, track lead and sale conversions, and review attribution analytics from their connected Dub workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Dub account can be used to change commissions, approve rewards, ban partners, and create, update, or delete records.

Mitigation: Use only the endpoints needed for the user's request, confirm exact targets and amounts, and obtain explicit confirmation before destructive or outbound actions.

Risk: The skill requires an API key to access the connected account.

Mitigation: Supply the key through SUPERAGNT_API_KEY in the environment rather than placing it directly in commands or messages.

Risk: The hosted services' behavior was not verified in the artifact review, and the curl examples contain HTML-escaped quotes.

Mitigation: Verify the service behavior before connecting an account and correct the escaped curl examples before running them.

## Reference(s):

- [Documentation](https://superagnt.com/r/ch-dub-links-docs)
- [MCP server](https://mcp.superagnt.com/mcp)
- [Client installation guide](https://www.superagnt.com/install)
- [Dub connections page](https://app.superagnt.com/dashboard/connections)
- [API keys](https://superagnt.com/r/ch-dub-links-key)
- [ClawHub release](https://clawhub.ai/superagnt/skills/dub-links)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON data, Guidance]

**Output Format:** [Markdown instructions with curl examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected Dub account and SUPERAGNT_API_KEY.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
