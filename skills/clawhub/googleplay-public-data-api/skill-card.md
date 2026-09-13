## Description:

Query Google Play app data through a read-only API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Android app data from ReplyNodes, including app details, search results, permissions, reviews, categories, availability, and data safety. It is intended for read-only app research workflows, not publishing, private account access, or catalog enumeration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ReplyNodes API keys can be exposed if pasted into chat, reports, logs, URLs, screenshots, or source files.

Mitigation: Store REPLYNODES_API_KEY in a secret store or environment variable, send it only as an Authorization bearer token, and remove authorization headers from shared outputs.

Risk: Batches, pagination, or repeated requests can consume prepaid ReplyNodes credits.

Mitigation: Check the capabilities endpoint before use, confirm advertised costs, and apply caller-side limits for batches and pagination.

Risk: Provider failures, timeouts, or changing public store data can lead to incomplete or stale results.

Mitigation: Report provider errors without fabricating data, preserve request IDs and capture times, and treat null fields as unknown.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/replynodes-ai/skills/googleplay-public-data-api)
- [ReplyNodes Publisher Profile](https://clawhub.ai/user/replynodes-ai)
- [ReplyNodes API Gateway](https://api.replynodes.com)
- [ReplyNodes Developer Console](https://app.replynodes.com/developers)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline bash examples and JSON response handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only GET request guidance and normalized JSON interpretation; does not output credentials.]

## Skill Version(s):

1.1.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
