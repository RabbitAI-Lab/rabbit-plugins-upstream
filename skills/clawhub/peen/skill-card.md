## Description:

Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to configure a Peen provider and workspace, connect clients over WebSocket, and operate or inspect durable coding-agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup runs an unpinned remote installer with broader system access than the listed permissions describe.

Mitigation: Review a fixed installer revision before running it and explicitly approve its installation locations and Docker authority.

Risk: An agent can access its assigned project, and tool output may be stored in transcripts and sent to connected clients.

Mitigation: Use a dedicated project, keep secrets outside the agent workspace, and do not grant the agent access to credentials.

Risk: Exposing the API beyond a trusted local network without protection can allow unauthorized access.

Mitigation: Keep the API local unless authentication and TLS are configured.

## Reference(s):

- [Peen setup, providers, WebSocket, and REST](references/setup.md)
- [Peen repository](https://github.com/psyb0t/peen)
- [Deployment documentation](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [Where Peen runs](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [HTTP API reference](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, API calls]

**Output Format:** [Markdown with shell commands, JSON configuration, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance vary with the selected provider, workspace, and session task.]

## Skill Version(s):

0.27.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
