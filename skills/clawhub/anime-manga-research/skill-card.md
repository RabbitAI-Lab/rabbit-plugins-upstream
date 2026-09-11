## Description:

Researches anime and manga titles via the Crawlora API -- search, title detail, characters, staff, recommendations, rankings, and airing schedules -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up anime and manga titles, casts, staff, rankings, schedules, and recommendations through Crawlora and receive normalized JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Anime and manga lookup queries and the Crawlora API key are sent to Crawlora.

Mitigation: Install only if this data sharing is acceptable; keep the key in CRAWLORA_API_KEY and do not hardcode, pass, or commit it elsewhere.

Risk: The security verdict flags the helper for review before broad trust because authenticated POST behavior and path validation may exceed the intended lookup scope.

Mitigation: Review before installation, restrict use to documented anime and manga endpoints, and tighten the helper to GET-only exact route validation before broad deployment.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/anime-manga-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON responses and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and may return paginated public anime and manga data.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
