## Description:

Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure Peen and its provider and workspace settings, then operate durable coding-agent sessions through its command-line and WebSocket workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup workflow executes a changeable online installer before configuring access to the computer.

Mitigation: Review and pin the installer before running it.

Risk: The controller has powerful Docker access, and an agent's filesystem and shell access depend on its workspace and execution mode.

Mitigation: Restrict the workspace root, keep workers isolated, and do not expose the Docker socket, SSH files, or credentials to an agent unless explicitly intended.

Risk: Sessions can expose workspace content in transcripts, and an externally reachable API or unattended work can create additional security and privacy risks.

Mitigation: Exclude secrets from agent-readable workspaces, confirm provider data handling, keep the API local unless protected by authentication and TLS, and explicitly stop unattended work.

## Reference(s):

- [Peen setup and provider guide](references/setup.md)
- [Peen project documentation](https://github.com/psyb0t/peen)
- [Where Peen runs](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [Peen configuration](https://github.com/psyb0t/peen/blob/main/docs/configuration.md)
- [Peen deployment](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [Peen API reference](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell commands, JSON examples, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.28.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
