## Description:

Calls third-party APIs through Maton-connected app credentials and guides agents through read, write, trigger, webhook destination, and function workflows with explicit confirmation rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to have an agent call APIs for Maton-connected third-party apps, inspect resources, make approved changes, manage triggers and destinations, and work with Maton-hosted functions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act through user-connected services, including writes, messages, sharing changes, webhook or trigger setup, function deployment, and local --exec handlers.

Mitigation: Prefer read-only tasks first, verify the exact account or connection, and require explicit user confirmation before sensitive or state-changing actions.

Risk: Webhook destinations and triggers can create persistent event forwarding until they are removed.

Mitigation: Require a separate approval that identifies the source, event type, destination URL, payload scope, and removal plan before creating or updating destinations.

Risk: Local --exec handlers run user-side scripts on event data that may be untrusted.

Mitigation: Run only user-authored or user-reviewed handlers, keep approval separate from normal API calls, and validate event data before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Artifact Supported App References](references/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, text]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and task-specific user confirmation for sensitive actions.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
