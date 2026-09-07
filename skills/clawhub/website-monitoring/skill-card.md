## Description:

Creates and manages website-change monitors via the Crawlora API to watch a page for content changes or a sitemap for added and removed URLs, with signed webhook delivery when changes occur.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and competitive intelligence teams use this skill to create, manage, and inspect Crawlora monitors for public pages or sitemaps. It helps them receive webhook notifications for page changes or added and removed sitemap URLs without building their own polling and diffing workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key to the URL configured by CRAWLORA_API_BASE.

Mitigation: Leave CRAWLORA_API_BASE unset unless intentionally using a trusted Crawlora-compatible endpoint.

Risk: The helper accepts broader Crawlora API paths than the documented website-monitoring workflow.

Mitigation: Use the documented monitor endpoints unless the operator deliberately chooses another Crawlora API route.

Risk: Webhook deliveries can be spoofed or replayed if the signature is not checked.

Mitigation: Verify the X-Crawlora-Signature HMAC and reject stale timestamps before trusting webhook payloads.

## Reference(s):

- [website-monitoring endpoint reference](artifact/reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/website-monitoring)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authentication and returns normalized JSON from Crawlora monitor endpoints.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
