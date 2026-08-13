## Description:

Search and read Groupon deals from the terminal via curl using Groupon's consumer GraphQL API for deal search, deal detail, and category taxonomy, anonymously without a key or login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping assistants use this skill to search, browse, and inspect public Groupon deal data from an agent terminal without account credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-chosen searches, city slugs, and deal IDs are sent to Groupon's public GraphQL endpoint.

Mitigation: Avoid submitting sensitive or private search terms, and disclose that Groupon receives lookup details.

Risk: Stored persisted-query hashes and Groupon's public API behavior may change.

Mitigation: Handle non-JSON responses and PersistedQueryNotFound errors, then recapture public query hashes from Groupon network requests when needed.

Risk: The skill is intended for read-only deal lookup and does not perform purchases or authenticated account actions.

Mitigation: Do not provide Groupon credentials or use the skill as a purchase workflow; keep purchase decisions in Groupon's authenticated web experience.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon public GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl requests to Groupon's public GraphQL endpoint and jq filters for compact deal output.]

## Skill Version(s):

0.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
