## Description:

Researches Reddit via the Crawlora API, including subreddit posts and comments, individual post discussions, keyword search, public user history, domain-linked posts, and hot, new, rising, or top trends, returning normalized JSON instead of scraping Reddit directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to research public Reddit conversations, monitor brand or competitor mentions, inspect discussion threads, review public user activity, and identify trending subreddit topics through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit research inputs, usage patterns, and the user's Crawlora API key are sent to Crawlora when the helper calls the API.

Mitigation: Use an approved Crawlora account and avoid submitting secrets, confidential investigation terms, or sensitive personal data as search terms, usernames, domains, or post identifiers.

Risk: The skill includes a Reddit buying-intent leads endpoint in addition to general research and sentiment workflows.

Mitigation: Review policy, consent, and outreach requirements before using lead-scoring outputs for prospecting, profiling, or contact decisions.

Risk: Reddit engagement metrics and anonymous-page data can be approximate, omitted, rate-limited, or limited to an initial subset of large threads.

Mitigation: Treat engagement figures as directional, cite the endpoint limitations, follow pagination cursors, and retry 503 responses according to Retry-After.

Risk: API credentials can be exposed if copied into prompts, command histories, repositories, or query strings.

Mitigation: Keep the key in CRAWLORA_API_KEY, do not hardcode or commit it, and rely on the helper's credential-safe curl configuration.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/reddit-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; helper supports documented GET routes only; list responses are cursor-paginated and default to limited result counts.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
