## Description:

Search and read Groupon deals from the terminal via curl against Groupon's consumer GraphQL API, including deal search, deal detail, and category taxonomy without requiring an account, key, or login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Groupon deal searches, deal details, and category browsing while receiving curl and jq guidance for public read-only lookup requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deal searches send query terms, city slugs, and deal IDs to Groupon.

Mitigation: Use only public lookup inputs and do not add cookies, account credentials, or other sensitive data to the curl examples unless intentionally moving beyond the read-only public lookup use case.

Risk: Groupon may return challenge interstitials, non-JSON responses, or stale persisted-query errors.

Mitigation: Check responses before parsing and refresh public persisted-query hashes from browser Network evidence when PersistedQueryNotFound occurs.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [Groupon consumer GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with inline bash, JSON, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only curl recipes and parsing guidance for public Groupon deal lookup responses.]

## Skill Version(s):

0.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
