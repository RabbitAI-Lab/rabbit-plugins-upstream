## Description:

TickTick API integration with managed OAuth for managing tasks, projects, and task lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect a TickTick account through Maton OAuth, list tasks and projects, and perform approved create, update, complete, and delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton API keys or TickTick response data could be exposed through command lines, logs, files, or raw response dumps.

Mitigation: Prefer OAuth and the operating system credential store, avoid putting live secrets in command lines, and extract only the response fields needed for the task.

Risk: Write operations, connection changes, or deletions can modify TickTick data or authorization state.

Mitigation: Default to read and list calls first, then require explicit confirmation of the target resource, payload, and intended effect before POST, PUT, PATCH, DELETE, or connection changes.

Risk: Persistent triggers and destinations can continue forwarding future event data until removed.

Mitigation: Review the destination URL, event fields, persistence, and credentials before creation or update; keep TickTick automation on approved Maton-hosted functions where possible and delete destinations that are no longer needed.

Risk: Local event handlers run through trigger watch --exec would process untrusted event payloads.

Mitigation: Use plain event listing or watch for inspection, and run --exec only with a user-authored or user-reviewed handler after separate approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/ticktick-api-skill)
- [Maton Homepage](https://maton.ai)
- [TickTick Developer Portal](https://developer.ticktick.com/)
- [TickTick Help Center](https://help.ticktick.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
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

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated API call instructions, Maton CLI commands, raw HTTPS examples, and approval checklists.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
