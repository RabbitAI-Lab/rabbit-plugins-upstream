## Description:

Creates and manages website-change monitors via the Crawlora API: watch a page for a content change or a sitemap for added or removed URLs, and get a signed webhook when something changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to create, list, update, delete, and inspect website-change monitors for public pages and sitemaps. It is suited for tracking page changes, new or removed sitemap URLs, webhook delivery status, and monitor health without building a separate polling and diffing pipeline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora API key exposure or misuse.

Mitigation: Provide the key through CRAWLORA_API_KEY, avoid hardcoding or committing it, and review commands before execution.

Risk: Unintended monitor deletion or changes that reset a monitor baseline.

Mitigation: Review DELETE and PATCH requests before execution, especially changes to target_type or sitemap configuration.

Risk: Monitoring URLs or sending webhooks without proper authorization.

Mitigation: Use the skill only for public URLs and webhook destinations you are authorized to monitor or operate.

Risk: Trusting forged or replayed webhook deliveries.

Mitigation: Verify the X-Crawlora-Signature HMAC and reject stale timestamps before trusting webhook payloads.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the CRAWLORA_API_KEY environment variable and documented Crawlora monitor endpoints.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
