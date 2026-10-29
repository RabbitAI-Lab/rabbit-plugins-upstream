## Description:

Search and read Groupon deals from the terminal via curl — the consumer GraphQL API (deal search/browse, deal detail, category taxonomy). Anonymous, no key or login. Use when asked to find Groupon deals, look up a specific deal, or browse a city's offers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search and browse public Groupon deals by city, retrieve deal details, and inspect category taxonomy from the terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and the chosen city are sent to Groupon.

Mitigation: Avoid including sensitive or personal information in search terms.

Risk: The documented examples invoke grpn, while the helper is named gp, so copied commands may fail.

Mitigation: Change the example invocations to gp before running them.

Risk: Persisted-query fingerprints may become stale after Groupon changes its frontend queries.

Mitigation: If the API returns PersistedQueryNotFound, recapture the matching public fingerprint and update the recipe.

## Reference(s):

- [Groupon GraphQL query recipes](references/graphql-queries.md)
- [Groupon consumer GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public deal data returned as JSON; no account credentials are required.]

## Skill Version(s):

1.1.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
