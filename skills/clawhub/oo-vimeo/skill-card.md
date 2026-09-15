## Description:

Vimeo (vimeo.com). Use this skill for ANY Vimeo request: reading, creating, updating, and deleting data through the OOMOL-connected Vimeo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Vimeo accounts through the OOMOL `oo` CLI, including reading Vimeo metadata and managing videos, folders, showcases, tags, uploads, replacements, and downloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that security evidence says deserve review before installation.

Mitigation: Review installer contents and verify the OOMOL CLI distribution path before installation; avoid piping remote scripts directly into a shell.

Risk: The skill can perform write and destructive Vimeo actions, including upload, replace, delete, remove, and tag changes.

Mitigation: Confirm exact payloads, targets, and expected effects before write actions, and require explicit approval for delete, remove, replace, or upload actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vimeo)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Vimeo](https://vimeo.com)
- [Vimeo service icon](https://static.oomol.com/logo/third-party/vimeo.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are requested as JSON and include data plus an execution ID when actions run.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
