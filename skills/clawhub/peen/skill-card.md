## Description:

Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure and run Peen as a durable coding-agent backend, connect to it over WebSocket and REST, and manage project harness files, sessions, jobs, and execution controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup can expose an unauthenticated coding-agent service with workspace access to the network.

Mitigation: Bind the service to localhost for local use, set a strong PEEN_API_TOKEN before remote or shared-network use, and use wss:// or HTTPS outside trusted local environments.

Risk: A Peen workspace gives the agent shell and filesystem access under the configured execution profile.

Mitigation: Mount only a disposable or intended project workspace, avoid mounting home directories, credential directories, or the Docker socket, and review changes to .env, AGENTS.md, .agents files, and hooks.

Risk: Sessions are not sandboxed by default; isolation depends on the actual execution profile.

Mitigation: Choose an execution profile appropriate to the workspace risk and avoid assuming the default native profile provides isolation.

## Reference(s):

- [Skill page](https://clawhub.ai/psyb0t/skills/peen)
- [Publisher profile](https://clawhub.ai/user/psyb0t)
- [Setup, providers, WebSocket, and REST](references/setup.md)
- [Homepage](https://github.com/psyb0t/peen)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline shell, dotenv, JavaScript, HTTP, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational instructions for Docker setup, provider configuration, WebSocket messaging, REST inspection, and project harness files.]

## Skill Version(s):

0.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
