## Description:

Govee (govee.com). Use this skill for Govee requests that read device information or control supported device capabilities through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list Govee devices, inspect supported capabilities, read current device state, list scenes, and control documented device settings through an OOMOL-connected Govee account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The oo CLI installer can be run through one-line curl or PowerShell commands.

Mitigation: Install only if OOMOL is trusted, and review the installer or use documented platform-specific install steps before running it.

Risk: Device-control actions can change Govee device state.

Mitigation: Confirm the exact device-control payload and expected effect with the user before executing state-changing actions.

Risk: Broad Govee requests may cause the agent to invoke connector actions without enough context.

Mitigation: Fetch the live connector schema first and confirm target identifiers and capabilities before running actions that modify devices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-govee)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Govee homepage](https://www.govee.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
