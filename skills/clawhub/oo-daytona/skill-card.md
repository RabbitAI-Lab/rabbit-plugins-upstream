## Description:

Daytona (daytona.io). Use this skill for reading, creating, inspecting, starting, stopping, and deleting Daytona sandboxes through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Daytona sandboxes through the oo CLI after inspecting live connector schemas. It supports read, write, and destructive sandbox actions with confirmation requirements for state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that run shell or PowerShell scripts directly.

Mitigation: Review the setup path before installation and prefer verified, version-pinned oo CLI release instructions.

Risk: Daytona write actions can change sandbox state and destructive actions can delete sandboxes.

Mitigation: Confirm the exact payload and effect before write actions, and require explicit approval for destructive deletions.

## Reference(s):

- [Daytona homepage](https://www.daytona.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-daytona)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live Daytona connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
