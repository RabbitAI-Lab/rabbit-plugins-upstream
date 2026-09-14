## Description:

Calendly API integration with managed OAuth for retrieving scheduling data, checking availability, booking meetings, and managing approved webhook-based automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a Calendly account through Maton, inspect event types, scheduled events, invitees, and availability, book meetings, and manage approved webhooks or hosted automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys or OAuth credentials could be exposed if copied into commands, logs, files, or trigger destinations.

Mitigation: Use OAuth where possible, keep credentials in the platform or operating-system credential store, and avoid putting Maton or provider tokens in destination headers or templates.

Risk: Webhook subscriptions, trigger destinations, and hosted automations can create persistent forwarding or unattended actions on scheduling data.

Mitigation: Review and approve every write or automation action, confirm the exact destination and data flow, and only send data to hosts the user controls and explicitly approved.

Risk: A hosted function can act through the deploying Maton account's connected services.

Mitigation: Use a dedicated Maton account or narrowly scoped connection set for hosted functions, prefer DENY_ALL network policy, and deploy only user-authored or user-reviewed handlers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/calendly-api)
- [Maton](https://maton.ai)
- [Calendly Developer Portal](https://developer.calendly.com/)
- [Calendly API Reference](https://developer.calendly.com/api-docs)
- [Calendly API Use Cases](https://developer.calendly.com/api-use-cases)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with shell commands, HTTP/API examples, and small Python or JavaScript snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and a Maton account; OAuth is recommended, writes and automations require explicit approval, and raw API-key use is reserved for environments where the CLI cannot be installed.]

## Skill Version(s):

1.2.4 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
