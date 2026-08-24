## Description:

Website Monitoring creates and manages Crawlora website-change monitors for page-content and sitemap changes with optional signed webhook notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to create, inspect, update, pause, and delete Crawlora monitors that watch public pages or sitemaps for changes. It is useful for competitor pricing checks, new-page discovery, and debugging monitor check history or webhook delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key to create and manage monitors.

Mitigation: Store the key only in CRAWLORA_API_KEY, avoid hardcoding or committing it, and review commands before execution.

Risk: The included helper can call broader Crawlora API endpoints beyond the stated website-monitoring purpose.

Mitigation: Prefer the documented /monitors paths and review PATCH or DELETE requests before running them.

Risk: Webhook notifications can be trusted incorrectly if signatures or timestamps are not checked.

Mitigation: Verify the X-Crawlora-Signature HMAC with the webhook secret and reject stale timestamps.

## Reference(s):

- [website-monitoring endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Crawlora API endpoints and return normalized JSON when commands are run.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
