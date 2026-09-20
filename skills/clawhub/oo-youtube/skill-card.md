## Description:

Use this skill to operate YouTube through an OOMOL-connected account for reading, creating, updating, and deleting YouTube data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate YouTube through the oo CLI, including search, listing, content management, playlist, comment, caption, rating, thumbnail, and upload workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute a remote installer for the oo CLI.

Mitigation: Review the installer first or use a verified package or documented manual installation method.

Risk: The skill operates through OOMOL as an intermediary for a connected YouTube account.

Mitigation: Install only when that account access model is acceptable for the intended user and environment.

Risk: Write and destructive actions can post, upload, update, rate, overwrite, or delete YouTube resources.

Mitigation: Confirm the exact payload, target resource, and intended effect with the user before running those actions.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [YouTube homepage](https://www.youtube.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload or response handling.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live action schemas before execution and to require confirmation for write or destructive YouTube actions.]

## Skill Version(s):

1.0.5 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
