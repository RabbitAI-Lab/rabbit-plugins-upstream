## Description:

Researches anime and manga titles via the Crawlora API: search, title detail, characters, staff, recommendations, rankings, and airing schedules, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to retrieve normalized anime and manga data for title lookups, cast and staff details, recommendations, rankings, and airing schedules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call endpoints beyond the anime and manga paths described by the skill.

Mitigation: Review or patch scripts/crawlora.sh to restrict requests to approved anime and manga endpoints before deployment.

Risk: The Crawlora API key can be sent to a custom API base URL if CRAWLORA_API_BASE is set.

Mitigation: Do not set CRAWLORA_API_BASE unless the destination is trusted, and keep CRAWLORA_API_KEY out of code, logs, and committed files.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/anime-manga-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY for helper-script API calls.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
