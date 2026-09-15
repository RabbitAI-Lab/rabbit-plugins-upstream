## Description:

Search and read Groupon deals from the terminal via curl using Groupon's consumer GraphQL API for deal search, deal detail, and category taxonomy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Groupon deal searches, individual deal details, or category browsing and receive ready-to-run curl and jq guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, city slugs, and deal IDs are sent to Groupon's consumer GraphQL endpoint.

Mitigation: Use only non-sensitive search inputs and review generated curl commands before running them.

Risk: Adding cookies or account credentials to the examples could expose account data outside the documented anonymous workflow.

Mitigation: Run the provided examples without cookies, account credentials, or authenticated purchase flows unless that separate workflow has been reviewed and trusted.

Risk: Persisted GraphQL query hashes can become stale when Groupon changes its frontend queries.

Mitigation: If Groupon returns PersistedQueryNotFound, refresh the public persisted-query hash using the artifact's documented browser Network workflow.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon consumer GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces terminal-oriented instructions for anonymous public deal reads; no credentials are required by the artifact.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
