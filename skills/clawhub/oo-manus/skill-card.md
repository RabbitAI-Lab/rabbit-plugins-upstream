## Description:

Manus (manus.im). Use this skill for ANY Manus request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to operate Manus through an OOMOL-connected account, including creating, listing, updating, stopping, messaging, and deleting Manus tasks. It is intended for users who need Manus workflow operations via the oo CLI while preserving confirmation checks for write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer scripts that can execute directly in a shell.

Mitigation: Prefer a pinned, signed, or package-manager installation path for the oo CLI and review installer contents before execution.

Risk: Write and destructive Manus actions can change account state or permanently delete stopped tasks.

Mitigation: Confirm the exact action, payload, target account, and task or project identifier with the user before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-manus)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Manus homepage](https://manus.im)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that read from or change Manus account state, depending on the selected action.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
