## Description:

Helps agents search Groupon deals, browse city offers and categories, and read deal details without an account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can find Groupon offers by city or search term, inspect a deal's prices and conditions, and browse categories before deciding what to explore further.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deal searches are sent to Groupon.

Mitigation: Avoid including sensitive information in search terms and use the skill only when this disclosure is acceptable.

Risk: Deal prices, availability, and conditions can change after a lookup.

Mitigation: Confirm the current listing and fine print before making a purchase decision.

## Reference(s):

- [Groupon MCP on ClawHub](https://clawhub.ai/chrischall/skills/groupon-mcp)
- [Groupon query recipes](references/graphql-queries.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with deal summaries and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only deal lookups; no purchase or account changes.]

## Skill Version(s):

1.1.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
