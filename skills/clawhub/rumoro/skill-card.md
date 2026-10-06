## Description:

Helps agents monitor brands, competitors, and topics across social platforms, triage mentions, configure alerts, and summarize analytics with Rumoro.

This skill is ready for commercial/non-commercial use.

## Publisher:

[markolo10](https://clawhub.ai/user/markolo10)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and agents use Rumoro to monitor public discussion of brands, competitors, and topics, review and triage mentions, set alerts, and report trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monitoring and triage data sent to Rumoro's external API may include sensitive business context.

Mitigation: Install only when sharing relevant brand, competitor, keyword, alert, and triage data with Rumoro is acceptable.

Risk: A write-capable key permits account changes that may affect billing.

Mitigation: Prefer a read-only key for analysis; use a write key only when authorized to create or modify tracking keywords, alerts, channels, and notes.

## Reference(s):

- [Rumoro OpenClaw integration](https://docs.rumoro.dev/integrations/openclaw)
- [Rumoro agent guide](https://mcp.rumoro.dev/mcp/guide)
- [Rumoro API reference](https://api.rumoro.dev/v1/openapi.json)
- [Rumoro ClawHub release](https://clawhub.ai/markolo10/skills/rumoro)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Natural-language summaries and guidance, with optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to source posts and monitoring or alert settings.]

## Skill Version(s):

0.1.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
