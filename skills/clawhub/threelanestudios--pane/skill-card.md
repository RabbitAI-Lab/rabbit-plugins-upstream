## Description:

Operate Pane through its local Gateway: create notes, tasks, and projects via chat sessions; manage AI sessions; sync agent identity files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[threelanestudios](https://clawhub.ai/user/threelanestudios)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and Pane users use this skill to connect an agent to a paired local Pane Gateway so the agent can manage Pane chat sessions, request note, task, project, and folder changes conversationally, and synchronize allowlisted agent identity files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Pane Gateway token grants authenticated access to the paired local Gateway.

Mitigation: Keep PANE_GATEWAY_TOKEN private, avoid printing it in transcripts or logs, and re-pair if the token is missing, expired, or exposed.

Risk: The Gateway commonly uses a self-signed TLS certificate, and disabling TLS verification can expose requests to interception.

Mitigation: Prefer certificate pinning with the Gateway health-check certificate; use PANE_GATEWAY_INSECURE_TLS only when explicitly configured for development.

Risk: Identity-file sync can move sensitive memory, user, rules, tool, and log files into or out of Pane.

Mitigation: Review each identity-file sync request before sending content, and keep sync limited to the documented allowlist.

Risk: Note, task, project, and folder operations are performed through Pane chat sessions and may be ambiguous if titles or project names are unclear.

Mitigation: Use specific titles, project names, statuses, and due dates, then poll or stream session messages to confirm the action completed as intended.

## Reference(s):

- [Pane Gateway API Reference](references/gateway-api.md)
- [Pane Homepage](https://paneapp.ai/?utm_source=clawhub)
- [Pane skill on ClawHub](https://clawhub.ai/threelanestudios/skills/pane)
- [Three Lane Studios publisher profile](https://clawhub.ai/user/threelanestudios)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local Gateway HTTP and SSE calls through curl; authenticated operations require PANE_GATEWAY_URL and PANE_GATEWAY_TOKEN.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
