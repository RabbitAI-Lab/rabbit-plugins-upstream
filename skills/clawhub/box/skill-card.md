## Description:

Box API integration with managed OAuth for managing files, folders, collaborations, shared links, and cloud storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to manage Box files and folders through Maton-managed OAuth. It supports read, upload, sharing, collaboration, webhook, and automation workflows when the user has authorized the relevant Box connection and approved higher-risk actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A long-lived Maton API key can be exposed through environment variables, logs, shell history, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist the API key, send it only to api.maton.ai, and rotate it if exposed.

Risk: Box uploads, deletes, public shared links, collaborations, and webhooks can disclose, replace, or remove user data.

Mitigation: Default to read and list operations, verify the target resource and payload, and get explicit user confirmation before every write, sharing, collaboration, webhook, upload, or delete operation.

Risk: Hosted functions, triggers, and destinations can create persistent automation or forwarding of event data.

Mitigation: Use only user-authored or user-reviewed handlers, prefer DENY_ALL network policy, keep destinations on Maton-controlled hosts unless explicitly approved, and remove unneeded functions, triggers, and destinations.

## Reference(s):

- [ClawHub Box Skill](https://clawhub.ai/byungkyu/skills/box)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Box API Reference](https://developer.box.com/reference)
- [Box Developer Documentation](https://developer.box.com/guides)
- [Box Authentication Guide](https://developer.box.com/guides/authentication)
- [Box SDKs](https://developer.box.com/sdks-and-tools)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-authorized Box OAuth connection; write, sharing, webhook, function, trigger, and destination actions require explicit confirmation.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
