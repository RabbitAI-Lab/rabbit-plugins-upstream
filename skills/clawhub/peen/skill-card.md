## Description:

Configure and operate Peen, the durable coding-agent backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure a Peen provider and Docker workspace, send work over WebSocket, add project harness rules, and inspect or control durable coding-agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill helps configure a backend that gives an agent shell and filesystem access to the mounted workspace.

Mitigation: Install it only for a Peen project the operator intentionally wants an agent to operate, and mount only a specific project workspace.

Risk: Broad mounts or sensitive directories can expose credentials, SSH keys, host resources, or unrelated files to the agent.

Mitigation: Do not mount a home directory, SSH keys, the Docker socket, or broad credential folders; use reviewed writable mounts and stronger isolation when needed.

Risk: Provider credentials and API tokens can be exposed through configuration, transcripts, or network access if handled carelessly.

Mitigation: Keep credentials in a reviewed .env or secret store, avoid embedding secrets in PEEN_UPSTREAMS, use PEEN_API_TOKEN and TLS before exposing the service, and never put tokens in URLs.

Risk: Workspace hooks can run commands and should not be enabled for untrusted workspaces.

Mitigation: Enable workspace hooks only for trusted workspaces and review hook behavior before use.

## Reference(s):

- [Set up and use Peen](references/setup.md)
- [Peen GitHub repository](https://github.com/psyb0t/peen)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/peen)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, dotenv, JavaScript, and text code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include Docker commands, WebSocket examples, REST inspection commands, and workspace harness configuration.]

## Skill Version(s):

0.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
