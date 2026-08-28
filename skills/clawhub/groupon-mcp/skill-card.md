## Description:

Search and read Groupon deals from the terminal via curl using Groupon's consumer GraphQL API for deal search, deal detail, and category taxonomy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Groupon offers, inspect a specific deal, or browse city and category deal data through anonymous curl requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, city slugs, and requested deal IDs are sent to Groupon when using the curl examples.

Mitigation: Avoid entering sensitive personal information in search queries or deal identifiers.

Risk: Adding cookies, account tokens, or browser headers while adapting examples could expose account-linked data.

Mitigation: Use the anonymous headers shown by the skill and do not add cookies, account tokens, or captured browser headers.

Risk: Persisted-query hashes can become stale and cause lookup failures.

Mitigation: If Groupon returns PersistedQueryNotFound, re-capture only the public persisted-query hash as described by the skill.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon consumer GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown]

**Output Format:** [Markdown with inline bash and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only lookup guidance and command examples; API responses are JSON arrays from Groupon.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
