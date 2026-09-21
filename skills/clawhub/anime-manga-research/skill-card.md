## Description:

Researches anime and manga titles via the Crawlora API - search, title detail, characters, staff, recommendations, rankings, and airing schedules - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to look up public anime and manga title details, characters, staff, recommendations, rankings, and airing schedules through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Anime and manga lookup queries and the Crawlora API key are sent to Crawlora.

Mitigation: Install only when that data sharing is acceptable, keep the key in the environment, and avoid sharing logs that may contain sensitive request details.

Risk: Undocumented or unrelated Crawlora routes could broaden the skill's behavior beyond the reviewed lookup use case.

Mitigation: Use the bundled helper for the documented public-data lookup routes and review proposed commands before execution.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented GET-only Crawlora routes.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
