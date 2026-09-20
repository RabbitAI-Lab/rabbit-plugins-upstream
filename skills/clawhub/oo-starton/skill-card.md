## Description:

Starton (starton.com). Use this skill for any Starton request, including reading, creating, updating, and deleting data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage Starton IPFS pins from a connected OOMOL account. It supports listing and reading pins, creating JSON pins, pinning existing IPFS CIDs, and deleting pins with explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-time CLI installation can involve pipe-to-shell commands.

Mitigation: Prefer the linked install guide or verify the installer before running it, and install only if OOMOL's oo CLI is trusted.

Risk: Write actions can create new Starton IPFS pins or pin existing CIDs.

Mitigation: Inspect the live action schema, confirm the exact payload and intended effect with the user, then run the action.

Risk: The delete action can remove a Starton pin.

Mitigation: Confirm the pin identifier and obtain explicit user approval before executing the destructive action.

## Reference(s):

- [Starton homepage](https://starton.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
