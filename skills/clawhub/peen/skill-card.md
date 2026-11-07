## Description:

Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure Peen, connect coding agents to project workspaces, send and monitor session tasks, and manage retained work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions run an unverified installer downloaded from a mutable URL with the invoking user's privileges; some referenced material was only partly analyzed.

Mitigation: Review and verify the installer before running it, and use a trusted, pinned source. Follow the skill's guidance to limit workspace and credential access and to set an API token before exposing Peen beyond a trusted local network.

## Reference(s):

- [Setup, providers, WebSocket, and REST](references/setup.md)
- [Where the agent runs](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [Configuration](https://github.com/psyb0t/peen/blob/main/docs/configuration.md)
- [Deployment](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [HTTP API reference](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)
- [Recovery and continuation](https://github.com/psyb0t/peen/blob/main/docs/agents.md#recovery-after-a-crash)

## Skill Output:

**Output Type(s):** [Configuration instructions, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands, configuration examples, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.45.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
