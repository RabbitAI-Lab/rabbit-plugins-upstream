## Description:

Manages Common Ninja widgets and projects through an OOMOL-connected account, including widget configuration and embedding information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Common Ninja users and developers use this skill to find, create, update, and remove widgets and to retrieve project details, widget configuration, editor links, and embed code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup offers remote shell installer commands.

Mitigation: Install the CLI through a verified, manual process; do not let an agent run remote installer one-liners automatically.

Risk: Widget changes or deletion can alter or permanently remove account data.

Mitigation: Review the target and exact changes, confirm write actions, and explicitly approve destructive actions before execution.

## Reference(s):

- [Common Ninja skill release](https://clawhub.ai/oomol/skills/oo-commonninja)
- [Common Ninja](https://www.commoninja.com/)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Code, Configuration, Guidance]

**Output Format:** [Markdown with JSON or HTML snippets when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include widget details, editor URLs, and embed code.]

## Skill Version(s):

1.0.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
