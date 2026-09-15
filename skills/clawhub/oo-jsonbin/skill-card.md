## Description:

JSONBin.io helps agents create, read, update, and delete JSONBin.io bins through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to manage JSONBin.io records through OOMOL's JSONBin connector. It supports live action-schema inspection before running read, write, or delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes remote installer commands for the oo CLI.

Mitigation: Use a trusted, verified oo CLI release path for installation instead of allowing an agent to pipe remote scripts directly into a shell.

Risk: Write and destructive actions can change or delete JSONBin.io data.

Mitigation: Confirm the exact payload, target bin, and expected effect with the user before running write or delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jsonbin)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [JSONBin.io homepage](https://jsonbin.io/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before composing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
