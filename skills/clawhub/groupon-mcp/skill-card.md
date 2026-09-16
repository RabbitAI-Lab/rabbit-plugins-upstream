## Description:

Search and read Groupon deals from the terminal via curl using Groupon's consumer GraphQL API for deal search, deal detail, and category taxonomy without an API key or login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to find Groupon deals, inspect deal details, and browse city or category offers through public Groupon API requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Groupon search terms, city slugs, and deal IDs are sent to Groupon's public API.

Mitigation: Use only non-sensitive lookup inputs and do not add cookies, account tokens, payment data, or session data unless intentionally building a separate authenticated integration.

Risk: Persisted-query hashes or challenge responses can cause empty, non-JSON, or PersistedQueryNotFound responses.

Mitigation: Check that responses are valid JSON before parsing and refresh public persisted-query hashes from Groupon browser traffic when the documented hashes become stale.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon consumer GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces public Groupon lookup guidance and command recipes; no credentials are required.]

## Skill Version(s):

0.3.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
