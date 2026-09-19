## Description:

Search and read public Groupon deal data from the terminal with curl, including deal search, deal details, and category taxonomy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Groupon offers, inspect a specific deal, or browse category data through documented curl and jq recipes for Groupon's public consumer GraphQL endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and deal IDs requested through the skill are sent to Groupon.

Mitigation: Use the skill only for deal lookups that are appropriate to send to Groupon's public consumer endpoint.

Risk: Persisted-query hashes may become stale after Groupon changes its frontend queries.

Mitigation: Refresh only the public persisted-query hash from browser DevTools and avoid copying cookies, authorization headers, or other session data.

Risk: Empty or non-JSON responses can occur when Groupon returns a challenge interstitial.

Mitigation: Check response content before parsing JSON and retry rather than blindly parsing empty or HTML responses.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon consumer GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API Calls]

**Output Format:** [Markdown guidance with bash curl and jq snippets; Groupon API responses are JSON arrays.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No credentials are required; persisted-query hashes may need to be refreshed if Groupon changes them.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
