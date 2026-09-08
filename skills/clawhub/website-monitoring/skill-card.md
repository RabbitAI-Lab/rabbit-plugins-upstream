## Description:

Creates and manages website-change monitors via the Crawlora API to watch a page for content changes or a sitemap for added and removed URLs, with signed webhook delivery when changes are detected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and teams responsible for website monitoring use this skill to create, inspect, pause, update, and delete Crawlora monitors for public pages or sitemaps. It is suited for competitor pricing watches, new-page discovery, and webhook-based change alerts without building a separate polling and diffing pipeline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can use the Crawlora API key for broader arbitrary Crawlora requests and can be redirected through an API-base override.

Mitigation: Avoid setting CRAWLORA_API_BASE, use a dedicated or least-privileged Crawlora key when available, and review API calls before execution.

Risk: The skill can create, update, pause, and delete website monitors tied to the user's Crawlora account.

Mitigation: Require explicit confirmation before update or delete operations, and verify monitor IDs and target URLs before running commands.

Risk: Webhook notifications should not be trusted without validation.

Mitigation: Configure a webhook secret, verify the X-Crawlora-Signature HMAC, and reject stale timestamps before acting on a delivery.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/website-monitoring)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; monitor operations call the Crawlora API and return normalized JSON.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
