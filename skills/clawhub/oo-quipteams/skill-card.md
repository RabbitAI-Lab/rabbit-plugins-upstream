## Description:

Enables agents to search and retrieve Quipteams employee, device, asset, kit, product, and quote data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users with an OOMOL-connected Quipteams account use this skill to inspect live connector schemas and retrieve Quipteams records such as employees, devices, assets, kits, products, and quotes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance may ask an agent to run remote installer scripts directly in a shell.

Mitigation: Review the OOMOL CLI installation path, prefer an official version-pinned installer, inspect downloaded installers before running them, and avoid administrator privileges unless required.

Risk: Quipteams employee, device, asset, and quote data is routed through OOMOL for connector execution.

Mitigation: Confirm the deployment is approved for routing this Quipteams data through OOMOL before use.

## Reference(s):

- [Quipteams homepage](https://www.quipteams.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-quipteams)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions should inspect the live action schema before submitting JSON payloads.]

## Skill Version(s):

1.0.3 (source: evidence release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
