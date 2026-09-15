## Description:

Configure and operate Peen, a durable coding-agent backend for provider setup, Docker workspaces, WebSocket work submission, project harness rules, and durable session inspection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure Peen for a dedicated project workspace, run its Docker server, send agent work over WebSocket, and inspect or control durable sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide Docker execution with mounted workspaces, which can expose host files if broad paths are mounted.

Mitigation: Mount only a dedicated project workspace, avoid home directories, SSH directories, secret-bearing paths, and the Docker socket, and prefer isolated or rootless Docker.

Risk: Peen uses provider credentials and an API token, and tool output is stored in durable transcripts.

Mitigation: Keep credentials in a gitignored .env or deployment secret store, avoid printing secrets, use a real PEEN_API_TOKEN, and use TLS outside trusted local environments.

Risk: The skill may modify .env, AGENTS.md, and .agents/** and can propose curl or network-facing server commands.

Mitigation: Review configuration and harness changes before use, expose services only intentionally, and keep unauthenticated operation limited to local test environments.

## Reference(s):

- [Set up and use Peen](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/peen)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Docker commands, WebSocket and REST examples, workspace harness guidance, and configuration file changes.]

## Skill Version(s):

0.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
