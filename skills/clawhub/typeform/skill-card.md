## Description:

Typeform API integration with managed OAuth for creating forms, managing responses, accessing insights, and wiring user-approved Typeform actions into Maton functions or triggers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Typeform through Maton, inspect forms and responses, and make explicitly approved changes such as creating, updating, or deleting Typeform resources. It also guides approved automation patterns using Maton functions and triggers when unattended Typeform actions are needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and delete operations can change or remove Typeform resources.

Mitigation: Default to read and list calls, then require explicit user confirmation before POST, PUT, PATCH, DELETE, new connections, or connection deletion.

Risk: Raw API key usage can expose a long-lived Maton credential through process environments, logs, shell history, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI; use raw HTTP only when the CLI cannot be installed, never print or persist the key, and rotate it if exposed.

Risk: Functions, triggers, and destinations can run or forward data continuously after setup.

Mitigation: Create hosted automation only after the user approves the handler, target connection, destination, and network policy; delete automation that is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/typeform)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Typeform API Overview](https://www.typeform.com/developers/get-started)
- [Typeform Forms API](https://www.typeform.com/developers/create/reference/retrieve-forms)
- [Typeform Responses API](https://www.typeform.com/developers/responses/reference/retrieve-responses)
- [Typeform Workspaces API](https://www.typeform.com/developers/create/reference/retrieve-workspaces)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses read-first guidance, explicit approval for writes and new connections, and OAuth-preferred credential handling.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
