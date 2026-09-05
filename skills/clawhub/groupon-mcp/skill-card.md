## Description:

Groupon MCP helps agents search and read Groupon deals from the terminal via curl using Groupon's consumer GraphQL API for deal search, deal detail, and category taxonomy without a key or login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Groupon offers, inspect deal details, and browse Groupon category taxonomy from terminal workflows without account credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Groupon search terms, city/location slugs, and deal IDs are sent to Groupon when the generated curl commands are run.

Mitigation: Use only search and deal inputs you are comfortable sending to Groupon's public API.

Risk: Adding cookies, account tokens, or personal data to the provided commands could expose sensitive information.

Mitigation: Run the commands without cookies, account tokens, or personal data; when refreshing a stale persisted query, copy only the public persisted-query hash.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon consumer GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command examples call Groupon public deal APIs and typically return JSON for downstream filtering.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
