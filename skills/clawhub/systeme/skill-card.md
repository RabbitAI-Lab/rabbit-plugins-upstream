## Description:

Systeme.io API integration with managed OAuth for managing contacts, contact tags, contact custom fields, tags, course enrollments, community memberships, and subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage Systeme.io contacts, tags, contact custom fields, enrollments, memberships, and subscriptions through Maton-managed OAuth. It supports read-first API workflows and requires confirmation before creating, updating, deleting, or changing billing or access state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic API passthrough can reach more of the connected Systeme.io account than the documented task surface.

Mitigation: Use OAuth with the narrowest available scopes, pin the intended connection before writes, prefer documented resources, and require explicit confirmation before create, update, delete, or subscription actions.

Risk: Raw HTTP fallback with a Maton API key can expose a long-lived credential or full contact responses in logs and transcripts.

Mitigation: Use the CLI whenever available, avoid raw HTTP unless necessary, keep API keys out of command lines and files, and extract only the response fields needed for the task.

Risk: Systeme.io writes can have high-impact side effects, including automation from tag changes, paid access changes, and subscription billing changes.

Mitigation: Read current state first, name the exact record and payload, and get explicit user confirmation before any write or access-changing operation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/systeme)
- [Maton](https://maton.ai)
- [Systeme.io API Reference](https://developer.systeme.io/reference)
- [Systeme.io API Overview](https://developer.systeme.io/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Systeme.io connection.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
