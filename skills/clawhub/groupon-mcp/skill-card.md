## Description:

Helps agents search Groupon deals, inspect deal details, and browse categories using public, read-only requests without an account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents looking for local offers can search deals by city and keyword, review prices and deal details, or browse categories before deciding what to explore further.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, city slugs, and deal IDs are sent to Groupon when looking up offers.

Mitigation: Avoid sensitive searches if disclosing those details to Groupon is a concern.

## Reference(s):

- [Groupon MCP on ClawHub](https://clawhub.ai/chrischall/skills/groupon-mcp)
- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon consumer API](https://www.groupon.com/mobilenextapi/graphql)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Deal summaries, links, and optional curl and jq commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deal prices and availability may change; deal lookup does not purchase offers.]

## Skill Version(s):

1.1.2

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
