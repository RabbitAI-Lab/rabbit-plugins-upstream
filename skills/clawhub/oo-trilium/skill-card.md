## Description:

This skill lets an agent read, search, create, update, and delete TriliumNext Notes through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected TriliumNext Notes workspace from an agent, including note search, content retrieval, note-tree edits, attachment operations, and confirmed writes or deletions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write to or delete data in a connected TriliumNext Notes account.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

Risk: The skill gives an agent access to note metadata, note content, branches, attributes, and attachments in the connected account.

Mitigation: Install and use it only when the agent is intended to access that TriliumNext Notes workspace.

Risk: First-time setup can involve running an oo CLI installer command.

Mitigation: Review the oo CLI installer before running first-time setup commands.

## Reference(s):

- [TriliumNext Notes homepage](https://triliumnotes.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trilium)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
