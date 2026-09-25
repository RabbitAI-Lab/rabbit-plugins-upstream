## Description:

Search and read Groupon deals from the terminal via curl -- the consumer GraphQL API for deal search, deal detail, and category taxonomy without a key or login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search public Groupon deals, inspect deal details, and browse Groupon category taxonomy from terminal-oriented workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Groupon searches, city slugs, and deal IDs are sent to Groupon when the curl recipes are used.

Mitigation: Use only for public deal lookup workflows where sending those query details to Groupon is acceptable.

Risk: Persisted GraphQL query hashes can become stale after Groupon frontend changes.

Mitigation: Refresh the public persisted-query hash from a Groupon browser request when the API returns PersistedQueryNotFound.

Risk: The skill provides read-only deal lookup recipes and does not cover authenticated purchases or account actions.

Mitigation: Do not use this skill for buying Groupons or handling account-specific workflows.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline bash, curl, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are read-only public deal data recipes; purchasing and account-specific actions are out of scope.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
