## Description:

Operate Pane through its local Gateway: create notes, tasks, and projects via chat sessions; manage AI sessions; sync agent identity files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[threelanestudios](https://clawhub.ai/user/threelanestudios)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Pane users use this skill to let an agent operate a paired local Pane Gateway for conversational note, task, project, session, and identity-file workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Pane Gateway bearer token that can act on the user's local Pane workspace.

Mitigation: Install only when that access is acceptable, keep the token secret, and use the skill for explicit, bounded Pane tasks.

Risk: Proactive scheduling can queue follow-up work after the initial request.

Mitigation: Review the scheduled-work behavior before installation and use it only for tasks where deferred steps are expected.

Risk: Insecure TLS can disable certificate verification for local development.

Mitigation: Prefer pinned Gateway certificates and enable insecure TLS only for local development.

## Reference(s):

- [Pane Gateway API Reference](references/gateway-api.md)
- [Pane Homepage](https://paneapp.ai/?utm_source=clawhub)
- [ClawHub Skill Page](https://clawhub.ai/threelanestudios/skills/pane)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a local Pane Gateway with a bearer token and may queue follow-up work for explicit multi-step Pane session tasks.]

## Skill Version(s):

1.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
