## Description:

mymind (mymind.com). Use this skill for ANY mymind request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to operate a user's connected mymind account through OOMOL for reading, searching, creating, updating, organizing, and deleting mymind content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded scripts directly.

Mitigation: Review the setup section before installing and prefer verified official releases or package-manager guidance; avoid pipe-to-shell installation unless the user accepts that risk.

Risk: Write actions can change mymind state.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

Risk: Destructive actions can delete, remove, or overwrite mymind data.

Mitigation: Confirm the explicit target and obtain user approval before running destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mymind)
- [mymind homepage](https://mymind.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
