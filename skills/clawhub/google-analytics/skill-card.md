## Description:

Google Analytics API integration with managed OAuth for reading Analytics reports through the Data API and administering accounts, properties, and data streams through the Admin API with explicit approval for writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analytics operators use this skill to connect an agent to Google Analytics through Maton, run GA4 reports, inspect accounts and properties, and perform administrative changes only after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Analytics access is routed through the Maton OAuth gateway.

Mitigation: Install only when this routing is acceptable for the target account and prefer OAuth-backed Maton CLI flows over long-lived API keys.

Risk: The Admin API can create, update, and delete Analytics accounts, properties, data streams, and related configuration.

Mitigation: Use the read-only Data API for reporting tasks; create an Admin API connection only for administrative work and require exact resource IDs plus explicit user confirmation before any write or deletion.

Risk: Analytics responses may contain account, property, user, or reporting data that should not be broadly exposed.

Mitigation: Return only fields needed for the task and avoid logging, persisting, or printing raw response bodies unless the user explicitly asks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-analytics)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Analytics Admin API Overview](https://developers.google.com/analytics/devguides/config/admin/v1)
- [Google Analytics Data API Overview](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [Run Report Reference](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runReport)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request paths, report payloads, connection instructions, and confirmation prompts for write-capable Admin API operations.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
