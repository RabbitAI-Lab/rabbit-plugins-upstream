## Description:

ProjectManager lets an agent search and read ProjectManager projects and tasks through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect ProjectManager projects and tasks from an OOMOL-connected account. It is intended for read-only project lookup workflows that require live schema inspection before connector calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer scripts that may be piped directly into a shell.

Mitigation: Review setup steps manually, prefer a verified and versioned installation channel, and avoid running downloaded scripts from an elevated terminal.

Risk: Connector access depends on account connection state, scopes, credentials, and billing status.

Mitigation: Keep setup and recovery flows under user control, and run routine read actions only after inspecting the live connector schema.

## Reference(s):

- [ProjectManager homepage](https://www.projectmanager.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ProjectManager ClawHub listing](https://clawhub.ai/oomol/skills/oo-projectmanager)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ProjectManager connector responses returned as JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
