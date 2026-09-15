## Description:

Toggl Track API integration with managed OAuth for tracking time and managing workspaces, projects, clients, tags, and time entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to Toggl Track through Maton, inspect account and workspace data, and create, update, or delete Toggl Track resources after user approval. It also documents how approved Toggl Track actions can be run through hosted functions and scheduled or event-driven triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External package installation and gateway use require trust in Maton and its package sources.

Mitigation: Install only from trusted Maton package sources and keep the reviewed CLI version pinned unless release notes are reviewed before upgrading.

Risk: OAuth tokens or long-lived API keys can expose Toggl Track data if mishandled.

Mitigation: Prefer OAuth and the operating system credential store, avoid exporting MATON_API_KEY except where the CLI cannot be installed, and do not paste signing keys into command examples.

Risk: Write operations, connection changes, hosted functions, and triggers can modify data or continue acting after setup.

Mitigation: Default to read and list calls, then obtain explicit user approval for every write, new connection, function deployment, trigger, invocation, or deletion.

Risk: Persistent trigger destinations can forward future event data, including sensitive third-party data, outside the platform.

Mitigation: Avoid third-party destinations unless the user explicitly approves the exact host and data flow, minimize forwarded fields with templates, and delete destinations that are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/toggl-track)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Toggl Track API Documentation](https://engineering.toggl.com/docs/)
- [Toggl Track API Reference](https://engineering.toggl.com/docs/api/authentication)
- [Time Entries API](https://engineering.toggl.com/docs/api/time_entries)
- [Projects API](https://engineering.toggl.com/docs/api/projects)
- [Clients API](https://engineering.toggl.com/docs/api/clients)
- [Tags API](https://engineering.toggl.com/docs/api/tags)
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

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, HTTP examples, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated API call plans, Maton CLI commands, hosted function examples, trigger configuration guidance, and safety confirmations before writes or automation.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
