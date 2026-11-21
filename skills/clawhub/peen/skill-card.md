## Description:

Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to install and configure Peen, connect a model provider, and open a project workspace. It guides them through sending work to durable coding-agent sessions and inspecting or controlling those sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guide pipes a mutable remote installer into Bash, and the security review was partial.

Mitigation: Review the installer and verify its integrity before installing; check the host-level access the installation will receive against the intended setup.

Risk: The skill documents Peen workspaces as direct shell and filesystem access for the model; the controller setup can also expose the host Docker socket to Peen.

Mitigation: Open only projects the operator is willing to let the agent change. Do not expose the Docker socket, SSH files, or credentials to the agent unless needed, and use a real API token with secure WebSocket transport when exposing Peen beyond a trusted local network.

## Reference(s):

- [Setup, providers, WebSocket, and REST](references/setup.md)
- [Peen deployment guide](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [Where Peen runs](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [Peen API reference](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown instructions with shell commands, configuration examples, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.50.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
