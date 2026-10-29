## Description:

Twitter API helps agents fetch read-only Twitter/X data from fetcher.sh for searches, profiles, timelines, followers, lists, trends, and tweet lookups through paid HTTP or MCP endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Twitter/X public data for search, profile lookup, timeline analysis, list inspection, trend checks, competitor monitoring, hashtag tracking, and follower export workflows without using the official X API application process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitter/X searches, account identifiers, tweet IDs, list IDs, and related metadata are sent to the external twitter.fetcher.sh service.

Mitigation: Use a scoped Fetcher key and avoid confidential investigations or regulated data unless the workflow has been approved.

Risk: Paid API and MCP actions can spend prepaid credits or trigger per-call x402 payments.

Mitigation: Set budget and agent controls around paid actions, especially credit top-up and fetch operations.

Risk: The artifact notes that upstream failures may still be billed after payment settlement.

Mitigation: Use small test calls before larger jobs and design workflows to handle failed or incomplete upstream responses.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fetcher-sh/skills/twitter-api)
- [Publisher Profile](https://clawhub.ai/user/fetcher-sh)
- [Server-Resolved GitHub Source](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/twitter-api)
- [Endpoint Reference](references/endpoints.md)
- [Usage Scenarios](references/scenarios.md)
- [FAQ](references/faq.md)
- [Comparison Guide](references/comparison.md)
- [OpenAPI Contract](https://twitter.fetcher.sh/openapi.json)
- [Condensed Catalog](https://twitter.fetcher.sh/llms.txt)
- [Service Site](https://twitter.fetcher.sh)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with HTTP endpoint guidance, curl commands, and JSON MCP configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only API usage; responses are described as JSON envelopes from the external service]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
