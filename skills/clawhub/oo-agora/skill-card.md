## Description:

Agora (agora.io). Use this skill for ANY Agora request: reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and administer Agora Console projects through OOMOL's oo CLI. It supports project listing, project detail lookup, usage checks, project creation, project status changes, and primary App Certificate management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The one-time oo CLI installer runs shell or PowerShell commands from a remote URL.

Mitigation: Install only when Agora management through OOMOL is intended, and verify the oo CLI source through OOMOL's official documentation before running the installer.

Risk: Project creation changes Agora account state.

Mitigation: Confirm the exact payload and expected effect with the user before running create_project.

Risk: Certificate reset, certificate enable or disable, and project status changes can disrupt Agora applications.

Mitigation: Require explicit user approval of the target project and action before running reset_primary_certificate, set_primary_certificate, or update_project_status.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-agora)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Agora homepage](https://www.agora.io)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
