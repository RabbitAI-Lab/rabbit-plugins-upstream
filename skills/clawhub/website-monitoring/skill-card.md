## Description:

Creates and manages website-change monitors via the Crawlora API to watch a page for content changes or a sitemap for added and removed URLs, with signed webhook delivery when changes occur.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external users use this skill to create and manage Crawlora monitors for public webpages or sitemaps, then inspect check history or receive webhook notifications when content changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends public URLs, webhook URLs, and optional webhook secrets to the Crawlora service.

Mitigation: Install only when that service use is acceptable, keep CRAWLORA_API_KEY in the environment, and avoid hardcoding or committing credentials.

Risk: Create, update, and delete actions can change persistent monitors and scheduled checks may consume credits.

Mitigation: Confirm monitor IDs and requested changes before modifying or deleting monitors, and choose cadences that match the target change frequency.

Risk: Webhook payloads may be spoofed or replayed if signatures are not checked.

Mitigation: Verify the X-Crawlora-Signature HMAC with the configured webhook secret and reject stale timestamps before trusting deliveries.

## Reference(s):

- [Website Monitoring Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/website-monitoring)
- [Crawlora Publisher Profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora JSON API responses for monitor management and check-history workflows.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
