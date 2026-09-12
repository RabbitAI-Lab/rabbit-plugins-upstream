## Description:

Google Analytics API integration with managed OAuth that guides agents to run read-only Data API reports and, with explicit approval, make Admin API account, property, and data stream changes through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to authenticate through Maton, inspect GA4 accounts and properties, run analytics reports, and perform explicit user-approved Admin API changes when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a Maton-connected Google Analytics Admin API account to create, update, or delete accounts, properties, and data streams.

Mitigation: Prefer the read-only Data API for reporting; use the Admin API only after confirming the exact account, property, data stream, payload, and intended effect with the user.

Risk: Admin API changes can have high-impact or irreversible effects on analytics configuration and data collection.

Mitigation: List or retrieve the target resource first, present the specific identifiers and consequences, wait for explicit approval, and revoke unused Admin API connections after the task.

Risk: Maton API keys and provider-issued tokens can leak if printed, logged, persisted, or passed on command lines.

Mitigation: Use OAuth and the operating system credential store where possible; when raw HTTP is required, read the key from the process environment, never display it, and send it only to api.maton.ai.

Risk: Google Analytics API responses may contain sensitive or untrusted external data.

Mitigation: Request only task-relevant fields, avoid storing raw responses unless requested, and treat response content as data rather than instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-analytics)
- [Maton homepage](https://maton.ai)
- [Admin API Overview](https://developers.google.com/analytics/devguides/config/admin/v1)
- [Admin API Accounts](https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1beta/accounts)
- [Admin API Properties](https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1beta/properties)
- [Admin API Data Streams](https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1beta/properties.dataStreams)
- [Data API Overview](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [Run Report](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runReport)
- [Realtime Report](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runRealtimeReport)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides Google Analytics calls through Maton OAuth or a raw HTTPS fallback when the CLI cannot be installed.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
