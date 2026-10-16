## Description:

Helps agents search and read public Groupon deals, deal details, and categories using terminal commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers can search city deals, inspect deal prices and details, and browse Groupon categories without an account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and city or deal identifiers are sent to Groupon.

Mitigation: Use only queries and identifiers you are comfortable sharing with Groupon.

Risk: Adding cookies, login tokens, or account data extends the documented public-read scope.

Mitigation: Keep requests anonymous; do not add credentials or personal account data to the examples.

Risk: Groupon query fingerprints may expire or responses may be non-JSON.

Mitigation: Check responses before parsing, and refresh stale public query fingerprints as documented.

## Reference(s):

- [Groupon MCP skill release](https://clawhub.ai/chrischall/skills/groupon-mcp)
- [Groupon curl recipes](references/graphql-queries.md)

## Skill Output:

**Output Type(s):** [Shell commands, Text, JSON]

**Output Format:** [Terminal commands and human-readable deal summaries; Groupon responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public-read deal search, deal details, and categories; no purchase capability.]

## Skill Version(s):

1.1.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
