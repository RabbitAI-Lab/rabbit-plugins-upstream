## Description:

GoHighLevel Private Integration Token API integration with managed Maton authentication for CRM, sales pipelines, calendars, conversations, payments, and marketing automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to make GoHighLevel API calls through Maton for contacts, opportunities, calendars, conversations, invoices, products, workflows, and location-scoped CRM tasks. It supports read/list workflows by default and requires confirmation for connection creation or write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill brokers access to a GoHighLevel account through Maton, which can expose CRM, calendar, conversation, billing, workflow, and location data within the connected account.

Mitigation: Install only when Maton-brokered GoHighLevel access is intended, use the narrowest available connection and scopes, and specify the correct account or connection before making calls.

Risk: Write, delete, messaging, billing, scheduling, and automation operations can create external side effects or data loss.

Mitigation: Default to read and list calls, verify identifiers and current state first, and require explicit user confirmation of the target, payload, and intended effect before any modifying request.

Risk: Raw API-key mode uses a long-lived credential and has higher exposure risk than OAuth-backed CLI authentication.

Mitigation: Prefer Maton OAuth login and avoid raw API-key mode unless the CLI cannot be used.

## Reference(s):

- [GoHighLevel API Documentation](https://highlevel.stoplight.io/docs/integrations/)
- [GoHighLevel Marketplace Documentation](https://marketplace.gohighlevel.com/docs/)
- [Private Integration Token Guide](https://marketplace.gohighlevel.com/docs/integrations/custom-token)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected GoHighLevel Private Integration Token.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
