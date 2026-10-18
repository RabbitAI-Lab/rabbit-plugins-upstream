## Description:

Helps developers configure and operate Peen for Docker-backed coding work, project instructions, and durable sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up Peen with a provider and Docker workspace, send coding tasks, and inspect or control persistent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer runs downloaded code and Peen's controller has broad Docker authority.

Mitigation: Review or pin the installer before running it and install only if you trust the Peen project.

Risk: A coding agent can change files in its workspace or encounter sensitive credentials.

Mitigation: Open only intended projects; keep secrets, SSH keys, and Docker socket access out of agent workspaces.

Risk: An exposed API or stored transcripts may reveal sensitive work and tool output.

Mitigation: Set PEEN_API_TOKEN before non-local exposure and treat stored transcripts as sensitive.

## Reference(s):

- [Peen setup guide](references/setup.md)
- [Peen configuration](https://github.com/psyb0t/peen/blob/main/docs/configuration.md)
- [Peen deployment](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [Peen agent isolation](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [Peen API reference](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workspace and session examples require operator-specific paths and credentials.]

## Skill Version(s):

0.26.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
