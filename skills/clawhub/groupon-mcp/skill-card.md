## Description:

Search and read Groupon deals from the terminal via curl -- the consumer GraphQL API (deal search/browse, deal detail, category taxonomy).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Groupon deals, inspect deal details, and browse category taxonomy through public curl-based GraphQL requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Groupon searches, city slugs, and deal IDs are sent to Groupon's API.

Mitigation: Use only public deal lookup terms and avoid private account, payment, cookie, or token data in requests.

Risk: Persisted GraphQL query hashes can become stale and cause request failures.

Mitigation: Refresh only the public persisted-query fingerprint from a matching Groupon browser request when PersistedQueryNotFound occurs.

Risk: Challenge interstitials or empty non-JSON responses can be returned by the upstream service.

Mitigation: Check response shape before parsing JSON and retry rather than blindly parsing empty or HTML responses.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code]

**Output Format:** [Markdown with curl and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces public Groupon API request examples and parsing guidance; it does not provide credentials or persist data.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
