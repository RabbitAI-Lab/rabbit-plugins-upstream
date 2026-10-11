## Description:

Helps agents search Groupon deals by city, inspect deal details, and browse categories using public, unauthenticated requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents looking for Groupon offers can search a city's deals, check individual offers, and browse available categories without signing in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, city slugs, and deal IDs are sent to Groupon when the agent queries offers.

Mitigation: Avoid including sensitive information in searches; do not add cookies, login sessions, or payment data to requests.

## Reference(s):

- [Groupon MCP release on ClawHub](https://clawhub.ai/chrischall/skills/groupon-mcp)
- [Groupon curl recipes](artifact/references/graphql-queries.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and deal summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only deal lookups; responses from Groupon are JSON.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
