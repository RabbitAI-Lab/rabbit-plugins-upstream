## Description:

Researches anime and manga titles via the Crawlora API - search, title detail, characters, staff, recommendations, rankings, and airing schedules - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to look up anime and manga titles, cast, staff, recommendations, rankings, and airing schedules from Crawlora as normalized JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send authenticated Crawlora requests beyond the anime and manga purpose described by the skill.

Mitigation: Review commands before execution, keep CRAWLORA_API_KEY private, avoid sensitive query terms, and restrict use to the documented /anime and /manga GET endpoints.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/anime-manga-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora requests; list endpoints are paginated.]

## Skill Version(s):

1.0.1 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
