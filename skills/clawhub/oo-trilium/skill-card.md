## Description:

TriliumNext Notes helps agents read, create, update, and delete TriliumNext Notes data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate TriliumNext Notes from an agent, including note search, reading, creation, updates, attachments, branches, attributes, and explicit-confirmation delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Use the official OOMOL CLI installation documentation or a version-pinned, verified installer before installing.

Risk: Write and destructive actions can change or remove TriliumNext Notes data.

Mitigation: Review write and delete payloads carefully and require explicit confirmation before destructive actions.

## Reference(s):

- [TriliumNext Notes homepage](https://triliumnotes.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trilium)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
