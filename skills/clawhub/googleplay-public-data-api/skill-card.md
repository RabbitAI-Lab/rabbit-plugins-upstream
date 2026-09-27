## Description:

Query public Google Play app data through ReplyNodes' read-only API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app researchers use this skill to search for Android apps and inspect public listings, reviews, permissions, availability, and data safety through ReplyNodes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A ReplyNodes API key could be exposed in chat, logs, URLs, or reports.

Mitigation: Keep REPLYNODES_API_KEY in a secret store and send it only as an authorization header.

Risk: Unbounded batches or pagination can consume prepaid credits unexpectedly.

Mitigation: Check capability pricing before batches and set request and page limits.

Risk: Requests send app research queries to a third-party API provider.

Mitigation: Use only if ReplyNodes is an acceptable third-party provider for the intended work.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/replynodes-ai/skills/googleplay-public-data-api)
- [ReplyNodes developer portal](https://app.replynodes.com/developers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance and normalized JSON from API requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public app data; successful API responses include data and a request ID.]

## Skill Version(s):

1.1.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
