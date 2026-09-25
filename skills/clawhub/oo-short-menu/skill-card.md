## Description:

Short Menu (shortmenu.com) manages Short Menu links through the OOMOL short_menu connector, including creating, updating, and deleting links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Short Menu links from an agent through their OOMOL-connected account. It supports creating, updating, and deleting short links after inspecting the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer execution for the oo CLI.

Mitigation: Review the installation path first and prefer an official, versioned, verifiable installer or package-manager method.

Risk: The skill can create, update, or delete Short Menu links.

Mitigation: Confirm the exact payload and effect before running write actions, and require explicit approval before destructive deletion.

## Reference(s):

- [Short Menu homepage](https://shortmenu.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-short-menu)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
