## Description:

Google Analytics API integration with managed OAuth for read-only reporting through the Data API and administrative account, property, and data stream management through the Admin API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to connect a Maton-authenticated Google Analytics account, run GA4 reports, and perform explicitly approved Admin API changes. It supports reporting workflows first and treats account, property, data stream, and custom definition changes as high-impact actions requiring specific resource identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates against live Google Analytics data through Maton-authenticated connections.

Mitigation: Use the read-only Data API for reporting, confirm the exact account or property before each action, and avoid printing or storing unnecessary raw report data.

Risk: Admin API writes can create, update, or delete accounts, properties, data streams, and related configuration.

Mitigation: Approve Admin API writes only after reviewing the exact resource identifiers, payload, and expected effect.

Risk: Raw API keys and broad OAuth access increase credential and data exposure risk.

Mitigation: Prefer OAuth through the Maton CLI, use raw API keys only when the CLI cannot be used, and choose the narrowest Google Analytics scopes available.

Risk: Connections, functions, triggers, or destinations can remain active after the task is complete.

Mitigation: Delete unused connections, functions, triggers, and destinations when finished.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-analytics)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Analytics Admin API Overview](https://developers.google.com/analytics/devguides/config/admin/v1)
- [Google Analytics Data API Overview](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [Google Analytics Run Report](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runReport)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, API paths, JSON examples, and optional Python or Node code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are instructions and examples for authenticated live Google Analytics calls through Maton; writes require explicit user approval.]

## Skill Version(s):

1.2.5 (source: server release evidence; artifact metadata version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
