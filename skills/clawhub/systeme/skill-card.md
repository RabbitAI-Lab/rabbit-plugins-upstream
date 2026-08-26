## Description:

Systeme.io API integration with managed OAuth for managing contacts, tags, courses, communities, and subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, business operators, and developers use this skill to manage Systeme.io contacts, tags, course enrollments, community memberships, and subscriptions through Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Systeme.io contacts, tags, enrollments, memberships, subscriptions, and automations through authenticated API calls.

Mitigation: Default to read and list operations first, then require explicit user approval with target resource, payload, and intended effect before any write, delete, subscription, enrollment, membership, or automation action.

Risk: Long-lived API keys or provider-issued tokens could be exposed if printed, persisted, logged, or passed on command lines.

Mitigation: Prefer OAuth through the Maton CLI, let the operating system credential store hold secrets, and avoid printing, exporting, logging, or persisting credentials.

Risk: Requests may affect the wrong Systeme.io account when multiple Maton profiles or connections exist.

Mitigation: Specify the intended Maton profile and Systeme.io connection when multiple accounts or connections are available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/systeme)
- [Maton homepage](https://maton.ai)
- [Systeme.io API reference](https://developer.systeme.io/reference)
- [Systeme.io API overview](https://developer.systeme.io/)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user approval before connection creation or data-modifying API calls.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter lists 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
