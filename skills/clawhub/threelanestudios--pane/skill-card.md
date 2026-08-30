## Description:

Operate Pane through its local Gateway: create notes, tasks, and projects via chat sessions; manage AI sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[threelanestudios](https://clawhub.ai/user/threelanestudios)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Pane users use this skill to let an agent work with a local Pane workspace through a paired Gateway, including creating and updating notes, tasks, projects, folders, and chat sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paired Gateway token allows agent control over the user's local Pane workspace.

Mitigation: Install only when this control is intended, keep the token secret, and avoid printing or logging the full token in chat transcripts.

Risk: Self-signed Gateway TLS can be weakened if verification is skipped.

Mitigation: Prefer certificate pinning from the Gateway health endpoint and use insecure TLS only when explicitly configured for development.

Risk: Multi-step Pane requests may schedule follow-up actions in the same session.

Mitigation: Review multi-step requests and confirm the intended Pane session before allowing scheduled follow-up work.

## Reference(s):

- [Pane Skill on ClawHub](https://clawhub.ai/threelanestudios/skills/pane)
- [Pane Homepage](https://paneapp.ai/?utm_source=clawhub)
- [Pane Gateway API Reference](references/gateway-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local Gateway calls with a user-provided bearer token; session message content is capped at 1 MiB and chat completion proxy bodies at 8 MiB.]

## Skill Version(s):

1.2.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
