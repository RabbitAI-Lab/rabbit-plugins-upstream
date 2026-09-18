## Description:

Quipteams helps an agent search and read Quipteams data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to retrieve Quipteams employees, devices, kits, products, quotes, assets, and device action records through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include one-line remote installer commands for the oo CLI.

Mitigation: Use a verified, signed, or package-manager-based installation path before running Quipteams actions.

Risk: The skill retrieves potentially sensitive Quipteams account, employee, device, procurement, and asset information through OOMOL as a broker.

Mitigation: Install only when that brokered access is acceptable, and limit execution to documented read actions unless a future write action is clearly labeled and explicitly approved.

Risk: Incorrect action payloads can lead to failed or misleading connector requests.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing each JSON payload.

## Reference(s):

- [ClawHub Quipteams Skill](https://clawhub.ai/oomol/skills/oo-quipteams)
- [Quipteams Homepage](https://www.quipteams.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
