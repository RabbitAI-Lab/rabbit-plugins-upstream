## Description:

Creates and manages Crawlora monitors that detect changes to public pages or sitemap URLs and can notify a webhook.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can create, inspect, update, and delete website-change monitors, review check history, and receive notifications when a public page or sitemap changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposure of the Crawlora API key could allow unauthorized monitor management.

Mitigation: Keep CRAWLORA_API_KEY secret and out of committed files and command-line arguments.

Risk: Unverified webhook deliveries could be spoofed or replayed.

Mitigation: Verify webhook signatures using the configured secret and reject stale timestamps before trusting events.

Risk: Updating or deleting the wrong monitor can disrupt change tracking.

Mitigation: Confirm the monitor ID and intended changes before update or delete actions.

## Reference(s):

- [Website monitoring endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub website-monitoring release](https://clawhub.ai/crawlora-org/skills/website-monitoring)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monitor checks consume credits; webhooks can report changes or completed runs.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
