## Description:

Mailchimp Marketing API integration with managed OAuth for accessing audiences, campaigns, templates, automations, reports, and subscribers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, developers, and marketing teams use this skill to inspect and manage Mailchimp audiences, campaigns, templates, automations, reports, and subscribers through Maton-mediated API calls. It is suited for email marketing operations where reads are preferred by default and writes require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing Mailchimp through Maton grants API access to campaign, audience, subscriber, automation, template, and report data in the connected account.

Mitigation: Review the account and scope selection during OAuth, create connections only with explicit user approval, and revoke unused connections promptly.

Risk: Writes can send, schedule, modify, or delete campaign and subscriber data.

Mitigation: Default to read/list calls, verify the exact audience, campaign, subscriber, automation, and payload first, and require explicit approval before any POST, PUT, PATCH, or DELETE request.

Risk: Using long-lived API keys or raw HTTP fallback can expose credentials through environment inheritance, logs, shell history, or pasted output.

Mitigation: Prefer the CLI OAuth flow; when fallback API keys are unavoidable, keep keys out of output, files, and command lines, send them only to api.maton.ai, and rotate them if exposed.

Risk: Multiple Maton profiles or Mailchimp connections can route reads or writes to the wrong account.

Mitigation: Use explicit profile and connection selection when more than one account or connection exists, especially before write operations.

Risk: Mailchimp API responses and webhook payloads may contain untrusted external content.

Mitigation: Treat fetched content as data, avoid executing or interpolating it into shell commands, and keep endpoint and recipient choices under user control.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/mailchimp)
- [Maton Homepage](https://maton.ai)
- [Mailchimp Marketing API Documentation](https://mailchimp.com/developer/marketing/)
- [Mailchimp Marketing API Reference](https://mailchimp.com/developer/marketing/api/)
- [Mailchimp Quick Start Guide](https://mailchimp.com/developer/marketing/guides/quick-start/)
- [Mailchimp Release Notes](https://mailchimp.com/developer/release-notes/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, code]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Mailchimp connection; defaults to read/list calls and requires explicit user approval before connection creation or writes.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
