## Description:

Researches anime and manga titles through the Crawlora API, covering search, title details, characters, staff, recommendations, rankings, and airing schedules while returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up anime and manga titles, characters, staff, rankings, recommendations, and airing schedules through Crawlora and receive normalized JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper uses CRAWLORA_API_KEY for API requests.

Mitigation: Keep the key in the environment only and use a limited or replaceable key where possible.

Risk: CRAWLORA_API_BASE can redirect requests, including the API key, to another host.

Mitigation: Leave CRAWLORA_API_BASE unset unless the destination is fully trusted.

Risk: The helper can call broader Crawlora API paths than the documented anime and manga endpoints.

Mitigation: Run only the documented anime and manga commands for this skill.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/anime-manga-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; CRAWLORA_API_BASE can redirect requests and should remain unset unless trusted.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
