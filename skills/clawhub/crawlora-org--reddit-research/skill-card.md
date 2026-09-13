## Description:

Researches public Reddit posts, comments, users, domains, trends, and keyword results through the Crawlora API and returns normalized JSON for agent analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to gather public Reddit context for community sentiment, thread summaries, user-history review, trend monitoring, brand mentions, and lead-discovery workflows through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Reddit search terms, usernames, domains, and related request parameters to Crawlora using the user's Crawlora API key.

Mitigation: Use only with queries and identifiers that are appropriate to share with Crawlora under the user's policy and account terms.

Risk: The /reddit/leads endpoint supports prospecting from public Reddit posts and may be inappropriate for some use policies.

Mitigation: Review organizational acceptable-use rules before using lead-generation workflows and limit use to permitted public-data research.

Risk: The skill accesses public Reddit content only, and endpoint results may omit or approximate some metrics.

Mitigation: Treat Reddit metrics as directional and avoid representing approximate engagement data as exact.

## Reference(s):

- [reddit-research endpoint reference](reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/reddit-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns normalized JSON from Crawlora's public Reddit endpoints.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
