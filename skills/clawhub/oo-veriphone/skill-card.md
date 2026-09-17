## Description:

Veriphone lets an agent use an OOMOL-connected account to verify phone numbers and retrieve verification credit information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Veriphone through the OOMOL oo CLI for phone-number validation, carrier and region lookup, and account credit checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that run downloaded scripts directly in a shell.

Mitigation: Before running setup, download the installer from the official source, inspect it, and verify any available signature or checksum instead of piping it directly into Bash or PowerShell.

## Reference(s):

- [Veriphone ClawHub skill page](https://clawhub.ai/oomol/skills/oo-veriphone)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Veriphone connection setup](https://console.oomol.com/app-connections?provider=veriphone)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector action schemas before constructing request payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
