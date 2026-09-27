## Description:

Helps agents search and read Groupon deals, deal details, and categories using public, unauthenticated requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can find deals in a city, inspect an individual deal's pricing and details, and browse Groupon categories without signing in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deal search terms are sent to Groupon.

Mitigation: Avoid sensitive personal information in search terms.

Risk: Public query fingerprints can become stale, interrupting deal lookups.

Mitigation: Refresh the fingerprint from a current Groupon request when a persisted query is not found; do not treat it as a credential.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon MCP skill on ClawHub](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands]

**Output Format:** [Markdown with deal summaries and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deal results depend on Groupon's current listings and public query availability.]

## Skill Version(s):

1.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
