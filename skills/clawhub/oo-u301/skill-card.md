## Description:

This skill lets an agent operate U301 short links through OOMOL's oo CLI, including listing domains, creating shortened URLs, and deleting links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage U301 short links through an OOMOL-connected account, including listing available domains, creating shortened URLs, and deleting links with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance runs remote installer scripts directly from URLs without integrity checks.

Mitigation: Install the oo CLI only from a trusted source, verify installer contents before execution, or use a safer pinned package-manager installation path.

Risk: The delete_link action can remove an existing U301 short link.

Mitigation: Confirm the exact domain and slug with the user and obtain explicit approval before running the destructive action.

Risk: Write actions can change data in the connected U301 workspace.

Mitigation: Inspect the live connector schema, validate the JSON payload, and confirm the intended effect with the user before execution.

## Reference(s):

- [U301 homepage](https://u301.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-u301)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector commands and JSON responses; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
