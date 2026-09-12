## Description:

Researches public X (formerly Twitter) profiles, recent posts, and individual post details through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to retrieve public X profile stats, recent profile posts, and single-post content and engagement without browser automation or official X API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authenticated Crawlora helper may allow broader requests than the documented X lookup routes.

Mitigation: Review before installing and constrain use to documented GET-only X routes with validated parameters.

Risk: The skill requires a Crawlora API key for authenticated requests.

Mitigation: Keep the key in CRAWLORA_API_KEY, avoid hardcoding or committing it, and rotate it if exposure is suspected.

## Reference(s):

- [x-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; public X data only; profile posts are limited to first-page results.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
