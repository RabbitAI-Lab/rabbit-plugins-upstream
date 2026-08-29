## Description:

Search and read Groupon deals from the terminal via curl -- the consumer GraphQL API (deal search/browse, deal detail, category taxonomy). Anonymous, no key or login. Use when asked to find Groupon deals, look up a specific deal, or browse a city's offers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Groupon deals, inspect deal details, and browse Groupon category taxonomy using public read-only curl recipes. It is useful when a user asks for Groupon offers by city, query, category, or deal permalink slug.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on public, undocumented Groupon persisted-query hashes that may become stale.

Mitigation: Refresh stale hashes from browser DevTools when Groupon returns PersistedQueryNotFound, following the artifact's recapture steps.

Risk: Groupon may return an empty or non-JSON challenge response even when the HTTP status is 2xx.

Mitigation: Check that responses are valid JSON before parsing and retry when a challenge interstitial is returned.

Risk: The skill makes unauthenticated read-only requests to Groupon's public deal endpoint.

Mitigation: Install only when this access pattern is acceptable; the skill does not use credentials, accounts, purchases, persistence, or local data.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with curl, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes for public Groupon deal data; no account, key, cookie, purchase flow, persistence, or local data access is requested.]

## Skill Version(s):

0.1.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
