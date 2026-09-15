## Description:

Wrike API integration with managed OAuth for managing tasks, folders, projects, spaces, team collaboration, and administrative functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, project managers, and developers use this skill to inspect and update Wrike work items, collaboration resources, time logs, and account resources through a managed OAuth connection. It is also used for approved Wrike automation through Maton functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access broad Wrike workspace data, including administrative resources and data exports.

Mitigation: Use OAuth with least-privilege scopes, prefer read/list operations, and require explicit confirmation for admin, export, and write actions.

Risk: API keys and trigger destination secrets could be exposed if placed in shell commands, logs, headers, or body templates.

Mitigation: Prefer managed OAuth and OS credential storage; never print, log, or embed Maton or provider credentials in trigger destinations.

Risk: Triggers and destinations can create persistent forwarding of future event data.

Mitigation: Create triggers or destinations only after the user approves the exact source, scope, destination host, payload fields, and persistence, and remove them when no longer needed.

Risk: Hosted functions can continue acting with the deploying Maton account's connected app access.

Mitigation: Deploy only user-authored or user-reviewed handlers, prefer DENY_ALL network policy, summarize reachable connections before deployment, and delete functions after their task is complete.

## Reference(s):

- [Wrike API Documentation](https://developers.wrike.com/)
- [Wrike API Overview](https://developers.wrike.com/overview/)
- [OAuth 2.0 Authorization](https://developers.wrike.com/oauth-20-authorization/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [Wrike Skill on ClawHub](https://clawhub.ai/byungkyu/skills/wrike-api)
- [API Gateway Skill on ClawHub](https://clawhub.ai/byungkyu/api-gateway)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Wrike connection; write, admin, export, connection, function, and trigger actions require explicit user approval.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
