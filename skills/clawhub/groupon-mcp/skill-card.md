## Description:

Search and read Groupon deals from the terminal via curl using Groupon's consumer GraphQL API for deal search, deal detail, and category taxonomy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to search Groupon offers by city, inspect deal details, and retrieve category taxonomy without adding account credentials or API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Groupon can receive the search terms, city slugs, and deal IDs used in lookups.

Mitigation: Use the skill only when sharing those lookup parameters with Groupon is acceptable.

Risk: Adding cookies, account tokens, or payment data to the curl recipes could expose sensitive information.

Mitigation: Keep requests anonymous and do not add cookies, account tokens, or payment data.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon consumer GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, configuration]

**Output Format:** [Markdown with curl, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces public deal lookup guidance and command recipes; it does not install code, request credentials, or persist data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
