## Description:

Search and read Groupon deals from the terminal via curl using Groupon's consumer GraphQL API for deal search, deal detail, and category taxonomy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to browse Groupon offers, inspect deal details, and list Groupon categories from public deal data without account credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, city slugs, and deal identifiers are sent to Groupon when the curl examples are run.

Mitigation: Use the skill only for public deal browsing and avoid entering private account, payment, cookie, or other sensitive data.

Risk: Persisted-query hashes can become stale when Groupon changes frontend queries.

Mitigation: If Groupon returns PersistedQueryNotFound, recapture the public hash from a browser network request as described in the artifact.

Risk: Empty or non-JSON 2xx responses can indicate an interstitial challenge.

Mitigation: Check response content before parsing and retry rather than blindly JSON-parsing empty or HTML responses.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl requests, jq filters, Groupon city slugs, deal identifiers, and notes about stale persisted-query hashes.]

## Skill Version(s):

0.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
