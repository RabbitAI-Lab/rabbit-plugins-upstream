## Description:

Guides developers through configuring and operating Peen for durable coding-agent sessions, workspace rules, and WebSocket-based work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up a Peen provider and Docker workspace, start and monitor sessions, and add project-specific agent instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unauthenticated API exposed beyond the local machine could let others control the coding agent.

Mitigation: Bind to 127.0.0.1 and set a non-empty PEEN_API_TOKEN; use HTTPS and WSS for remote access.

Risk: The agent can read or change mounted files and may encounter secrets.

Mitigation: Mount only the intended workspace and secrets the agent is allowed to access; review trusted project hooks.

Risk: Using a floating Docker image tag can change the deployed software unexpectedly.

Mitigation: Pin the Docker image to a reviewed version or digest.

## Reference(s):

- [Peen setup and usage guide](artifact/references/setup.md)
- [Peen project homepage](https://github.com/psyb0t/peen)

## Skill Output:

**Output Type(s):** [Configuration instructions, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker and a configured model provider.]

## Skill Version(s):

0.19.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
