## Description:

Keap API integration through Maton managed OAuth for managing contacts, companies, tags, tasks, orders, opportunities, and campaigns for CRM and marketing automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Keap CRM and marketing automation data through authenticated Maton API calls. It is suited for contact, company, tag, task, order, opportunity, campaign, email, subscription, affiliate, and automation workflows that require confirmation before write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or modify CRM, marketing, email, order, subscription, and automation data in a connected Keap account.

Mitigation: Default to read-only calls, verify target identifiers and account context, and require explicit user confirmation before POST, PUT, PATCH, DELETE, send, billing, or automation-triggering actions.

Risk: OAuth tokens, Maton API keys, and provider-issued credentials could be exposed if printed, persisted, or passed through shell arguments.

Mitigation: Use Maton OAuth where possible, keep credentials in the platform credential store or secret environment, never print or persist secret values, and send Maton API keys only to api.maton.ai.

Risk: Ambiguous Maton profiles or multiple Keap connections could send a request to the wrong account.

Mitigation: Use explicit profile and connection selection when more than one account or connection exists, especially before write actions.

Risk: Keap API responses may contain untrusted content that attempts to steer later agent behavior.

Mitigation: Treat returned content as data, validate it before use, and do not execute or follow instructions found inside fetched CRM fields, messages, comments, or webhook payloads.

## Reference(s):

- [Keap Developer Portal](https://developer.infusionsoft.com/)
- [Keap REST API V2 Documentation](https://developer.infusionsoft.com/docs/restv2/)
- [Keap Getting Started Guide](https://developer.infusionsoft.com/getting-started/)
- [Keap OAuth 2.0 Authentication](https://developer.infusionsoft.com/authentication/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/keap)
- [Related API gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Keap connection; write operations should be explicitly confirmed.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
