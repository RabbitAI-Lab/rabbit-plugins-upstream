## Description:

Search and read Groupon deals from the terminal via curl - the consumer GraphQL API for deal search, deal detail, and category taxonomy, with no key or login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Groupon offers, fetch specific deal details, and inspect category taxonomy from the terminal using read-only curl and jq recipes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls an unofficial Groupon GraphQL endpoint, and persisted-query hashes may stop working if Groupon changes its frontend queries.

Mitigation: Treat failures such as PersistedQueryNotFound as drift; re-capture public persisted-query hashes as documented and review requests against Groupon's site rules.

Risk: Adding cookies, account credentials, or purchasing workflows would change the security posture beyond the reviewed read-only behavior.

Mitigation: Keep usage anonymous and read-only unless credentialed or purchasing behavior receives separate review.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon consumer GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash, curl, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes for public Groupon deal search, deal detail, and category taxonomy.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
