## Description:

A TikTok API alternative on fetcher.sh that helps agents retrieve read-only TikTok data by keyword, post, profile, follower or following list, hashtag, sound, location, comments, or replies through paid GET endpoints without TikTok login or app review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to select and call fetcher.sh TikTok REST or MCP endpoints for social listening, trend tracking, influencer discovery, competitor analysis, and TikTok data pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Follower lists, followings, comments, replies, and location-tagged posts can contain sensitive personal or social data.

Mitigation: Use the API only for lawful, platform-compliant purposes, minimize collection, and avoid surveillance or targeting workflows.

Risk: Bearer-key and x402 usage can incur per-call costs.

Mitigation: Monitor paid calls, set usage budgets, and test narrow queries before running broad collection workflows.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/tiktok-api)
- [ClawHub skill page](https://clawhub.ai/fetcher-sh/skills/tiktok-api)
- [TikTok endpoint reference](artifact/references/endpoints.md)
- [TikTok scenario cookbook](artifact/references/scenarios.md)
- [TikTok API FAQ](artifact/references/faq.md)
- [TikTok data access comparison](artifact/references/comparison.md)
- [Full agent setup](https://tiktok.fetcher.sh/skill.md)
- [OpenAPI 3.1 contract](https://tiktok.fetcher.sh/openapi.json)
- [Condensed endpoint catalog](https://tiktok.fetcher.sh/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with endpoint tables, curl examples, and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only guidance for paid TikTok data retrieval; responses from the referenced service use JSON envelopes.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
