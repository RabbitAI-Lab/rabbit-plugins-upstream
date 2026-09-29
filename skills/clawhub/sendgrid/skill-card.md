## Description:

Connects an agent to SendGrid through Maton to send email, manage contacts and email settings, and review delivery performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to send transactional or marketing email, manage SendGrid contacts, templates and suppressions, and examine email performance through an authorized account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email sends can reach unintended recipients or carry incorrect content.

Mitigation: Confirm recipients, sender, subject and content before approving a send.

Risk: Contact, list, suppression or sender changes can affect live email operations.

Mitigation: Confirm the exact account, resources and scope before approving changes.

Risk: API key creation produces long-lived credentials that persist beyond the session.

Mitigation: Manage keys only when explicitly requested; verify scopes and never expose key values.

Risk: Hosted functions, triggers and destinations can run persistently or forward data to external hosts.

Mitigation: Confirm persistence, event scope, data shared and destination host before approving automation.

## Reference(s):

- [SendGrid skill release on ClawHub](https://clawhub.ai/byungkyu/skills/sendgrid)
- [SendGrid API documentation](https://www.twilio.com/docs/sendgrid/api-reference)
- [Maton homepage](https://maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide authorized SendGrid actions; writes require explicit user approval.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
