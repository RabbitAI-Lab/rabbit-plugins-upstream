## Description:

Toggl Track API integration with managed OAuth for tracking time and managing projects, clients, tags, and workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to access Toggl Track through Maton-managed OAuth, perform read/list operations, and make approved changes to time entries, projects, clients, tags, and related automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes, connection creation, hosted functions, triggers, and destinations can change Toggl Track data or create ongoing automations and data flows.

Mitigation: Default to read and list operations, and require explicit user confirmation before any write, connection creation, hosted function, trigger, destination, invocation, or deletion.

Risk: Long-lived Maton API keys can be exposed if copied into environment variables, logs, files, commands, or trigger destinations.

Mitigation: Prefer OAuth through the Maton CLI and operating system credential store; use raw HTTP and API keys only when the CLI cannot be installed, and avoid logging or storing credentials.

Risk: Using the wrong Toggl Track connection or deploying broad hosted code can access unintended account data.

Mitigation: List and confirm the exact connection before use, scope OAuth to the task, use user-authored or user-reviewed handlers, and deploy hosted functions with DENY_ALL network policy unless the user explicitly approves named hosts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/toggl-track)
- [Maton Homepage](https://maton.ai)
- [Toggl Track API Documentation](https://engineering.toggl.com/docs/)
- [Toggl Track API Reference](https://engineering.toggl.com/docs/api/authentication)
- [Time Entries API](https://engineering.toggl.com/docs/api/time_entries)
- [Projects API](https://engineering.toggl.com/docs/api/projects)
- [Clients API](https://engineering.toggl.com/docs/api/clients)
- [Tags API](https://engineering.toggl.com/docs/api/tags)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands, Python snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval for writes, new connections, hosted functions, triggers, destinations, and destructive actions.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
