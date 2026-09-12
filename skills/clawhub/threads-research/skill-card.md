## Description:

Researches public Threads profiles, posts, replies, and search results via the Crawlora API, returning clean JSON for profile stats, post content, replies, recent posts, and keyword searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, marketers, researchers, and developers use this skill to inspect public Threads profiles, posts, replies, recent profile activity, and keyword search results through Crawlora instead of scraping Threads directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper uses a Crawlora API key and sends authenticated requests to Crawlora.

Mitigation: Set CRAWLORA_API_KEY only in trusted environments, avoid committing it, and review outgoing requests before regular use.

Risk: Security evidence says the authenticated helper is broader than the documented read-only Threads catalog.

Mitigation: Prefer documented Threads endpoints and have the publisher narrow the helper to GET-only, exact endpoint shapes before broad deployment.

Risk: The skill only retrieves public data exposed by Crawlora and some Threads result sets may be limited or lack continuation cursors.

Mitigation: Treat results as a bounded public snapshot and avoid representing first-page search results or incomplete reply pages as exhaustive coverage.

## Reference(s):

- [Threads endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/threads-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns only public Threads data exposed by the documented Crawlora endpoints.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
