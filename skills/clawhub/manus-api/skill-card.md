## Description:

Manus provides a Maton-backed integration for creating and managing Manus AI agent tasks, projects, files, and webhooks with managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Manus through Maton for task, project, file, and webhook workflows. Routine use starts with read and list calls, with explicit user confirmation for writes, new connections, hosted functions, triggers, and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Maton as a gateway to the user's Manus account and can reach data allowed by the authorized connection.

Mitigation: Prefer OAuth login, select only needed scopes when available, use the intended connection explicitly when multiple connections exist, and confirm new connections or writes with the user.

Risk: Raw Maton API keys can be exposed through environment variables, command lines, logs, shell history, or pasted output when the CLI cannot be used.

Mitigation: Use OAuth and the Maton CLI credential store when possible; if raw HTTP is necessary, keep MATON_API_KEY out of logs and command arguments, send it only to api.maton.ai, avoid persistence, and rotate it if exposed.

Risk: Hosted functions, triggers, webhook destinations, and local --exec automation can run approved actions later or send data outside the user's intended boundary.

Mitigation: Review every function handler, trigger destination, webhook URL, and automation command before approval; prefer DENY_ALL network policy for hosted functions unless specific hosts are required.

Risk: Manus responses may contain personal or business data such as names, email addresses, files, messages, or document contents.

Mitigation: Extract only the fields needed for the task and avoid dumping raw responses into logs, files, or user-visible output unless explicitly requested.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/manus-api)
- [Maton Homepage](https://maton.ai)
- [Manus API Overview](https://open.manus.im/docs)
- [Manus API Reference](https://open.manus.im/docs/api-reference)
- [Manus Website](https://manus.im)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Catalogue](references/calendly/triggers.md)
- [GitHub Trigger Catalogue](references/github/triggers.md)
- [Google Mail Trigger Catalogue](references/google-mail/triggers.md)
- [HubSpot Trigger Catalogue](references/hubspot/triggers.md)
- [Linear Trigger Catalogue](references/linear/triggers.md)
- [Notion Trigger Catalogue](references/notion/triggers.md)
- [Slack Trigger Catalogue](references/slack/triggers.md)
- [Stripe Trigger Catalogue](references/stripe/triggers.md)
- [Time Trigger Catalogue](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP examples for constrained environments, hosted-function examples, trigger setup guidance, and safety checks for user approval.]

## Skill Version(s):

1.2.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
