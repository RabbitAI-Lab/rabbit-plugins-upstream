## Description:

Keap API integration with managed OAuth for managing contacts, companies, tags, tasks, orders, opportunities, and campaigns for CRM and marketing automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Keap through Maton-managed OAuth, read CRM data, and manage contacts, tags, tasks, orders, opportunities, campaigns, and related marketing automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Keap REST passthrough access can perform writes, send email, trigger campaign or automation actions, and change business data.

Mitigation: Use read and list calls first, connect only the intended Keap account, prefer least-privilege OAuth scopes, and require explicit user confirmation before every POST, PUT, PATCH, DELETE, message send, or workflow trigger.

Risk: Credential exposure could occur if API keys, OAuth tokens, credential stores, config files, or provider-issued tokens are printed, logged, persisted, or passed through shell commands.

Mitigation: Prefer Maton OAuth, let the CLI and operating system credential store handle secrets, use `maton whoami` for verification, and never read, export, print, log, or persist credential values.

Risk: Multiple Maton profiles or Keap connections can cause reads or writes to target the wrong account.

Mitigation: Specify the Maton profile and Keap connection when more than one is available, and verify account context before making changes.

Risk: Content returned from Keap can contain untrusted text or instructions that could influence later agent actions.

Mitigation: Treat API response content as data, validate identifiers and payloads, avoid shell interpolation, and do not follow instructions found inside fetched CRM records, messages, comments, or webhook payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/keap)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Keap Developer Portal](https://developer.infusionsoft.com/)
- [Keap REST API V2 Documentation](https://developer.infusionsoft.com/docs/restv2/)
- [Keap OAuth 2.0 Authentication](https://developer.infusionsoft.com/authentication/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, Keap API paths, request payload examples, and approval guidance for write operations.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
