## Description:

GoHighLevel (Private Integration Token) API integration with managed authentication for CRM, sales pipelines, calendars, conversations, payments, and marketing automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate on GoHighLevel CRM, pipeline, calendar, conversation, payment, location, and workflow data through Maton-managed Private Integration Token authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on CRM, messaging, billing, calendar, location, and workflow data in a connected GoHighLevel account.

Mitigation: Use OAuth where possible, connect only the needed account or location, and require explicit confirmation of the exact resource, payload, and intended effect before writes, deletions, messages, billing changes, or workflow operations.

Risk: Credentials or provider-issued tokens could be exposed if copied into commands, logs, files, or prompts.

Mitigation: Let Maton manage credentials through OAuth or the operating system credential store, and do not print, export, persist, or transmit credential values.

Risk: Agency and Sub-Account tokens have different scopes, so an ambiguous connection can target the wrong account or location.

Mitigation: Specify the intended Maton profile and connection for sensitive calls, and use read/list calls first to verify account context and resource identifiers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/highlevel-api)
- [Maton Homepage](https://maton.ai)
- [GoHighLevel API Documentation](https://highlevel.stoplight.io/docs/integrations/)
- [GoHighLevel Marketplace Documentation](https://marketplace.gohighlevel.com/docs/)
- [Private Integration Token Guide](https://marketplace.gohighlevel.com/docs/integrations/custom-token)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval for new connections or write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
