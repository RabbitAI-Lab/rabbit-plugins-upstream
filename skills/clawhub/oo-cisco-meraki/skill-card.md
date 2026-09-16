## Description:

Cisco Meraki helps agents search and read Cisco Meraki data through an OOMOL-connected account and the cisco_meraki connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Cisco Meraki organizations, networks, inventory devices, and individual devices by serial number through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cisco Meraki request data and results are routed through OOMOL.

Mitigation: Use a dedicated least-privilege Meraki API key and confirm OOMOL retention and logging practices before use.

Risk: Installer guidance includes pipe-to-shell commands.

Mitigation: Avoid running the installer until the installer source and integrity have been independently verified.

## Reference(s):

- [Cisco Meraki homepage](https://meraki.cisco.com/)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cisco-meraki)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Cisco Meraki connector results as JSON when actions are executed with the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
