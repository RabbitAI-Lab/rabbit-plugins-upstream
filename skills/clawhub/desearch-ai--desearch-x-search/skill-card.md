## Description:

Search X (Twitter) posts by keyword, user or hashtag. Get a user's timeline, replies, retweeters or trending topics by location, or fetch specific posts by ID or URL. Supports advanced filters like date range, language, engagement thresholds, and media type.

This skill is ready for commercial/non-commercial use.

## Publisher:

[desearch-ai](https://clawhub.ai/user/desearch-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts can use the skill to search and retrieve X posts, timelines, replies, retweeters, and location-based trends, then inspect the returned text or structured data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, account identifiers, post IDs or URLs, filters, and the DESEARCH_API_KEY are sent to Desearch when a command runs.

Mitigation: Submit only information authorized for Desearch, keep confidential data out of search inputs, and protect the API key in the runtime environment.

Risk: The security scan had partial coverage because two local references were unresolved.

Mitigation: Review the supplied skill and its dependencies before installation, and interpret the benign verdict within the available scan coverage.

## Reference(s):

- [Desearch](https://desearch.ai)
- [Desearch API Reference](https://desearch.ai/docs/api-reference)
- [Desearch Console](https://console.desearch.ai)
- [OpenClaw Tool Policy](https://docs.openclaw.ai/tools)
- [OpenClaw Exec Controls](https://docs.openclaw.ai/tools/exec)
- [ClawHub Release](https://clawhub.ai/desearch-ai/skills/desearch-x-search)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text or JSON printed to stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tweet-format commands show up to 20 results and truncate post text to 280 characters; retweeter and trend commands return JSON.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
