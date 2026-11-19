## Description:

Manage Dub short links, track conversions, and read link attribution analytics through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing teams can use this skill to manage Dub short links, review attribution analytics, and track lead or sale conversions. It also supports connected-account tasks for customers, domains, and partner programs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with medium confidence, citing account-credit access and financial or partner administration beyond its stated link and analytics purpose.

Mitigation: Before installing, verify the API destination and review whether the account access and actions match the intended use. The scan is partial, so some local references could not be resolved.

Risk: The documented operations include destructive changes such as deleting links, customers, domains, or partner records.

Mitigation: Use only endpoints needed for the task and get explicit confirmation before deleting, overwriting, or sending anything on the user's behalf.

## Reference(s):

- [superagnt Dub Integration documentation](https://superagnt.com/r/ch-dub-links-docs)
- [Dub connection API](https://api.superagnt.com/v1/connections/dub)
- [superagnt MCP server](https://mcp.superagnt.com/mcp)
- [superagnt install instructions](https://www.superagnt.com/install)
- [Connect a Dub account](https://app.superagnt.com/dashboard/connections)
- [Get a superagnt API key](https://superagnt.com/r/ch-dub-links-key)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [JSON API responses and concise text summaries or instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions use the connected Dub account and may create, update, or delete records when requested.]

## Skill Version(s):

2.0.17 (source: frontmatter; ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
