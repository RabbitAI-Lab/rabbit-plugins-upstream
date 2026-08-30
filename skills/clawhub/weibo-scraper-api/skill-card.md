## Description:

Pull Weibo user profiles and posts, post comments, likes and reposts, keyword search across posts, videos, users, topics and images, the hot-search board, ranking boards, and channel feeds as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and analysts use this skill to retrieve Weibo profiles, posts, engagement data, keyword search results, hot-search entries, ranking boards, and channel feeds through Scavio API endpoints. It supports China-market social listening, trend monitoring, creator research, and structured-data workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weibo lookup targets, identifiers, and search terms are sent to Scavio's API.

Mitigation: Avoid using the skill for confidential investigations or sensitive personal data unless sharing those queries with Scavio is acceptable.

Risk: The skill requires SCAVIO_API_KEY for authenticated API calls.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and keep it out of source code.

Risk: Every Weibo endpoint call consumes Scavio credits, including empty results.

Mitigation: Validate required identifiers before calling endpoints and paginate only with cursors returned by previous responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/weibo-scraper-api)
- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=weibo-scraper-api)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with Python and shell examples for JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Weibo API calls consume Scavio credits and return structured JSON envelopes.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
