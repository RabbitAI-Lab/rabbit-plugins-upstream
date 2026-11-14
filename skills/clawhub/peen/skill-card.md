## Description:

Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to set up and operate Peen for durable coding-agent sessions, configure providers and workspaces, connect clients over WebSocket, and inspect or control retained work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions pipe a mutable remote installer directly into Bash; the security scan also reports undeclared setup writes and incomplete analysis.

Mitigation: Avoid direct download-to-Bash installation. If proceeding, verify a pinned installer from a trusted source, review its requested permissions and configuration writes, and inspect the setup guide before running it.

Risk: The skill operates an agent with access to its assigned project, and the documented default controller setup uses the host Docker socket.

Mitigation: Open only projects the operator is willing to let the agent change. Keep the Docker socket, SSH directories, and credentials out of the agent's reach; use a real API token and wss:// when exposing Peen beyond a trusted local network.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/peen)
- [Peen repository and project documentation](https://github.com/psyb0t/peen)
- [Setup, providers, WebSocket, and REST](references/setup.md)
- [Where Peen and its agents run](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [HTTP API reference](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)
- [Recovery and continuation](https://github.com/psyb0t/peen/blob/main/docs/agents.md#recovery-after-a-crash)
- [Configuration](https://github.com/psyb0t/peen/blob/main/docs/configuration.md)
- [Deployment](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [Harness](https://github.com/psyb0t/peen/blob/main/docs/harness.md)
- [Project rules](https://github.com/psyb0t/peen/blob/main/docs/rules.md)
- [Skills](https://github.com/psyb0t/peen/blob/main/docs/skills.md)
- [Session events](https://github.com/psyb0t/peen/blob/main/docs/events.md)
- [Hooks](https://github.com/psyb0t/peen/blob/main/docs/hooks.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, API calls]

**Output Format:** [Markdown with inline shell, JSON, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.49.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
