## Description:

Researches anime and manga titles via the Crawlora API: search, title detail, characters, staff, recommendations, rankings, and airing schedules, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to look up anime and manga titles, cast and staff, similar works, rankings, and airing schedules from Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call paths beyond the documented anime and manga endpoints.

Mitigation: Restrict operational use to documented /anime and /manga paths, and review shell commands before execution.

Risk: The skill requires a Crawlora API key in the agent environment.

Mitigation: Provide the key only through CRAWLORA_API_KEY, avoid hardcoding or committing it, and rotate it if exposed.

Risk: The helper supports arbitrary POST bodies and an overrideable API base URL.

Mitigation: Disable or review non-GET calls and CRAWLORA_API_BASE overrides unless they are explicitly required.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill listing](https://clawhub.ai/tonywangcn/skills/anime-manga-research)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON API responses with Markdown setup notes and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for API calls; list endpoints are paginated.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
