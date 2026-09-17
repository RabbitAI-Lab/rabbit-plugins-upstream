## Description:

Cisco Meraki helps an agent search and read Cisco Meraki data through the OOMOL Cisco Meraki connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external users can use this skill to retrieve Cisco Meraki device, organization, network, and inventory information from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup flow directs users to run remote installer scripts directly in a shell.

Mitigation: Review the installer first, prefer a verified official package or manual installation path, and avoid elevated shells unless the vendor clearly requires them.

Risk: The skill requires Cisco Meraki access through OOMOL as an intermediary.

Mitigation: Install and use the skill only when the organization is comfortable connecting Cisco Meraki through OOMOL and has reviewed the required account permissions.

Risk: Future write or destructive connector actions could change or remove Cisco Meraki data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before executing write actions, and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub Cisco Meraki skill](https://clawhub.ai/oomol/skills/oo-cisco-meraki)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Cisco Meraki homepage](https://meraki.cisco.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from the oo CLI when connector actions are executed.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
