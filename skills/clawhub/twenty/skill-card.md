## Description:

Twenty CRM API integration with managed authentication for managing companies, people, opportunities, notes, tasks, workflows, and workspace members.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Twenty CRM through Maton-managed authentication for CRM records, activities, workflows, and workspace member tasks. It supports read-first workflows and requires confirmation before creating connections, modifying CRM data, deleting resources, or enabling automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify CRM data through a Maton-mediated Twenty CRM connection.

Mitigation: Prefer read and list calls first, confirm the exact account and connection, and require explicit approval before any write or delete.

Risk: Long-lived API keys can be exposed through environment variables or process inheritance.

Mitigation: Prefer OAuth and the operating system credential store; avoid exporting MATON_API_KEY except where the CLI cannot be installed.

Risk: Hosted functions and triggers can keep running after setup and act on future data.

Mitigation: Use user-authored or user-reviewed handlers, apply least-privilege connection scope, use DENY_ALL network policy where documented, and get separate approval for deploys and invocations.

Risk: Trigger destinations can create persistent automatic forwarding to a URL.

Mitigation: Create or update destinations only after the user confirms the destination host, data fields, persistence, and credential handling; remove destinations that are no longer needed.

## Reference(s):

- [Twenty CRM ClawHub Page](https://clawhub.ai/byungkyu/skills/twenty)
- [Maton Homepage](https://maton.ai)
- [Twenty API Documentation](https://docs.twenty.com/developers/extend/api)
- [Twenty GitHub](https://github.com/twentyhq/twenty)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, Python, JSON, and HTTP examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Twenty CRM connection; write, delete, connection, function, trigger, and destination actions require explicit user confirmation.]

## Skill Version(s):

1.2.5 (source: server release evidence, released 2026-09-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
