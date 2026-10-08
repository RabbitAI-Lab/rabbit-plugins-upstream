## Description:

Helps agents search Groupon deals, inspect deal details, and browse categories using public, unauthenticated requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can find local Groupon offers, compare deal details and prices, and browse available categories without signing in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deal search parameters are sent to Groupon when running the examples.

Mitigation: Share only intended search terms and locations; do not add cookies, sessions, or secrets to requests.

Risk: Groupon may change query fingerprints or return a challenge instead of deal data.

Mitigation: Check responses before using results and refresh outdated public query fingerprints when needed.

## Reference(s):

- [Groupon MCP on ClawHub](https://clawhub.ai/chrischall/skills/groupon-mcp)
- [Groupon curl recipes](references/graphql-queries.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with curl and jq examples or concise deal summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deal results and prices depend on Groupon's current data.]

## Skill Version(s):

1.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
