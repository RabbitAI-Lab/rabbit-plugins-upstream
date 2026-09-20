## Description:

This skill operates Dropbox through an OOMOL-connected account for reading, creating, updating, and deleting Dropbox data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Dropbox through an OOMOL-connected account, including reading, creating, updating, sharing, and deleting Dropbox files and folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes running a remotely fetched installer script with shell execution.

Mitigation: Review the oo CLI installer source and provenance before running setup, and prefer a pinned or verified installation method when available.

Risk: Dropbox write and destructive actions can create, modify, move, delete, restore, or revoke user data and links.

Mitigation: Require explicit user approval for the exact target, payload, and expected effect before any write or destructive action.

## Reference(s):

- [ClawHub Dropbox skill page](https://clawhub.ai/oomol/skills/oo-dropbox)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Dropbox homepage](https://www.dropbox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before running Dropbox actions and to request approval before write or destructive actions.]

## Skill Version(s):

1.0.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
