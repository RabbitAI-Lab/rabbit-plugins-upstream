## Description:

Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to install and configure Peen, connect coding agents to project workspaces, send and follow work through WebSocket, and inspect or control retained sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Peen gives its coding agent access to the selected project, and the controller uses Docker privileges.

Mitigation: Use it only with a project and controller access you trust; inspect and pin the installer, keep agents isolated, and do not expose the Docker socket or credentials to an agent.

Risk: Remote access can expose sessions, and disconnecting a client does not stop ongoing work.

Mitigation: Require authentication and encrypted connections for remote access, and explicitly cancel the session or stop Peen when work should end.

Risk: The downloaded runtime was not fully audited.

Mitigation: Inspect and pin the installer before running it, and avoid granting access to secrets in the workspace.

## Reference(s):

- [Peen on ClawHub](https://clawhub.ai/psyb0t/skills/peen)
- [Peen project](https://github.com/psyb0t/peen)
- [Deployment guide](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [Where Peen runs](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [HTTP API reference](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)
- [Configuration guide](https://github.com/psyb0t/peen/blob/main/docs/configuration.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown instructions with shell, JavaScript, API, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No fixed output contract]

## Skill Version(s):

0.45.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
