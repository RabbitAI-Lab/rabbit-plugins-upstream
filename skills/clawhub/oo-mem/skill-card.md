## Description:

Mem operates Mem notes through an OOMOL-connected account, supporting reading, creating, updating, searching, trashing, restoring, and deleting notes via the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Mem notes from a connected Mem account. It is intended for note reading, search, creation, updates, trashing, restoration, and permanent deletion when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may lead users to run remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation path before installing; prefer an official package manager, a pinned release, or a downloaded installer that has been inspected or verified.

Risk: Write and destructive actions can change, trash, or permanently delete Mem notes.

Mitigation: Confirm the exact note, payload, and effect with the user before running state-changing actions, and use permanent deletion only after explicit approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mem)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Mem Homepage](https://mem.ai)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before forming action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
