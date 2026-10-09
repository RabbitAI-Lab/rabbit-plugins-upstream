## Description:

Guides developers through configuring and operating Peen, including Docker workspaces, WebSocket turns, project rules, and durable session inspection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to set up a Peen coding-agent workspace, configure a provider, send and monitor work, and manage persistent sessions and project instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can read and change files in its mounted project workspace.

Mitigation: Mount only the specific project directory intended for agent work; exclude home directories, credentials, and the Docker socket.

Risk: Transcripts, tool output, logs, and session state persist and may expose secrets.

Mitigation: Keep provider tokens out of prompts and tool output, and store credentials in a gitignored environment file or secret store.

Risk: An exposed service without adequate authentication can allow unauthorized access.

Mitigation: Set a real API token before exposing the service and use HTTPS and secure WebSockets outside a trusted local network.

## Reference(s):

- [Peen release on ClawHub](https://clawhub.ai/psyb0t/skills/peen)
- [Peen setup guide](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Docker, WebSocket, and REST examples.]

## Skill Version(s):

0.14.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
