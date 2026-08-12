## Description:

Researches Reddit via the Crawlora API: subreddit posts, comments, metadata, single post threads, keyword search, user history, domain-linked posts, and hot/new/rising/top trends returned as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agents use this skill to gather public Reddit posts, comments, user activity, domain mentions, and trends through Crawlora for community research, brand monitoring, sentiment review, and thread analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit research queries, identifiers, and API-key-authenticated requests are sent to Crawlora.

Mitigation: Use the skill only for non-confidential public Reddit research where transfer to Crawlora is acceptable.

Risk: The helper script can target paths beyond the stated Reddit-only purpose and supports an overridden API base URL.

Mitigation: Review calls before execution, keep CRAWLORA_API_BASE unset or pointed at the official Crawlora API, and prefer a Reddit-only allowlisted helper for stricter deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/reddit-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the CRAWLORA_API_KEY environment variable and public Reddit endpoint parameters.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
