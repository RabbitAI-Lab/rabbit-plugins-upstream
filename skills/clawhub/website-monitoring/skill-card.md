## Description:

Creates and manages website-change monitors via the Crawlora API to watch a page for content changes or a sitemap for added and removed URLs, with signed webhook notifications when changes occur.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business users use this skill to create, inspect, update, and delete Crawlora monitors for public web pages or sitemaps. It is useful for competitor pricing watches, new-page discovery, operational change alerts, and debugging monitor check history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends monitored public URLs, monitor settings, optional webhook details, and the Crawlora API key to Crawlora.

Mitigation: Install and run it only when this data sharing is acceptable, keep the API key in the CRAWLORA_API_KEY environment variable, and avoid hardcoding or committing credentials.

Risk: Create, update, pause, and delete actions can change server-side monitors, and created monitors continue running and consuming credits.

Mitigation: Confirm mutation requests before execution and review monitor cadence so ongoing checks match the user's intent and budget.

Risk: Webhook notifications can be spoofed or replayed if deliveries are trusted without validation.

Mitigation: Verify the X-Crawlora-Signature HMAC and reject stale timestamps before trusting webhook payloads.

Risk: The documentation advertises PATCH and DELETE monitor operations, but the bundled helper currently permits only GET and POST.

Mitigation: Treat update, pause, and delete workflows as requiring helper changes or direct API handling until the helper supports those HTTP methods.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/website-monitoring)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the CRAWLORA_API_KEY environment variable and returns normalized JSON from Crawlora API calls.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
