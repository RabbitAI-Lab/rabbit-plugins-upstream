## Description:

Operate Pane through its local Gateway: create notes, tasks, and projects via chat sessions; manage AI sessions; sync agent identity files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[matthewcarano](https://clawhub.ai/user/matthewcarano)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an OpenClaw agent to a local Pane Gateway, manage Pane sessions, and create or update workspace notes, tasks, projects, and identity files through Pane's chat-driven workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Gateway access can expose local Pane sessions and OpenClaw identity, memory, and log files.

Mitigation: Install only for trusted Pane Gateway instances and publishers, and avoid use in environments containing sensitive agent history unless that broad sync behavior is acceptable.

Risk: The skill supports deferred follow-up behavior through scheduled Pane session work.

Mitigation: Review requested multi-step work before granting credentials, and monitor Pane session transcripts for scheduled follow-up results.

Risk: The Gateway uses bearer tokens and may use self-signed TLS by default.

Mitigation: Treat PANE_GATEWAY_TOKEN as a secret, prefer certificate pinning with the Gateway health certificate, and use insecure TLS only when explicitly intended for development.

## Reference(s):

- [Pane Gateway API Reference](references/gateway-api.md)
- [Pane homepage](https://paneapp.ai/?utm_source=clawhub)
- [ClawHub skill page](https://clawhub.ai/matthewcarano/skills/pane)
- [Publisher profile](https://clawhub.ai/user/matthewcarano)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue authenticated local Gateway requests and schedule deferred follow-up steps when operating inside Pane sessions.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
