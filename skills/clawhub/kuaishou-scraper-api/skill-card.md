## Description:

Read Kuaishou (China) profiles, posts, live status, videos, comment threads, hashtag feeds, leaderboards and four kinds of search as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and social-listening teams use this skill to query public Kuaishou China creator, video, comment, hashtag, search, live, and leaderboard data through Scavio's API. It is suited for agent workflows that need structured JSON from Kuaishou while tracking endpoint-specific credit costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calls require a Scavio API key and may spend paid credits, especially search and batch endpoints.

Mitigation: Store SCAVIO_API_KEY as a secret, review endpoint costs before calling, and avoid unnecessary multi-page searches or broad fan-out.

Risk: Queries send Kuaishou links, user IDs, keywords, or hashtags to Scavio.

Mitigation: Use the skill only for appropriate public Kuaishou China data and assess whether sharing each query with Scavio fits the use case.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/kuaishou-scraper-api)
- [Scavio Kuaishou profile documentation](https://scavio.dev/docs/kuaishou-profile)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell and code examples; API calls return structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses disclose credits used and remaining.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
