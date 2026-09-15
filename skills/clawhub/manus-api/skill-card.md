## Description:

Manus provides managed access to the Manus AI Agent API for creating and managing agent tasks, projects, files, and webhooks through Maton-authenticated calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation builders use this skill to run Manus agent tasks, inspect projects and files, and set up approved webhooks or scheduled/event-driven automations through a Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading the Maton CLI from an untrusted or unpinned source could change the reviewed behavior.

Mitigation: Install the CLI only from trusted Maton channels and use the pinned versions documented by the skill unless the user deliberately approves an upgrade.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key that could leak through logs, shell history, child processes, or persisted environment files.

Mitigation: Prefer OAuth login through the Maton CLI; when raw HTTP is unavoidable, read the key only from the runtime environment, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

Risk: Webhooks, triggers, and hosted functions can create persistent or automated data forwarding for Manus task activity and connected app events.

Mitigation: Require explicit user approval for the exact destination, scope, host ownership, data being forwarded, function code, and network policy; prefer narrow scopes and DENY_ALL network policy where possible.

Risk: Write, delete, connection, webhook, trigger, or hosted function actions can affect user data or connected accounts.

Mitigation: Default to read and list operations, summarize the least-privilege action first, identify the exact connection or resource, and proceed only after user confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/manus-api)
- [Maton Homepage](https://maton.ai)
- [Manus API Overview](https://open.manus.im/docs)
- [Manus API Reference](https://open.manus.im/docs/api-reference)
- [Manus Website](https://manus.im)
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

**Output Format:** [Markdown with Maton CLI commands, SDK snippets, raw HTTP examples, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default outputs should favor read/list calls and concise extracted response fields; writes, new connections, functions, triggers, and webhooks require explicit user confirmation.]

## Skill Version(s):

1.2.5 (source: server release metadata; skill frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
