## Description:

Configure and operate Peen for durable coding-agent sessions, Docker workspaces, provider setup, and WebSocket-based work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up Peen, open project workspaces, send coding-agent tasks, and inspect or control persistent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing by piping an unpinned remote script into a shell can run unreviewed code.

Mitigation: Download and verify the installer first, or use a pinned release artifact.

Risk: Docker access and agent shell permissions can affect the host or modify workspace files.

Mitigation: Review Docker mounts and execution spaces, and grant access only to projects the agent may change.

Risk: Workspace files and tool output may expose credentials in stored transcripts.

Mitigation: Keep secrets out of accessible workspaces and avoid having the agent read or print credentials.

Risk: An exposed Peen endpoint could allow unauthorized access to agent sessions.

Mitigation: Bind to localhost unless an API token and TLS are configured.

## Reference(s):

- [Peen release on ClawHub](https://clawhub.ai/psyb0t/skills/peen)
- [Peen setup guide](references/setup.md)
- [Peen deployment documentation](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [Peen agent execution spaces](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [Peen HTTP API documentation](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with command, configuration, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe persistent sessions and WebSocket events.]

## Skill Version(s):

0.26.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
