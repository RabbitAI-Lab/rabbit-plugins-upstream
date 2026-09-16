## Description:

Operates Accredible Certificates through an OOMOL-connected account using the oo CLI for reading, creating, searching, listing, and deleting certificate data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate an Accredible Certificates connector from an agent, including credential and group discovery plus confirmed create and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Review the installer source or install the oo CLI through a trusted package or signed release path before running setup.

Risk: Create and delete actions can change or remove Accredible credential data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before write or destructive actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-accredible-certificates)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Accredible Certificates homepage](https://www.accredible.com/)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
