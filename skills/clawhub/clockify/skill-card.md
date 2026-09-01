## Description:

Clockify API integration with managed OAuth for tracking time and managing projects, clients, tasks, workspaces, and workspace members.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub users and agents use this skill to access a connected Clockify account through Maton for listing and updating time entries, projects, clients, tasks, tags, workspaces, and workspace members. It is intended for read/list workflows by default, with user confirmation before connection creation or write/delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables an agent to access a user's Clockify account through Maton.

Mitigation: Install only when Clockify access through Maton is intended, and review connection creation before authorizing it.

Risk: Write or delete operations can change workspaces, projects, tasks, clients, tags, time entries, or member access.

Mitigation: Confirm the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE operation.

Risk: Credentials or provider-issued tokens could be exposed if printed, persisted, or passed through shell arguments.

Mitigation: Prefer OAuth with the operating system credential store, avoid inspecting stored credentials, and use stdin-based raw HTTP fallback only when the CLI cannot be installed.

Risk: Multiple Maton or Clockify connections can cause actions to apply to the wrong account.

Mitigation: List available connections first and specify the intended connection or profile before making account-specific calls.

## Reference(s):

- [ClawHub Clockify Skill](https://clawhub.ai/byungkyu/skills/clockify)
- [Maton Homepage](https://maton.ai)
- [Clockify API Documentation](https://docs.clockify.me/)
- [Clockify Time Entry API Reference](https://docs.clockify.me/#tag/Time-entry)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides API calls through the Maton CLI and managed OAuth; no typed Clockify command wrapper is documented.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
