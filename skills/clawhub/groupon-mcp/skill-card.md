## Description:

Helps agents search and read public Groupon deals, deal details, and categories using terminal commands without an account or API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to find Groupon offers by city or search term, inspect deal details, and browse deal categories without making purchases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, city slugs, and deal identifiers are sent to Groupon.

Mitigation: Avoid sensitive queries and share only the information needed for the lookup.

Risk: Persisted queries may become stale or responses may be replaced by a challenge page.

Mitigation: Check responses before parsing and refresh the documented query fingerprints if Groupon reports they are unavailable.

## Reference(s):

- [Groupon MCP on ClawHub](https://clawhub.ai/chrischall/skills/groupon-mcp)
- [Groupon curl recipes](artifact/references/graphql-queries.md)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown with shell commands and deal summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public deal information; no purchase or account actions.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
